import os
import signal
from src.providers.gcp_pubsub import PubSubSource
from src.providers.gcp_gcs import GCSBufferedSink
from src.providers.gcp_dlq import DeadLetterSink
from src.core.batcher import BatchSinkWrapper
from src.services.ingestor.processor import EventProcessor
from src.services.ingestor.worker import IngestionWorker

def bootstrap():
    # Dependency Injection
    source = PubSubSource(os.getenv("GCP_PROJECT_ID"), os.getenv("SUB_ID"))
    processor = EventProcessor()
    
    raw_sink = GCSBufferedSink(os.getenv("GCS_BUCKET"))
    sink = BatchSinkWrapper(raw_sink) # Wrap for 1 PB efficiency
    dlq = DeadLetterSink(os.getenv("GCS_BUCKET"))

    worker = IngestionWorker(source, processor, sink, dlq)

    # Graceful Shutdown
    signal.signal(signal.SIGTERM, lambda s, f: sink.close() or exit(0))
    
    print("🚀 1 PB Ingestor Started...")
    worker.run()

if __name__ == "__main__":
    bootstrap()