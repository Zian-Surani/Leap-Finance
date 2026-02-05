# ui/dashboard.py

import streamlit as st
from datetime import datetime

from models.user_state import UserState


def render_dashboard(user: UserState, current_time: datetime):
    st.subheader("Current State")

    col1, col2, col3 = st.columns(3)

    col1.metric("Preparation Capital", round(user.preparation_capital, 2))
    col2.metric("Commitment Band", user.current_band or "None")
    col3.metric("Escrow Status", "DECAYING" if user.is_in_decay else "STABLE")

    st.caption(f"System Time: {current_time.strftime('%Y-%m-%d %H:%M')}")
