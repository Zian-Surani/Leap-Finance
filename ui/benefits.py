# ui/benefits.py

import streamlit as st
from datetime import datetime

from models.user_state import UserState
from models.benefit import BenefitStatus


def render_benefits_ledger(user: UserState, current_time: datetime):
    st.subheader("Escrowed Benefits Ledger")

    if not user.benefits:
        st.caption("No benefits configured.")
        return

    for benefit in user.benefits.values():
        col1, col2, col3 = st.columns([3, 2, 2])

        # --- Name ---
        if benefit.status == BenefitStatus.EXPIRED:
            col1.markdown(f"~~{benefit.name}~~")
        else:
            col1.markdown(f"**{benefit.name}**")

        # --- Status ---
        if benefit.status == BenefitStatus.LOCKED:
            col2.markdown("LOCKED")
        elif benefit.status == BenefitStatus.ACTIVE:
            col2.markdown("ACTIVE")
        elif benefit.status == BenefitStatus.DECAYING:
            hours_left = int(
                (benefit.decay_deadline - current_time).total_seconds() / 3600
            )
            col2.markdown(f"DECAYING ({hours_left}h left)")
        else:
            col2.markdown("EXPIRED")

        # --- Threshold / Value ---
        col3.markdown(
            f"Unlock PC ≥ {benefit.unlock_pc_threshold}"
        )
