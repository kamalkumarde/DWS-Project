import json
import uuid
import time
import multiprocessing
from google.cloud import pubsub_v1
from datetime import datetime, timezone

# Configuration
PROJECT_ID = "dws-project-mar26"
TOPIC_ID = "raw-events"
MESSAGES_PER_SECOND = 5000  # Adjust based on your test goals
DURATION_SECONDS = 60

def generate_payload():
    """Generates a valid SensorEvent based on your Pydantic model."""
    return {
        "event_id": str(uuid.uuid4()),
        "type": "sensor_reading",
        "producer_id": f"load-tester-{multiprocessing.current_process().name}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "payload": {
            "sensor_id": f"SN-{uuid.uuid4().hex[:6]}",
            "temperature": 25.5,
            "humidity": 45.0
        }
    }

def publisher_worker(project_id, topic_id, count):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    for _ in range(count):
        data = json.dumps(generate_payload()).encode("utf-8")
        publisher.publish(topic_path, data)

if __name__ == "__main__":
    print(f"🔥 Starting Load Test: {MESSAGES_PER_SECOND} msg/s for {DURATION_SECONDS}s")
    
    num_processes = multiprocessing.cpu_count()
    msgs_per_process = (MESSAGES_PER_SECOND * DURATION_SECONDS) // num_processes
    
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(
            target=publisher_worker, 
            args=(PROJECT_ID, TOPIC_ID, msgs_per_process)
        )
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        
    print("✅ Load Test Complete. Check Grafana for throughput metrics!")