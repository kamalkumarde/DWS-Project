import json
import time
from google.cloud import pubsub_v1

# Configuration
PROJECT_ID = "dws-project-mar26"  # Your Dev Project
TOPIC_ID = "raw-events-stream"

def publish_messages(count=10):
    # 1. Initialize Publisher with Batch Settings (Crucial for 1 PB Scale)
    # We batch by 1MB or 100 messages to optimize network calls
    batch_settings = pubsub_v1.types.BatchSettings(
        max_bytes=1024 * 1024,  # 1 MB
        max_latency=1,          # 1 second
    )
    
    publisher = pubsub_v1.PublisherClient(batch_settings=batch_settings)
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

    print(f"Publishing {count} messages to {topic_path}...")

    for i in range(count):
        # Create a sample data payload
        data_payload = {
            "event_id": f"evt_{i}_{int(time.time())}",
            "timestamp": time.time(),
            "payload": "sensor_reading",
            "value": i * 1.5
        }
        
        # Data must be binarized (utf-8)
        data = json.dumps(data_payload).encode("utf-8")

        # Non-blocking call
        future = publisher.publish(topic_path, data)
        
        # Optional: Add a callback to ensure it was sent
        future.add_done_callback(lambda f: print(f"Published ID: {f.result()}"))

    print("Batching complete. Waiting for background threads to finish...")

if __name__ == "__main__":
    publish_messages(50)