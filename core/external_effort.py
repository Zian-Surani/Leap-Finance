# core/external_effort.py

from datetime import datetime
from typing import Literal

from models.user_state import UserState
from core.pc_engine import apply_activity_pc


# Allowed validation outcomes
ValidationResult = Literal["pass", "fail"]


def validate_external_effort(
    comprehension_score: float,
    speaking_completed: bool,
    min_score_threshold: float = 0.6
) -> ValidationResult:
    """
    Validation gate for external learning.
    This simulates:
    - micro quiz OR
    - speaking check OR
    - adaptive questions

    Returns 'pass' or 'fail'.
    """

    if comprehension_score >= min_score_threshold:
        return "pass"

    if speaking_completed:
        return "pass"

    return "fail"


def register_external_effort(
    user: UserState,
    effort_minutes: float,
    validation_result: ValidationResult,
    timestamp: datetime
) -> float:
    """
    Converts validated external effort into PC.
    Unvalidated effort yields zero PC.
    """

    if validation_result != "pass":
        # Log rejected effort (for realism / audit)
        user.log_activity({
            "type": "external_unvalidated",
            "units": effort_minutes,
            "timestamp": timestamp,
            "pc_delta": 0.0
        })
        return 0.0

    # Treat validated external effort as low-weight 'video'
    # Explicitly conservative
    pc_delta = apply_activity_pc(
        user=user,
        activity_type="video",
        units=effort_minutes / 10,   # normalize minutes → units
        timestamp=timestamp
    )

    return pc_delta
