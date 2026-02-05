# app.py

import streamlit as st
import json
from datetime import datetime

from models.user_state import UserState
from models.benefit import Benefit

from ui.dashboard import render_dashboard
from ui.simulator import render_simulator
from ui.visualizations import render_visuals
from ui.benefits import render_benefits_ledger
from ui.audit import render_audit_log
from ui.metrics import render_metrics_mapping
from ui.tradeoffs import render_tradeoffs
from ui.scenarios import render_scenario_selector

from utils.time_utils import advance_time


# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Leap – Preparation Capital Simulator",
    layout="wide"
)

st.title("Preparation Capital & Commitment Simulator")


# --------------------------------------------------
# Helper: load mock benefits (BOM-safe)
# --------------------------------------------------
def load_mock_benefits(user: UserState):
    if user.benefits:
        return

    try:
        with open("data/mock_benefits.json", "r", encoding="utf-8-sig") as f:
            benefits = json.load(f)

        for b in benefits:
            user.benefits[b["benefit_id"]] = Benefit(**b)

    except Exception as e:
        st.error(f"Failed to load mock benefits: {e}")
        st.stop()


# --------------------------------------------------
# Session state
# --------------------------------------------------
if "user" not in st.session_state:
    st.session_state.user = UserState(user_id="demo_user")

if "current_time" not in st.session_state:
    st.session_state.current_time = datetime.now()


user = st.session_state.user
current_time = st.session_state.current_time

load_mock_benefits(user)


# --------------------------------------------------
# Sidebar controls
# --------------------------------------------------
with st.sidebar:
    st.subheader("System Time Control")

    days_forward = st.number_input(
        "Advance time by days",
        min_value=0,
        max_value=30,
        value=0
    )

    if st.button("Apply Time Advance"):
        st.session_state.current_time = advance_time(
            st.session_state.current_time,
            days=days_forward
        )
        st.rerun()

    st.divider()

    render_scenario_selector()


# --------------------------------------------------
# MAIN RENDER FLOW (LOCKED ORDER)
# --------------------------------------------------

render_dashboard(user, st.session_state.current_time)
st.divider()

render_benefits_ledger(user, st.session_state.current_time)
st.divider()

render_audit_log(user)
st.divider()

render_simulator(user)
st.divider()

render_visuals(user)
st.divider()

render_metrics_mapping()
render_tradeoffs()
