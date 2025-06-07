from fastapi import APIRouter, HTTPException
from store import user_busy_slots

router = APIRouter()

@router.get("/calendar/{user_id}")
def get_user_calendar(user_id: int):
    if user_id not in user_busy_slots:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user_id,
        "busy": user_busy_slots[user_id]
    }
