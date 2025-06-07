from datetime import datetime, timedelta

def parse_time(time_str: str) -> datetime:
    return datetime.strptime(time_str, "%H:%M")

def format_time(time_obj: datetime) -> str:
    return time_obj.strftime("%H:%M")

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for curr_start, curr_end in intervals[1:]:
        last_start, last_end = merged[-1]
        if curr_start <= last_end:
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            merged.append((curr_start, curr_end))
    return merged
