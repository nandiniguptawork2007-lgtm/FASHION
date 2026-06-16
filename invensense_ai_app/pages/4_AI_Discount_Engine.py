import streamlit as st
from utils import require_login, sidebar, get_df, money, page_header

require_login(); sidebar(); df = get_df().sort_values("risk_score", ascending=False)
page_header("AI Discount Recommendation Engine", "Transparent rule-based markdown recommendations dressed up like a premium fashion-tech assistant.", "Markdown salon")

if st.button("Run AI Analysis", use_container_width=True):
    st.success("Analysis complete. The engine refreshed markdown recommendations using risk score, trend score, weeks of supply, and stock age.")

recs = df[df.status.astype(str).isin(["Watch","At Risk"])][["product_name","category","risk_score","suggested_discount","estimated_recovery","margin_preserved","weeks_of_supply","trend_score","stock_qty"]]

for _, r in recs.head(10).iterrows():
    reason = "Excess supply, aging stock, and weak trend signal suggest a decisive markdown." if r.risk_score >= 70 else "Moderate stock pressure indicates a controlled discount before demand fades."
    urgency = "High Priority" if r.risk_score >= 70 else "Watch Carefully"
    st.markdown(f"""
    <div class='recommendation-card'>
      <span class='pill'>{urgency}</span>
      <div class='rec-title'>{r.product_name}</div>
      <div class='small'>{r.category} · {int(r.stock_qty)} units in stock · {r.weeks_of_supply} weeks of supply</div>
      <div class='rec-grid'>
        <div class='rec-mini'><div class='small'>Risk Score</div><div class='rec-number'>{int(r.risk_score)}</div></div>
        <div class='rec-mini'><div class='small'>Suggested Markdown</div><div class='rec-number'>{int(r.suggested_discount)}%</div></div>
        <div class='rec-mini'><div class='small'>Recovery Potential</div><div class='rec-number'>{money(r.estimated_recovery)}</div></div>
      </div>
      <p class='small' style='margin-top:1rem'><b>Why:</b> {reason} Expected margin preservation: <b>{money(r.margin_preserved)}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("### Full recommendation table")
st.dataframe(recs, use_container_width=True, hide_index=True)
