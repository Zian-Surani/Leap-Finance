# ui/simulator.py

import streamlit as st
from datetime import datetime, timedelta

from core.pc_engine import apply_activity_pc, apply_inactivity_decay
from core.external_effort import (
    validate_external_effort,
    register_external_effort
)
from core.bands_engine import (
    enter_band_if_eligible,
    check_band_maintenance
)
from core.escrow_engine import (
    lock_new_benefits,
    start_decay_for_all,
    attempt_recovery,
    expire_benefits
)
from models.user_state import UserState


def render_simulator(user: UserState):
    st.subheader("Behavior Simulator")

    col1, col2 = st.columns(2)

    with col1:
        activity_type = st.selectbox(
            "Activity Type",
            ["video", "practice", "speaking", "mock_test"]
        )
        units = st.number_input("Units (minutes/tests)", min_value=1.0, value=10.0)

        if st.button("Log Verified Activity"):
            apply_activity_pc(
                user,
                activity_type,
                units / 10,
                datetime.now()
            )
            enter_band_if_eligible(user, datetime.now())

    with col2:
        st.markdown("**External Effort (YouTube Simulation)**")
        minutes = st.number_input("Minutes Watched", min_value=5.0, value=30.0)
        quiz_score = st.slider("Comprehension Score", 0.0, 1.0, 0.7)
        speaking_done = st.checkbox("Speaking Prompt Completed")

        if st.button("Validate External Effort"):
            result = validate_external_effort(
                quiz_score,
                speaking_done
            )
            register_external_effort(
                user,
                minutes,
                result,
                datetime.now()
            )
            enter_band_if_eligible(user, datetime.now())

    st.divider()

    if st.button("Advance Time by 2 Days"):
        future_time = datetime.now() + timedelta(days=2)

        apply_inactivity_decay(user, future_time)

        if check_band_maintenance(user, future_time):
            start_decay_for_all(user, future_time)

        expire_benefits(user, future_time)
