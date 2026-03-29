from google.cloud import pubsub_v1
from src.core.interfaces import BaseSource

class PubSubSource(BaseSource):
    def __init__(self, project_id, subscription_id):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.path = self.subscriber.subscription_path(project_id, subscription_id)

    def connect(self):
        print(f"Connected to {self.path}")

    def start_streaming(self, callback):
        def _wrapper(message):
            callback(message.data)
            message.ack()
        
        future = self.subscriber.subscribe(self.path, callback=_wrapper)
        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()