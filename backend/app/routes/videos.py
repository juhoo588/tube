from fastapi import APIRouter
from app.services.trend_detector import detect_trending

router = APIRouter()

@router.get('/trending')
def trending():
    return detect_trending()
