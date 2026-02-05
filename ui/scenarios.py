# ui/scenarios.py

import streamlit as st


def render_scenario_selector():
    st.subheader("Scenario Loader")

    scenario = st.selectbox(
        "Select behavior pattern (pre-fills inputs only)",
        ["Manual", "Disciplined", "Erratic", "Dropout"]
    )

    st.caption(
        "Scenarios pre-fill behavior assumptions. "
        "They do not auto-execute actions."
    )

    return scenario
