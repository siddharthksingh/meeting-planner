from pydantic import BaseModel, Field
from typing import List, Tuple

class UserBusy(BaseModel):
    id: int
    busy: List[Tuple[str, str]] = Field(..., description="List of busy time intervals")

class SlotRequest(BaseModel):
    users: List[UserBusy]

class BookMeetingRequest(BaseModel):
    user_ids: List[int]
    start_time: str  # "HH:MM"
    end_time: str    # "HH:MM"