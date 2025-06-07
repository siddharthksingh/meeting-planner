from fastapi import APIRouter
from models.schemas import SlotRequest
from store import user_busy_slots

router = APIRouter()

@router.post("/slots")
def add_user_slots(slot_request: SlotRequest):
    for user in slot_request.users:
        user_busy_slots[user.id] = user.busy
    return {"message": "Slots stored successfully", "data": user_busy_slots}
