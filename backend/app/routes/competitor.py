from fastapi import APIRouter
from app.services.competitor_reverse_engine import channel_pattern, opportunity_gap

router = APIRouter(prefix="/competitor")

@router.get('/pattern/{channel_id}')
def get_pattern(channel_id: str):
    return channel_pattern({"id": channel_id})

@router.post('/gap')
def get_gap(my_channel: dict, competitor: dict):
    return {"gaps": opportunity_gap(my_channel, competitor)}
