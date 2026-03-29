import json
import logging
from src.core.models import SensorEvent
from pydantic import ValidationError

class EventProcessor:
    def process(self, raw_data: bytes):
        try:
            data = json.loads(raw_data)
            
            # 1. Check the discriminator 'type'
            event_type = data.get("type")
            
            if event_type == "sensor_reading":
                # 2. Use model_validate - Pydantic handles the 'type' alias automatically
                return SensorEvent.model_validate(data), None
            
            # If type is unknown, treat as error/DLQ
            return None, raw_data
            
        except (json.JSONDecodeError, ValidationError) as e:
            # Log the error so you can see it in GitHub Action logs
            logging.error(f"Validation failed: {e}")
            return None, raw_data