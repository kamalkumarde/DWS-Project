from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T", bound=BaseModel)

class BaseEvent(BaseModel, Generic[T]):
    model_config = ConfigDict(strict=True, frozen=True)
    event_id: str = Field(..., min_length=1)
    event_type: str = Field(..., alias="type")
    producer_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    payload: T

class SensorPayload(BaseModel):
    sensor_id: str
    temperature: float = Field(..., ge=-50, le=150)
    humidity: float = Field(..., ge=0, le=100)

class SensorEvent(BaseEvent[SensorPayload]):
    pass