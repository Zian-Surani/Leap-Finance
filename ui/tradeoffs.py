# ui/tradeoffs.py

import streamlit as st


def render_tradeoffs():
    with st.expander("Known Tradeoffs & Design Constraints"):
        st.markdown("""
- System prioritizes long-term preparation consistency over short-term engagement spikes
- Requires users to acknowledge visible consequences of inactivity
- Escrowed benefits introduce deliberate pressure rather than soft motivation
- Prototype focuses on behavioral validity and system design, not UI polish or scale
""")
