from fastapi import FastAPI
from .database import Base, engine
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="IoT Sensor Pipeline")

# Create tables
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)