import streamlit as st
from utils import require_login, sidebar, get_df, page_header

require_login(); sidebar(); df = get_df()
page_header("Reports Module", "Export boardroom-ready report packs from the in-app inventory dataset.", "Report atelier")

reports = {
    "Inventory Summary Report": df.describe(include="all").to_string(),
    "Slow-Moving Inventory Report": df.sort_values("weekly_sales").head(15).to_string(index=False),
    "AI Markdown Strategy Report": df.sort_values("risk_score", ascending=False)[["sku","product_name","risk_score","suggested_discount","estimated_recovery"]].to_string(index=False),
    "Profit Recovery Report": df[["product_name","estimated_recovery","margin_preserved"]].sort_values("estimated_recovery", ascending=False).to_string(index=False),
}

cols = st.columns(2, gap="large")
for i, (name, content) in enumerate(reports.items()):
    with cols[i%2]:
        st.markdown(f"""
        <div class='editorial-card'>
          <span class='pill'>Export pack</span>
          <h3>{name}</h3>
          <p class='small'>Preview, download, and share with leadership. Styled for quick management review.</p>
        </div>
        """, unsafe_allow_html=True)
        st.download_button(f"Download {name}.txt", content, file_name=name.lower().replace(" ", "_")+".txt", use_container_width=True)
        st.download_button(f"Download {name}.json", df.to_json(orient="records", indent=2), file_name=name.lower().replace(" ", "_")+".json", use_container_width=True)
