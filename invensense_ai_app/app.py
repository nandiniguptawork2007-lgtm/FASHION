import streamlit as st
from utils import inject_css, DEMO_EMAIL, DEMO_PASSWORD

inject_css()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/1_Dashboard.py")

left, right = st.columns([1.35, .75], gap="large")
with left:
    st.markdown("""
    <div class="fashion-hero">
      <span class="eyebrow">✦ Velvet retail intelligence</span>
      <h1>Reduce Dead Stock.<br/>Recover Lost Profit.</h1>
      <p>InvenSense AI gives fast-fashion retailers an editorial-grade command center for inventory health, markdown strategy, and profit recovery — no database, no API, just a deployable Streamlit prototype with built-in sample data.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.markdown("<div class='editorial-card'><span class='pill'>Runway Signal</span><h3>Trend-aware risk</h3><p class='small'>Spot slow movers before they turn into clearance-room ghosts.</p></div>", unsafe_allow_html=True)
    c2.markdown("<div class='editorial-card'><span class='pill'>Margin Drama</span><h3>Markdown planning</h3><p class='small'>Simulate discounts with revenue and margin impact in real time.</p></div>", unsafe_allow_html=True)
    c3.markdown("<div class='editorial-card'><span class='pill'>Boardroom Ready</span><h3>Reports</h3><p class='small'>Export insights for managers, founders, and the fashionably impatient.</p></div>", unsafe_allow_html=True)

with right:
    st.markdown("<div class='editorial-card'>", unsafe_allow_html=True)
    st.markdown("### Welcome Back")
    st.caption("Demo credentials are prefilled below.")
    email = st.text_input("Email", value=DEMO_EMAIL)
    password = st.text_input("Password", type="password", value=DEMO_PASSWORD)
    if st.button("Login", use_container_width=True):
        if email == DEMO_EMAIL and password == DEMO_PASSWORD:
            st.session_state.logged_in = True
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials. Use demo@invensense.ai / demo123")
    if st.button("Demo Login", use_container_width=True):
        st.session_state.logged_in = True
        st.switch_page("pages/1_Dashboard.py")
    st.markdown("<p class='small'>Secure demo mode · rule-based recommendations · 50 in-app fashion SKUs</p></div>", unsafe_allow_html=True)
