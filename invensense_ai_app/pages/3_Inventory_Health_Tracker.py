import streamlit as st
import plotly.express as px
from utils import require_login, sidebar, get_df, page_header, style_plot, kpi

require_login(); sidebar(); df = get_df()
page_header("Inventory Health Tracker", "A rule-based risk studio using weeks of supply, sales velocity, trend score, and inventory age.", "Risk couture")

status = st.multiselect("Health status", ["Healthy","Watch","At Risk"], default=["Healthy","Watch","At Risk"])
cat = st.multiselect("Category", sorted(df.category.unique()))
view = df[df.status.astype(str).isin(status)]
if cat: view = view[view.category.isin(cat)]

c1,c2,c3 = st.columns(3)
with c1: kpi("Average Risk", round(view.risk_score.mean(),1), "selected view", "⚠️")
with c2: kpi("Avg Weeks Supply", round(view.weeks_of_supply.mean(),1), "stock coverage", "📅")
with c3: kpi("Avg Trend Score", round(view.trend_score.mean(),1), "demand signal", "📈")

st.dataframe(view[["sku","product_name","category","weeks_of_supply","weekly_sales","trend_score","risk_score","status"]], use_container_width=True, hide_index=True)

c1,c2,c3 = st.columns(3, gap="large")
with c1: st.plotly_chart(style_plot(px.pie(df, names="status", title="Risk Distribution", hole=.45)), use_container_width=True)
with c2: st.plotly_chart(style_plot(px.density_heatmap(df, x="category", y="status", z="risk_score", histfunc="avg", title="Category Heatmap")), use_container_width=True)
with c3: st.plotly_chart(style_plot(px.histogram(df, x="age_days", color="status", title="Inventory Aging")), use_container_width=True)
