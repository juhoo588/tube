from fastapi import APIRouter
from app.services.rising_shorts_bot import hunt_rising_shorts

router = APIRouter(prefix="/shorts")

@router.get('/rising')
def rising_shorts():
    return hunt_rising_shorts()
