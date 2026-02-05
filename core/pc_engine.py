# core/pc_engine.py

from datetime import datetime, timedelta

from config.constants import (
    PC_WEIGHTS,
    CONSISTENCY_WINDOW_DAYS,
    CONSISTENCY_MULTIPLIER,
    DECAY_START_HOURS,
    DECAY_RATE_PER_DAY,
    MAX_DAILY_DECAY,
    MIN_PC
)

from models.user_state import UserState


def apply_activity_pc(
    user: UserState,
    activity_type: str,
    units: float,
    timestamp: datetime
) -> float:
    """
    Apply PC gain from a verified activity.
    Returns the PC delta applied.
    """

    base_weight = PC_WEIGHTS.get(activity_type, 0.0)
    pc_delta = base_weight * units

    # Consistency bonus
    if user.last_activity_time:
        delta_days = (timestamp - user.last_activity_time).days
        if delta_days <= CONSISTENCY_WINDOW_DAYS:
            pc_delta *= CONSISTENCY_MULTIPLIER

    user.add_pc(pc_delta)
    user.log_activity({
        "type": activity_type,
        "units": units,
        "timestamp": timestamp,
        "pc_delta": pc_delta
    })

    return pc_delta


def apply_inactivity_decay(
    user: UserState,
    current_time: datetime
) -> float:
    """
    Applies decay to PC based on inactivity.
    Returns negative PC delta (or 0 if no decay).
    """

    if not user.last_activity_time:
        return 0.0

    hours_inactive = (current_time - user.last_activity_time).total_seconds() / 3600

    if hours_inactive <= DECAY_START_HOURS:
        return 0.0

    inactive_days = (hours_inactive - DECAY_START_HOURS) / 24
    raw_decay = inactive_days * DECAY_RATE_PER_DAY

    decay_fraction = min(raw_decay, MAX_DAILY_DECAY)
    pc_loss = user.preparation_capital * decay_fraction

    user.preparation_capital = max(
        MIN_PC,
        user.preparation_capital - pc_loss
    )

    return -pc_loss
