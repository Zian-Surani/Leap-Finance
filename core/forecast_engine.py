# core/forecast_engine.py

from datetime import datetime, timedelta

from models.user_state import UserState
from config.constants import DECAY_RATE_PER_DAY


def project_pc_forward(
    user: UserState,
    days_ahead: int,
    avg_daily_pc_gain: float
) -> list[tuple[int, float]]:
    """
    Projects PC forward assuming:
    - constant average daily gain
    - decay applied if gain is zero
    Returns list of (day_offset, projected_pc)
    """

    projections = []
    projected_pc = user.preparation_capital

    for day in range(1, days_ahead + 1):
        if avg_daily_pc_gain > 0:
            projected_pc += avg_daily_pc_gain
        else:
            # decay-only scenario
            projected_pc -= projected_pc * DECAY_RATE_PER_DAY

        projected_pc = max(0.0, projected_pc)
        projections.append((day, projected_pc))

    return projections


def estimate_avg_daily_pc(user: UserState, lookback_days: int = 7) -> float:
    """
    Computes average daily PC gain from recent history.
    """

    cutoff = datetime.now() - timedelta(days=lookback_days)
    recent_deltas = [
        a["pc_delta"] for a in user.activity_log
        if a["timestamp"] >= cutoff and a["pc_delta"] > 0
    ]

    if not recent_deltas:
        return 0.0

    return sum(recent_deltas) / lookback_days


def forecast_outcome(
    user: UserState,
    target_pc: float,
    exam_days_remaining: int
) -> dict:
    """
    Returns forecast summary.
    """

    avg_daily_pc = estimate_avg_daily_pc(user)
    projections = project_pc_forward(
        user,
        exam_days_remaining,
        avg_daily_pc
    )

    success_day = next(
        (day for day, pc in projections if pc >= target_pc),
        None
    )

    return {
        "avg_daily_pc": avg_daily_pc,
        "projected_curve": projections,
        "success_day": success_day,
        "will_succeed": success_day is not None
    }
