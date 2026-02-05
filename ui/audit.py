# ui/audit.py

import streamlit as st
from models.user_state import UserState


def render_audit_log(user: UserState):
    st.subheader("System Audit Log")

    if not user.activity_log:
        st.caption("No system events recorded yet.")
        return

    # Show last 6 events (most recent first)
    for event in user.activity_log[-6:][::-1]:
        ts = event["timestamp"].strftime("%Y-%m-%d %H:%M")
        st.markdown(
            f"- **{ts}** | `{event['type']}` | ΔPC: **{round(event['pc_delta'], 2)}**"
        )
