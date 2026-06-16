import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

DEMO_EMAIL = "demo@invensense.ai"
DEMO_PASSWORD = "demo123"

st.set_page_config(page_title="InvenSense AI", page_icon="💄", layout="wide")

VELVET = "#5A1236"
MERLOT = "#7A1E48"
ROSE = "#B76E79"
CHAMPAGNE = "#F4E6D7"
IVORY = "#FFFCF7"
INK = "#211721"
TAUPE = "#7D6B75"
GOLD = "#C9A227"

PLOT_COLORS = [VELVET, ROSE, GOLD, "#8A6F91", "#D8A7B1", "#7B506F", "#C48C6A"]


def inject_css():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    :root {{
      --velvet:{VELVET}; --merlot:{MERLOT}; --rose:{ROSE}; --champagne:{CHAMPAGNE};
      --ivory:{IVORY}; --ink:{INK}; --taupe:{TAUPE}; --gold:{GOLD};
    }}

    .stApp {{
      background:
        radial-gradient(circle at top left, rgba(183,110,121,.22), transparent 33%),
        radial-gradient(circle at bottom right, rgba(244,230,215,.78), transparent 38%),
        linear-gradient(135deg, #fffcf7 0%, #fff7f4 47%, #f8edf0 100%);
      color: var(--ink);
      font-family: 'Inter', sans-serif;
    }}

    h1, h2, h3 {{font-family:'Playfair Display', serif !important; color:var(--velvet); letter-spacing:-.02em;}}
    h1 {{font-size:2.75rem !important;}}

    [data-testid="stSidebar"] {{
      background: linear-gradient(180deg, #3A0B24 0%, #5A1236 48%, #210914 100%);
      border-right: 1px solid rgba(244,230,215,.22);
      box-shadow: 18px 0 50px rgba(90,18,54,.18);
    }}
    [data-testid="stSidebar"] * {{color:#fffaf5 !important;}}
    [data-testid="stSidebarNav"] {{display:none !important;}}
    [data-testid="collapsedControl"] {{color:var(--velvet) !important;}}

    .brand-lockup {{padding: 1.1rem .8rem 1rem .8rem;}}
    .brand-name {{font-family:'Playfair Display',serif; font-size:1.55rem; font-weight:800; letter-spacing:-.03em;}}
    .brand-sub {{font-size:.77rem; color:rgba(255,250,245,.72) !important; margin-top:.15rem;}}
    .sidebar-chip {{display:inline-block; margin-top:.8rem; padding:.35rem .7rem; border:1px solid rgba(244,230,215,.22); border-radius:999px; background:rgba(255,255,255,.08); font-size:.72rem;}}

    div[data-testid="stSidebarUserContent"] a {{
      display:block; padding:.72rem .86rem; margin:.22rem .35rem; border-radius:16px;
      text-decoration:none; font-weight:700; background:transparent;
      transition: all .18s ease; border:1px solid transparent;
    }}
    div[data-testid="stSidebarUserContent"] a:hover {{
      background: rgba(255,255,255,.12); border-color:rgba(244,230,215,.18); transform: translateX(3px);
    }}

    .fashion-hero {{
      position:relative; overflow:hidden; padding:3.1rem 3.25rem; border-radius:34px;
      background:
        linear-gradient(120deg, rgba(90,18,54,.96), rgba(122,30,72,.92)),
        radial-gradient(circle at 88% 20%, rgba(244,230,215,.38), transparent 26%);
      color:#fffaf5; box-shadow:0 30px 80px rgba(90,18,54,.28); border:1px solid rgba(244,230,215,.18);
    }}
    .fashion-hero:after {{
      content:""; position:absolute; right:-80px; top:-80px; width:310px; height:310px; border-radius:50%;
      background: radial-gradient(circle, rgba(244,230,215,.32), transparent 68%);
    }}
    .fashion-hero h1 {{color:#fffaf5 !important; font-size:3.55rem !important; line-height:1.02; margin:.65rem 0 1rem;}}
    .fashion-hero p {{font-size:1.08rem; max-width:760px; color:rgba(255,250,245,.88);}}

    .eyebrow {{display:inline-flex; gap:.45rem; align-items:center; padding:.38rem .78rem; border-radius:999px; background:rgba(255,255,255,.13); border:1px solid rgba(255,255,255,.22); font-weight:800; font-size:.78rem; letter-spacing:.04em; text-transform:uppercase;}}
    .editorial-card, .card {{
      background:rgba(255,252,247,.92); border:1px solid rgba(90,18,54,.10); padding:1.15rem; border-radius:24px;
      box-shadow: 0 18px 50px rgba(90,18,54,.10); backdrop-filter: blur(10px);
    }}
    .editorial-card:hover {{box-shadow:0 26px 66px rgba(90,18,54,.15); transform:translateY(-2px); transition:.2s ease;}}
    .metric-title {{font-size:.78rem; color:var(--taupe); font-weight:800; text-transform:uppercase; letter-spacing:.055em;}}
    .metric-value {{font-size:1.82rem; font-weight:900; color:var(--velvet); margin:.15rem 0;}}
    .small {{color:var(--taupe); font-size:.88rem;}}
    .pill {{display:inline-block; padding:.28rem .68rem; border-radius:999px; background:#F7E8EC; color:var(--velvet); font-weight:800; font-size:.76rem; border:1px solid rgba(90,18,54,.09);}}
    .status-Healthy {{background:#EAF8EF; color:#166534;}}
    .status-Watch {{background:#FFF5D6; color:#92400E;}}
    .status-AtRisk {{background:#FBE7EC; color:#9F1239;}}

    .section-band {{padding:1rem 1.15rem; border-radius:24px; background:linear-gradient(135deg, rgba(255,252,247,.95), rgba(244,230,215,.55)); border:1px solid rgba(90,18,54,.1);}}
    .recommendation-card {{
      padding:1.35rem; margin:.75rem 0; border-radius:28px; background:linear-gradient(145deg, #fffdf9, #fff3f6);
      border:1px solid rgba(90,18,54,.12); box-shadow:0 22px 60px rgba(90,18,54,.14); position:relative; overflow:hidden;
    }}
    .recommendation-card:before {{content:""; position:absolute; right:-50px; top:-70px; width:180px; height:180px; background:rgba(183,110,121,.18); border-radius:50%;}}
    .rec-title {{font-family:'Playfair Display',serif; font-size:1.35rem; color:var(--velvet); font-weight:800;}}
    .rec-grid {{display:grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap:.75rem; margin-top:1rem;}}
    .rec-mini {{padding:.8rem; border-radius:18px; background:rgba(255,255,255,.68); border:1px solid rgba(90,18,54,.08);}}
    .rec-number {{font-size:1.35rem; font-weight:900; color:var(--merlot);}}

    div.stButton > button, div.stDownloadButton > button {{
      border-radius:16px; border:0; background:linear-gradient(135deg, var(--velvet), var(--rose)); color:white; font-weight:800; padding:.72rem 1.1rem;
      box-shadow: 0 12px 30px rgba(90,18,54,.18);
    }}
    div.stButton > button:hover, div.stDownloadButton > button:hover {{filter:brightness(.96); color:white; transform:translateY(-1px);}}

    [data-testid="stDataFrame"] {{border-radius:24px; overflow:hidden; box-shadow:0 16px 45px rgba(90,18,54,.08); border:1px solid rgba(90,18,54,.09);}}
    .stTabs [data-baseweb="tab-list"] {{gap:.5rem;}}
    .stTabs [data-baseweb="tab"] {{border-radius:999px; background:#fff8f5; padding:.55rem 1rem;}}
    </style>
    """, unsafe_allow_html=True)


def money(x):
    return f"₹{float(x):,.0f}"


def require_login():
    inject_css()
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        st.switch_page("app.py")


def sidebar():
    with st.sidebar:
        st.markdown("""
        <div class='brand-lockup'>
          <div class='brand-name'>💄 InvenSense AI</div>
          <div class='brand-sub'>Runway-grade inventory intelligence</div>
          <div class='sidebar-chip'>Velvet Edition</div>
        </div>
        """, unsafe_allow_html=True)
        st.page_link("pages/1_Dashboard.py", label="🏠  Dashboard")
        st.page_link("pages/2_Inventory_Management.py", label="📦  Inventory Management")
        st.page_link("pages/3_Inventory_Health_Tracker.py", label="❤️  Health Tracker")
        st.page_link("pages/4_AI_Discount_Engine.py", label="🤖  Discount Engine")
        st.page_link("pages/5_Markdown_Simulator.py", label="📉  Markdown Simulator")
        st.page_link("pages/6_Analytics.py", label="📊  Analytics")
        st.page_link("pages/7_Reports.py", label="📄  Reports")
        st.page_link("pages/8_Settings.py", label="⚙️  Settings")
        st.divider()
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.switch_page("app.py")


def get_df():
    from data import load_inventory
    if "inventory_df" not in st.session_state:
        st.session_state.inventory_df = load_inventory()
    return st.session_state.inventory_df.copy()


def kpi(label, value, note="", icon="◆"):
    st.markdown(f"""
    <div class='editorial-card'>
      <div class='metric-title'>{icon} {label}</div>
      <div class='metric-value'>{value}</div>
      <div class='small'>{note}</div>
    </div>
    """, unsafe_allow_html=True)


def page_header(title, subtitle, tag="Fashion intelligence"):
    st.markdown(f"""
    <div class='section-band'>
      <span class='pill'>{tag}</span>
      <h1 style='margin:.35rem 0 .2rem 0'>{title}</h1>
      <div class='small'>{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")


def style_plot(fig, height=360):
    fig.update_layout(
        height=height,
        margin=dict(l=18, r=18, t=52, b=18),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(255,252,247,.65)',
        font=dict(family="Inter", color=INK),
        title_font=dict(family="Playfair Display", color=VELVET, size=22),
        colorway=PLOT_COLORS,
        legend=dict(orientation="h", yanchor="bottom", y=-0.24, xanchor="center", x=.5),
    )
    fig.update_xaxes(showgrid=True, gridcolor="rgba(90,18,54,.07)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(90,18,54,.07)")
    return fig


def status_badge(status):
    cls = str(status).replace(" ", "")
    return f"<span class='pill status-{cls}'>{status}</span>"
