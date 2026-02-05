# utils/time_utils.py

from datetime import datetime, timedelta


def advance_time(
    current_time: datetime,
    days: int = 0,
    hours: int = 0
) -> datetime:
    """
    Advances simulated system time.
    """
    return current_time + timedelta(days=days, hours=hours)


def hours_between(t1: datetime, t2: datetime) -> float:
    """
    Returns absolute hours between two timestamps.
    """
    return abs((t2 - t1).total_seconds()) / 3600
