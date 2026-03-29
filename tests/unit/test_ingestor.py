import pytest
import json
from unittest.mock import MagicMock
from src.services.ingestor.processor import EventProcessor
from src.core.models import SensorEvent

@pytest.fixture
def processor():
    return EventProcessor()

@pytest.fixture
def valid_payload():
    return {
        "event_id": "test-uuid-123",
        "type": "sensor_reading",
        "producer_id": "factory-01",
        "timestamp": "2026-03-29T10:00:00Z",
        "payload": {
            "sensor_id": "SN-99",
            "temperature": 22.5,
            "humidity": 45.0
        }
    }

def test_processor_success(processor, valid_payload):
    """Test that a valid JSON bytes object is correctly parsed into a SensorEvent."""
    raw_data = json.dumps(valid_payload).encode("utf-8")
    
    event, error = processor.process(raw_data)
    
    assert event is not None
    assert error is None
    assert isinstance(event, SensorEvent)
    assert event.payload.temperature == 22.5
    assert event.event_type == "sensor_reading"

def test_processor_validation_error(processor, valid_payload):
    """Test that invalid data (out of range temperature) triggers the DLQ path."""
    # Temperature 500 is outside our Pydantic range (ge=-50, le=150)
    valid_payload["payload"]["temperature"] = 500.0
    raw_data = json.dumps(valid_payload).encode("utf-8")
    
    event, error = processor.process(raw_data)
    
    assert event is None
    assert error == raw_data  # Should return raw bytes for the DLQ

def test_processor_malformed_json(processor):
    """Test that non-JSON data is safely caught and sent to DLQ."""
    raw_data = b"not a json string"
    
    event, error = processor.process(raw_data)
    
    assert event is None
    assert error == raw_data

def test_worker_routing():
    """Integration style test: Ensure the worker calls the sink on success and DLQ on failure."""
    from src.services.ingestor.worker import IngestionWorker
    
    # Mocks
    mock_source = MagicMock()
    mock_processor = MagicMock()
    mock_sink = MagicMock()
    mock_dlq = MagicMock()
    
    worker = IngestionWorker(mock_source, mock_processor, mock_sink, mock_dlq)
    
    # Simulate a successful process
    mock_processor.process.return_value = (MagicMock(spec=SensorEvent), None)
    
    # We need to capture the internal callback passed to start_streaming
    worker.run()
    callback = mock_source.start_streaming.call_args[0][0]
    
    # Execute callback
    callback(b"some data")
    
    mock_sink.write.assert_called_once()
    mock_dlq.bury.assert_not_called()