import streamlit as st
from utils import require_login, sidebar, page_header

require_login(); sidebar()
page_header("Settings & Profile", "Configure store details, risk appetite, and fashion-tech preferences.", "Account studio")

with st.form("settings"):
    st.subheader("Company Information")
    c1, c2 = st.columns(2)
    with c1:
        company = st.text_input("Company Name", "Miranda Mode Retail")
        brand = st.text_input("Retail Brand Name", "Velvet Rack")
        location = st.text_input("Store Location", "Mumbai, India")
    with c2:
        currency = st.selectbox("Preferred Currency", ["INR (₹)", "USD ($)", "EUR (€)"])
        theme = st.selectbox("Theme", ["Velvet & Ivory", "Champagne Light", "Editorial White"])
        notify = st.selectbox("Notifications", ["Email Notifications", "Dashboard Only", "Disabled"])

    st.subheader("Risk Controls")
    threshold = st.slider("Risk Threshold", 40, 90, 70)
    markdown_cap = st.slider("Maximum Markdown %", 10, 70, 35)

    st.subheader("Security")
    st.text_input("Email", "retailer@example.com")
    st.text_input("Password", "********", type="password")
    two_factor = st.checkbox("Enable two-factor authentication", value=True)
    if st.form_submit_button("Save Changes", use_container_width=True):
        st.success("Settings saved for this session.")
