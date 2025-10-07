from fastapi import APIRouter
from app.services.kpi_service import *

router = APIRouter()

@router.get("/classement")
def classement_general(by: str ='team', season: int =2025):
    return get_classification(season, by)