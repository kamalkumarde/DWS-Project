import json
from typing import Dict, Type, Optional
from src.core.models import BaseEvent, SensorEvent

class EventFactory:
    _REGISTRY: Dict[str, Type[BaseEvent]] = {
        "sensor_reading": SensorEvent
    }

    @classmethod
    def get_model(cls, raw_data: bytes) -> Optional[BaseEvent]:
        try:
            data_dict = json.loads(raw_data)
            event_type = data_dict.get("type")
            model_class = cls._REGISTRY.get(event_type)
            return model_class.model_validate(data_dict) if model_class else None
        except Exception:
            return None