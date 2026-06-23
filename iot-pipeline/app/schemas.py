from pydantic import BaseModel

class SensorCreate(BaseModel):
    device_id: str
    temperature: float
    humidity: float