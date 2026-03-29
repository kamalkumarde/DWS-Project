import time
from src.core.interfaces import BaseSink

class BatchSinkWrapper(BaseSink):
    def __init__(self, target_sink, max_batch_size=1000, max_age_seconds=60):
        self.target_sink = target_sink
        self.buffer = []
        self.max_batch_size = max_batch_size
        self.max_age_seconds = max_age_seconds
        self.last_flush = time.time()

    def write(self, event):
        self.buffer.append(event)
        if len(self.buffer) >= self.max_batch_size or (time.time() - self.last_flush) > self.max_age_seconds:
            self.flush()

    def flush(self):
        if self.buffer:
            self.target_sink.batch_write(self.buffer)
            self.buffer.clear()
            self.last_flush = time.time()
            
    def close(self):
        self.flush()