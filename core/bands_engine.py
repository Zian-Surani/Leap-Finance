# core/bands_engine.py

from datetime import datetime, timedelta

from models.user_state import UserState
from config.bands import BANDS


def determine_eligible_band(pc: float) -> str | None:
    """
    Returns the highest band name the user qualifies for.
    """
    eligible = None
    for band in BANDS:
        if pc >= band.min_pc:
            eligible = band.name
    return eligible


def enter_band_if_eligible(user: UserState, current_time: datetime) -> bool:
    """
    Moves user into a higher band if eligible.
    Returns True if band changed.
    """

    eligible_band = determine_eligible_band(user.preparation_capital)

    if eligible_band is None:
        return False

    if user.current_band == eligible_band:
        return False

    # Enter new band
    user.current_band = eligible_band
    user.band_entry_time = current_time
    user.is_in_decay = False

    return True


def check_band_maintenance(
    user: UserState,
    current_time: datetime
) -> bool:
    """
    Checks whether user violated band maintenance.
    Returns True if violation detected.
    """

    if not user.current_band:
        return False

    band = next(
        (b for b in BANDS if b.name == user.current_band),
        None
    )
    if not band:
        return False

    window_start = current_time - timedelta(days=7)
    recent_activities = [
        a for a in user.activity_log
        if a["timestamp"] >= window_start
        and a["pc_delta"] > 0
    ]

    if len(recent_activities) < band.min_weekly_activity:
        return True

    return False
