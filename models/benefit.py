# models/benefit.py

from enum import Enum
from dataclasses import dataclass
from datetime import datetime, timedelta


class BenefitStatus(Enum):
    LOCKED = "locked"        # Earned but not usable
    ACTIVE = "active"        # Fully unlocked
    DECAYING = "decaying"    # At risk due to inactivity
    EXPIRED = "expired"      # Permanently lost


@dataclass
class Benefit:
    benefit_id: str
    name: str
    description: str

    total_value: float              # Monetary or equivalent value
    unlock_pc_threshold: float      # PC required to earn it

    status: BenefitStatus = BenefitStatus.LOCKED

    escrow_start: datetime | None = None
    decay_deadline: datetime | None = None
    expiry_deadline: datetime | None = None

    def is_active(self) -> bool:
        return self.status == BenefitStatus.ACTIVE

    def is_at_risk(self) -> bool:
        return self.status == BenefitStatus.DECAYING

    def has_expired(self) -> bool:
        return self.status == BenefitStatus.EXPIRED
