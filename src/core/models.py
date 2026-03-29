from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
from datetime import datetime, timezone

# Define the TypeVar so T can be used in Generic[T]
T = TypeVar("T")

class BaseEvent(BaseModel, Generic[T]):
    model_config = ConfigDict(strict=False, frozen=True)
    
    event_id: str
    event_type: str = Field(..., alias="type")
    producer_id: str
    timestamp: datetime
    payload: T

    @field_validator('timestamp', mode='before')
    @classmethod
    def parse_timestamp(cls, v):
        if isinstance(v, str):
            # Handles 'Z' suffix by converting it to UTC offset
            return datetime.fromisoformat(v.replace('Z', '+00:00'))
        return v

class SensorPayload(BaseModel):
    sensor_id: str
    temperature: float = Field(..., ge=-50, le=150)
    humidity: float = Field(..., ge=0, le=100)

class SensorEvent(BaseEvent[SensorPayload]):
    pass