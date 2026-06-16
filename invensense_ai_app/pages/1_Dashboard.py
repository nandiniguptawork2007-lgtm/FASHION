import streamlit as st
import pandas as pd
import plotly.express as px
from utils import require_login, sidebar, get_df, kpi, money, page_header, style_plot

require_login(); sidebar(); df = get_df()

page_header("Executive Dashboard",
"Interactive inventory intelligence with complete KPIs, risk runway and recovery analytics.",
"Retail Intelligence")

c1,c2,c3,c4 = st.columns(4)
with c1: kpi("Inventory Value", money(df.total_value.sum()), "Live value", "💎")
with c2: kpi("Products", len(df), "Fashion SKUs", "📦")
with c3: kpi("Recovery Potential", money(df.estimated_recovery.sum()), "Projected", "₹")
with c4: kpi("Margin Saved", money(df.margin_preserved.sum()), "Estimated", "📈")

st.markdown("### Inventory Health Overview")
a,b=st.columns([1,1])
with a:
    fig=px.pie(df,names='status',hole=.55,title='Inventory Health Mix')
    st.plotly_chart(style_plot(fig,420),use_container_width=True)
with b:
    risk=df.groupby('category',as_index=False).risk_score.mean().sort_values('risk_score',ascending=False)
    fig=px.bar(risk,x='category',y='risk_score',text_auto='.1f',title='Category Risk Runway')
    fig.update_traces(textposition='outside')
    st.plotly_chart(style_plot(fig,420),use_container_width=True)

weekly=pd.DataFrame({
'week':['May1','May8','May15','May22','May29','Jun5','Jun12'],
'sales':[185,210,198,240,226,255,238]
})
fig=px.line(weekly,x='week',y='sales',markers=True,title='Weekly Sales Trend')
st.plotly_chart(style_plot(fig,380),use_container_width=True)

st.markdown("### Top Risk Products")
show=df.sort_values('risk_score',ascending=False)[['product_name','category','risk_score','suggested_discount','estimated_recovery']]
st.dataframe(show,use_container_width=True,hide_index=True)
