# models/user_state.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

from models.benefit import Benefit


@dataclass
class UserState:
    user_id: str

    # Core preparation metrics
    preparation_capital: float = 0.0
    last_activity_time: datetime | None = None

    # Commitment band
    current_band: str | None = None
    band_entry_time: datetime | None = None

    # Activity tracking (simulated)
    activity_log: List[Dict] = field(default_factory=list)

    # Escrowed benefits
    benefits: Dict[str, Benefit] = field(default_factory=dict)

    # System flags
    is_in_decay: bool = False

    def log_activity(self, activity: Dict):
        self.activity_log.append(activity)
        self.last_activity_time = activity.get("timestamp", self.last_activity_time)

    def add_pc(self, delta: float):
        self.preparation_capital = max(0.0, self.preparation_capital + delta)

    def get_active_benefits(self) -> List[Benefit]:
        return [b for b in self.benefits.values() if b.is_active()]

    def get_at_risk_benefits(self) -> List[Benefit]:
        return [b for b in self.benefits.values() if b.is_at_risk()]
