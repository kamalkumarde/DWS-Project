from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime, timezone
import dateutil.parser # Ensure this is in requirements.txt

class BaseEvent(BaseModel, Generic[T]):
    model_config = ConfigDict(strict=False, frozen=True) # Change strict to False
    event_id: str
    event_type: str = Field(..., alias="type")
    producer_id: str
    timestamp: datetime # Pydantic V2 will try to parse strings here
    payload: T

    @field_validator('timestamp', mode='before')
    @classmethod
    def parse_timestamp(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v.replace('Z', '+00:00'))
        return v