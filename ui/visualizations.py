# ui/visualizations.py

import streamlit as st
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


from core.forecast_engine import forecast_outcome
from models.user_state import UserState


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

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(target_pc, linestyle="--")
    ax.set_xlabel("Days Ahead")
    ax.set_ylabel("Projected PC")

    st.pyplot(fig)

    if forecast["will_succeed"]:
        st.success(f"Projected success in {forecast['success_day']} days.")
    else:
        st.error("Projected to miss target at current pace.")
