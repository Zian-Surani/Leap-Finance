# utils/validators.py

def validate_positive(value: float, name: str):
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def validate_percentage(value: float, name: str):
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be between 0 and 1")


def validate_non_empty(value, name: str):
    if value is None:
        raise ValueError(f"{name} cannot be None")
