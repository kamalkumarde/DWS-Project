import json
from src.core.models import SensorEvent

class EventProcessor:
    def process(self, raw_data: bytes):
        try:
            data = json.loads(raw_data)
            # Two-pass validation: check type, then validate
            if data.get("type") == "sensor_reading":
                return SensorEvent.model_validate(data), None
            return None, raw_data
        except Exception:
            return None, raw_data