# ui/visualizations.py

import streamlit as st

from core.forecast_engine import forecast_outcome
from models.user_state import UserState


# --- SAFE IMPORT FOR STREAMLIT CLOUD ---
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def render_visuals(user: UserState):
    st.subheader("Momentum Forecast")

    target_pc = st.slider("Target PC", 50, 300, 120)
    days_left = st.slider("Days to Exam", 10, 120, 45)

    forecast = forecast_outcome(user, target_pc, days_left)
    curve = forecast["projected_curve"]

    if not curve:
        st.info("Insufficient data to forecast.")
        return

    x = [d for d, _ in curve]
    y = [pc for _, pc in curve]

    # --- ONLY PLOT IF MATPLOTLIB EXISTS ---
    if plt is not None:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.axhline(target_pc, linestyle="--")
        ax.set_xlabel("Days Ahead")
        ax.set_ylabel("Projected PC")

        st.pyplot(fig)
    else:
        # Fallback for environments without matplotlib
        st.warning("Plotting library unavailable. Showing numeric forecast instead.")
        st.write(f"Average daily PC: {round(forecast['avg_daily_pc'], 2)}")
        st.write(f"Projected success day: {forecast['success_day']}")

    # --- SUCCESS / FAILURE MESSAGE ---
    if forecast["will_succeed"]:
        st.success(f"Projected success in {forecast['success_day']} days.")
    else:
        st.error("Projected to miss target at current pace.")
