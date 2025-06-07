from fastapi import APIRouter, HTTPException
from models.schemas import BookMeetingRequest
from store import user_busy_slots
from utils import parse_time

router = APIRouter()

@router.post("/book")
def book_meeting(payload: BookMeetingRequest):
    start = parse_time(payload.start_time)
    end = parse_time(payload.end_time)

    if start >= end:
        raise HTTPException(status_code=400, detail="Start time must be before end time")

    for user_id in payload.user_ids:
        if user_id not in user_busy_slots:
            user_busy_slots[user_id] = []
        user_busy_slots[user_id].append((payload.start_time, payload.end_time))

    return {
        "message": "Meeting booked successfully",
        "booked_for_users": payload.user_ids,
        "time": f"{payload.start_time}–{payload.end_time}"
    }
