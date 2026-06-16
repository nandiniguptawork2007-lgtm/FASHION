import streamlit as st
import pandas as pd
import plotly.express as px
from utils import require_login, sidebar, get_df, page_header, style_plot

require_login(); sidebar(); df=get_df()

page_header("Advanced Analytics",
"Interactive analytics for stock, sales, revenue and risk.",
"Business Intelligence")

fig=px.scatter(df,x='stock_qty',y='weekly_sales',
color='status',size='total_value',
hover_name='product_name',
title='Stock vs Sales Velocity')
st.plotly_chart(style_plot(fig,450),use_container_width=True)

monthly=pd.DataFrame({
'month':['Jan','Feb','Mar','Apr','May','Jun','Jul'],
'revenue':[320000,370000,410000,500000,455000,390000,445000]
})
fig=px.bar(monthly,x='month',y='revenue',text_auto=True,title='Monthly Revenue')
st.plotly_chart(style_plot(fig,400),use_container_width=True)

risk=df.groupby('category',as_index=False).risk_score.mean()
fig=px.line(risk,x='category',y='risk_score',markers=True,title='Category Risk Trend')
st.plotly_chart(style_plot(fig,380),use_container_width=True)
