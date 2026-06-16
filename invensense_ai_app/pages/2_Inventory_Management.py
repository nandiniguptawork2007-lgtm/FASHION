import streamlit as st
import pandas as pd
from utils import require_login, sidebar, get_df, kpi, money, page_header, status_badge

require_login(); sidebar(); df = get_df()
page_header("Inventory Management", "Upload-free demo data with a polished inventory atelier: search, filter, preview, and export JSON.", "Data atelier")

with st.expander("Optional local upload"):
    st.info("The deployable project includes no CSV files and no database connections. Uploaded Excel/CSV files are session-only.")
    file = st.file_uploader("Upload Excel or CSV for this session", type=["xlsx", "csv"])
    if file:
        try:
            new_df = pd.read_excel(file) if file.name.endswith("xlsx") else pd.read_csv(file)
            st.session_state.inventory_df = new_df
            st.success("Inventory uploaded for this session.")
        except Exception as e:
            st.error(f"Could not read file: {e}")

c1,c2,c3 = st.columns(3)
with c1: kpi("Total Products", len(df), "50 fashion SKUs", "📦")
with c2: kpi("Stock Units", f"{df.stock_qty.sum():,}", "available inventory", "🧵")
with c3: kpi("Inventory Value", money(df.total_value.sum()), "cost basis", "💰")

q = st.text_input("Search products or SKU")
cat = st.multiselect("Filter by category", sorted(df.category.unique()))
view = df.copy()
if q:
    view = view[view.product_name.str.contains(q, case=False, na=False) | view.sku.str.contains(q, case=False, na=False)]
if cat:
    view = view[view.category.isin(cat)]

show = view[["sku","product_name","category","stock_qty","unit_cost","selling_price","total_value","status"]].copy()
show["status"] = show["status"].astype(str)
st.dataframe(show, use_container_width=True, hide_index=True)
st.download_button("Export current view as JSON", data=view.to_json(orient="records", indent=2), file_name="inventory_export.json", use_container_width=True)
