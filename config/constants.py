# config/constants.py

# --- PC WEIGHTS (per verified activity unit) ---
PC_WEIGHTS = {
    "video": 1.0,        # passive, lowest weight
    "practice": 2.0,     # active recall
    "speaking": 3.0,     # high-value
    "mock_test": 5.0     # highest signal
}

# --- CONSISTENCY BONUS ---
CONSISTENCY_WINDOW_DAYS = 3
CONSISTENCY_MULTIPLIER = 1.2

# --- INACTIVITY DECAY ---
DECAY_START_HOURS = 48          # grace before decay
DECAY_RATE_PER_DAY = 0.08       # 8% PC decay per inactive day
MAX_DAILY_DECAY = 0.15          # hard cap to avoid rage-quits

# --- NORMALIZATION ---
MIN_PC = 0.0
