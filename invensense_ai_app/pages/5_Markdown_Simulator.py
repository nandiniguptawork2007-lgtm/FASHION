import streamlit as st
import pandas as pd
import plotly.express as px
from utils import require_login, sidebar, get_df, money, page_header, kpi, style_plot

require_login(); sidebar(); df = get_df()
page_header("Markdown Simulator", "Test discount drama before it hits the shop floor.", "Scenario planning")

product = st.selectbox("Select product", df.product_name)
r = df[df.product_name == product].iloc[0]
discount = st.slider("Discount percentage", 0, 70, int(r.suggested_discount))
new_price = r.selling_price * (1 - discount/100)
units_recovered = min(r.stock_qty, int(r.weekly_sales * (1 + discount/20) * 4))
revenue = new_price * units_recovered
margin = revenue - (r.unit_cost * units_recovered)

c1,c2,c3,c4 = st.columns(4)
with c1: kpi("New Selling Price", money(new_price), f"was {money(r.selling_price)}", "🏷️")
with c2: kpi("Revenue Recovery", money(revenue), "projected", "💰")
with c3: kpi("Margin Impact", money(margin), "after cost", "✂️")
with c4: kpi("Inventory Recovery", f"{units_recovered} units", f"of {r.stock_qty}", "🛍️")

curve = pd.DataFrame({"discount": list(range(0,75,5))})
curve["revenue"] = curve.discount.apply(lambda d: r.selling_price*(1-d/100)*min(r.stock_qty, int(r.weekly_sales*(1+d/20)*4)))
curve["margin"] = curve.discount.apply(lambda d: (r.selling_price*(1-d/100)-r.unit_cost)*min(r.stock_qty, int(r.weekly_sales*(1+d/20)*4)))
fig = px.line(curve, x="discount", y=["revenue","margin"], markers=True, title="Revenue and Margin Impact by Discount")
st.plotly_chart(style_plot(fig, 430), use_container_width=True)
