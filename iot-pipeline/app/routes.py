from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from .database import SessionLocal
from .models import SensorData
from .schemas import SensorCreate
from .s3 import upload_stats_to_s3  

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def home():
    return {"message": "IoT Sensor API running"}


@router.post("/sensor-data")
def create_sensor_data(data: SensorCreate, db: Session = Depends(get_db)):
    new_data = SensorData(
        device_id=data.device_id,
        temperature=data.temperature,
        humidity=data.humidity
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return {"message": "Data stored", "id": new_data.id}


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    avg_temp = db.query(func.avg(SensorData.temperature)).scalar()
    avg_hum = db.query(func.avg(SensorData.humidity)).scalar()
    count = db.query(SensorData).count()

    result = {
        "average_temperature": avg_temp,
        "average_humidity": avg_hum,
        "total_records": count
    }

    file = upload_stats_to_s3(result)

    return {
        "data": result,
        "s3_file": file
    }

@router.get("/sensor-history")
def get_sensor_history(db: Session = Depends(get_db)):
    data = db.query(SensorData).order_by(SensorData.id).all()
    return data