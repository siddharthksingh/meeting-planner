from fastapi import APIRouter, Query
from store import user_busy_slots
from utils import parse_time, format_time, merge_intervals
from datetime import datetime, timedelta

router = APIRouter()

WORKDAY_START = parse_time("09:00")
WORKDAY_END = parse_time("18:00")


@router.get("/suggest")
def suggest_slots(duration: int = Query(..., gt=0)):
    # Convert all busy intervals into datetime objects
    all_busy = []
    for busy_list in user_busy_slots.values():
        for start, end in busy_list:
            all_busy.append((parse_time(start), parse_time(end)))

    merged_busy = merge_intervals(all_busy)

    # Find free slots
    free_slots = []
    current = WORKDAY_START
    for start, end in merged_busy:
        if current < start:
            if (start - current).seconds // 60 >= duration:
                free_slots.append((current, start))
        current = max(current, end)
    if current < WORKDAY_END:
        if (WORKDAY_END - current).seconds // 60 >= duration:
            free_slots.append((current, WORKDAY_END))

    # Trim to 3 results and format
    result = [
        f"{format_time(start)}–{format_time(end)}"
        for start, end in free_slots[:3]
    ]

    return {"suggested_slots": result}
