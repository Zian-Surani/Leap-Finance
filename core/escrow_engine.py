# core/escrow_engine.py

from datetime import datetime, timedelta

from models.user_state import UserState
from models.benefit import Benefit, BenefitStatus
from config.bands import BANDS


def lock_new_benefits(user: UserState, current_time: datetime):
    """
    Lock benefits whose PC threshold has been crossed.
    """

    for benefit in user.benefits.values():
        if (
            benefit.status == BenefitStatus.LOCKED
            and user.preparation_capital >= benefit.unlock_pc_threshold
        ):
            benefit.status = BenefitStatus.ACTIVE
            benefit.escrow_start = current_time
            benefit.decay_deadline = None
            benefit.expiry_deadline = None


def start_decay_for_all(user: UserState, current_time: datetime):
    """
    Moves all active benefits into DECAYING state.
    """

    if not user.current_band:
        return

    band = next(b for b in BANDS if b.name == user.current_band)

    for benefit in user.benefits.values():
        if benefit.status == BenefitStatus.ACTIVE:
            benefit.status = BenefitStatus.DECAYING
            benefit.decay_deadline = current_time + timedelta(days=band.grace_days)
            benefit.expiry_deadline = benefit.decay_deadline + timedelta(days=1)

    user.is_in_decay = True


def attempt_recovery(user: UserState, current_time: datetime) -> bool:
    """
    Attempts to recover benefits if activity resumed within grace window.
    Returns True if recovery succeeded.
    """

    recovered = False

    for benefit in user.benefits.values():
        if (
            benefit.status == BenefitStatus.DECAYING
            and benefit.decay_deadline
            and current_time <= benefit.decay_deadline
        ):
            benefit.status = BenefitStatus.ACTIVE
            benefit.decay_deadline = None
            benefit.expiry_deadline = None
            recovered = True

    if recovered:
        user.is_in_decay = False

    return recovered


def expire_benefits(user: UserState, current_time: datetime):
    """
    Permanently expires benefits past expiry deadline.
    """

    for benefit in user.benefits.values():
        if (
            benefit.status == BenefitStatus.DECAYING
            and benefit.expiry_deadline
            and current_time > benefit.expiry_deadline
        ):
            benefit.status = BenefitStatus.EXPIRED

    # If all decaying benefits are gone, exit decay mode
    if not any(b.is_at_risk() for b in user.benefits.values()):
        user.is_in_decay = False
