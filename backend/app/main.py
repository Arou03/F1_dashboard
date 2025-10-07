from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import kpi_controller

app = FastAPI(title="F1 KPI API")

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kpi_controller.router)