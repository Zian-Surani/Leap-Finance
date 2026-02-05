# config/bands.py

from dataclasses import dataclass


@dataclass(frozen=True)
class CommitmentBand:
    name: str
    min_pc: float
    min_weekly_activity: int        # minimum verified actions per week
    grace_days: int                 # days before escrow decay starts


BANDS = [
    CommitmentBand(
        name="Foundation",
        min_pc=0.0,
        min_weekly_activity=2,
        grace_days=3
    ),
    CommitmentBand(
        name="Momentum",
        min_pc=50.0,
        min_weekly_activity=4,
        grace_days=2
    ),
    CommitmentBand(
        name="Acceleration",
        min_pc=120.0,
        min_weekly_activity=6,
        grace_days=1
    )
]
