import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Autism & Green Space Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS - LIGHT MODERN ECO HEALTH THEME
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

:root {
    --font-family-base: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    --fw-regular: 400;
    --fw-medium: 500;
    --fw-semibold: 600;
    --fw-bold: 700;
    --fw-extrabold: 800;
    --heading-color: #2E8B57;
    --muted-color: #6B7280;
    --title-font-size: 2.4rem;
    --title-line-height: 1.1;
    --title-letter-spacing: -0.02em;
}

html, body, [class*="css"] {
    font-family: var(--font-family-base);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.stApp {
    background: linear-gradient(135deg, #F6FAF7 0%, #EAF4EC 45%, #DFF2FF 100%);
    color: #2C3E50;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FFFFFF 0%, #EFF8F2 100%);
    border-right: 1px solid #D7E5DA;
}

.hero-box {
    background: linear-gradient(120deg, #FFFFFF 0%, #EAF4EC 45%, #DFF2FF 100%);
    padding: 2rem 2.2rem;
    border-radius: 28px;
    border: 1px solid #D7E5DA;
    box-shadow: 0 14px 35px rgba(46, 139, 87, 0.12);
    margin-bottom: 1.5rem;
}

.top-spacer {
    height: 0.35rem;
}

.banner-bottom-spacer {
    height: 0.65rem;
}

.hero-title {
    font-size: clamp(1.9rem, 2.6vw, 2.55rem);
    font-weight: var(--fw-extrabold);
    color: var(--heading-color);
    margin-bottom: 0.35rem;
    letter-spacing: -0.02em;
    line-height: 1.02;
}

.hero-subtitle {
    font-size: clamp(0.95rem, 1.1vw, 1.05rem);
    font-weight: var(--fw-medium);
    color: #52616B;
    max-width: 1100px;
    line-height: 1.5;
}

.badge-row {
    margin-top: 1rem;
    margin-bottom: -5px;
}

.badge {
    display: inline-block;
    padding: 0.45rem 0.8rem;
    border-radius: 999px;
    margin-right: 0.45rem;
    font-weight: var(--fw-semibold);
    font-size: 0.82rem;
    color: #1F3A2D;
    background: #DFF4E6;
    border: 1px solid #BFE8CF;
}

.kpi-card {
    background: #ffffff;
    padding: 0.9rem 1rem;
    border-radius: 22px;
    border: 1px solid rgba(215,229,218,0.6);
    box-shadow: 0 8px 18px rgba(44, 62, 80, 0.06);
    min-height: 110px;
    position: relative;
    overflow: hidden;
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    will-change: transform;
}

.kpi-card::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 22px;
    pointer-events: none;
    opacity: 0;
    transition: opacity 180ms ease;
    background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0));
}

.kpi-card:hover {
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 16px 34px rgba(44, 62, 80, 0.12);
    border-color: rgba(46, 139, 87, 0.28);
}

.kpi-card:hover::after {
    opacity: 1;
}

.kpi-label {
    color: var(--muted-color);
    font-size: 0.76rem;
    font-weight: var(--fw-semibold);
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.kpi-value {
    font-size: clamp(2.15rem, 2.6vw, 3.1rem);
    font-weight: var(--fw-extrabold);
    color: var(--kpi-value-color, #2C3E50);
    margin-top: 0.55rem;
    line-height: 1.02;
    letter-spacing: -0.02em;
}

.kpi-note {
    margin-top: 0.25rem;
    color: var(--muted-color);
    font-size: 0.78rem;
    font-weight: var(--fw-regular);
    line-height: 1.2;
}

.kpi-grid {
    --kpi-gap: 0.95rem;
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: var(--kpi-gap);
    margin-top: 0.25rem;
    margin-bottom: 0.2rem; /* tightened to bring KPI cards closer to following content */
}

@media (max-width: 1200px) {
    .kpi-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 640px) {
    .kpi-grid {
        grid-template-columns: 1fr;
    }
}

.section-card {
    background: rgba(255,255,255,0.94);
    padding: 1.35rem;
    border-radius: 24px;
    border: 1px solid #D7E5DA;
    box-shadow: 0 10px 26px rgba(44, 62, 80, 0.07);
    /* tightened vertical spacing around section cards */
    margin-top: 1.25rem;
    margin-bottom: 0.6rem;
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    will-change: transform;
}

.section-card:hover {
    transform: translateY(-4px) scale(1.01);
    transform-origin: center center;
    box-shadow: 0 16px 34px rgba(44, 62, 80, 0.12);
    border-color: #2E8B57;
}

.chart-card {
    background: linear-gradient(135deg, rgba(235, 247, 238, 0.98) 0%, rgba(255, 255, 255, 0.99) 48%, rgba(247, 241, 212, 0.95) 100%);
    padding: 1.1rem 1.1rem 1rem;
    border-radius: 28px;
    border: 1px solid var(--heading-color) !important;
    box-shadow: 0 10px 26px rgba(44, 62, 80, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.72);
    /* reduced vertical gutter between chart rows */
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
    transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    overflow: visible;
}
.chart-card:hover {
    transform: translateY(-4px) scale(1.01);
    transform-origin: center center;
    box-shadow: 0 16px 34px rgba(44, 62, 80, 0.12), inset 0 0 0 1px rgba(255, 255, 255, 0.75);
    border-color: var(--heading-color) !important;
}

.chart-header {
    margin-bottom: 0.85rem;
}

.chart-title {
    color: var(--heading-color);
    font-size: clamp(1.02rem, 1.35vw, 1.25rem);
    font-weight: var(--fw-extrabold);
    line-height: 1.25;
    margin: 0;
}

.chart-subtitle {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    line-height: 1.65;
    margin-bottom: 0.75rem;
    margin-top: 0.28rem;
}

.dashboard-title,
.section-title,
.carousel-title,
.explorer-hero-title {
    color: #2F855A;
    font-family: var(--font-family-base);
    font-size: var(--title-font-size);
    font-weight: 800;
    line-height: var(--title-line-height);
    letter-spacing: var(--title-letter-spacing);
    margin: 0 0 0.35rem 0;
}

.section-subtitle {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 1rem;
    font-weight: 450;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}

div[data-testid="stCaptionContainer"],
div[data-testid="stCaptionContainer"] * {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}

.insight-box {
    padding: 1rem 1.1rem;
    border-radius: 18px;
    background: #F1FAF4;
    border: 1px solid #CBEBD6;
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    margin-top: 0.15rem;
    margin-bottom: 1.1rem;
    line-height: 1.65;
}

.warning-box {
    padding: 1rem 1.1rem;
    border-radius: 18px;
    background: #FFF1F4;
    border: 1px solid #F7C4CF;
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    margin-top: 0.7rem;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background: #FFFFFF;
    border-radius: 999px;
    border: 1px solid #D7E5DA;
    padding: 8px 18px;
    color: #2C3E50;
    font-weight: var(--fw-semibold);
}

.stTabs [aria-selected="true"] {
    background: #DFF4E6 !important;
    color: var(--heading-color) !important;
}

hr {
    border: none;
    height: 1px;
    background: #D7E5DA;
    margin: 1.1rem 0;
}

.risk-grid-wrap {
    background: rgba(255,255,255,0.92);
    border: 1px solid #D7E5DA;
    border-radius: 24px;
    padding: 1.2rem;
    box-shadow: 0 10px 26px rgba(44, 62, 80, 0.07);
}
.risk-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(28px, 1fr));
    gap: 10px;
    align-items: center;
    margin-top: 0.8rem;
}
.person-icon {
    width: 24px;
    height: 34px;
    position: relative;
    display: inline-block;
    filter: drop-shadow(0 4px 7px rgba(44, 62, 80, 0.12));
}
.person-icon::before {
    content: "";
    position: absolute;
    top: 0;
    left: 7px;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: var(--person-color);
}
.person-icon::after {
    content: "";
    position: absolute;
    top: 13px;
    left: 5px;
    width: 15px;
    height: 19px;
    border-radius: 7px 7px 4px 4px;
    background: var(--person-color);
}
.grid-legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.7rem;
    margin-top: 0.8rem;
    font-size: 0.86rem;
    color: #52616B;
}
.legend-dot {
    display:inline-block;
    width: 11px;
    height: 11px;
    border-radius: 50%;
    margin-right: 5px;
}
.metric-pill {
    display:inline-block;
    padding: 0.28rem 0.6rem;
    border-radius: 999px;
    background: #F1FAF4;
    border: 1px solid #CBEBD6;
    color: #2E8B57;
    font-weight: var(--fw-bold);
    font-size: 0.78rem;
    margin-right: 0.35rem;
}

/* Explorer control card styles */
.control-card {
    /* make the control card visually minimal so individual controls own their outlines */
    background: transparent !important;
    border: none !important;
    border-radius: 18px;
    padding: 0.55rem 0.6rem;
    box-shadow: none !important;
}

/* New: control panel wrapper with subtle gradient and 1px green outline */
.control-panel {
    background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(242,255,246,0.95));
    border: 1px solid var(--heading-color) !important;
    border-radius: 16px;
    padding: 0.65rem 0.75rem;
    box-shadow: 0 8px 20px rgba(46,139,87,0.03);
}
.control-label {
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--heading-color);
    margin-bottom: 0.3rem;
}
.input-wrap { margin-bottom: 0.6rem; }
.mini-card {
    background: rgba(241,250,244,0.9);
    border: 1px solid rgba(203,235,214,0.9);
    padding: 0.45rem 0.6rem;
    border-radius: 12px;
    display: inline-block;
}
.small-btn { display:inline-block; margin-left:0.5rem; }

/* KPI pills for explorer */
.explorer-kpis { display:flex; gap:0.6rem; flex-wrap:wrap; margin-bottom:0.6rem; }
.explorer-kpi { background:#FFFFFF; border:1px solid rgba(46,139,87,0.08); padding:0.45rem 0.7rem; border-radius:999px; font-weight:600; color:var(--heading-color); box-shadow:0 6px 16px rgba(46,139,87,0.03); font-size:0.85rem; }

/* Slightly larger chart titles inside explorer for emphasis */
.chart-card .chart-title { font-size: 1.15rem !important; }

/* Streamlit widget sizing tweaks (best-effort selectors) */
.stSelectbox div[role="combobox"], .stMultiSelect div[role="combobox"], .stSlider div[role="slider"] { min-height:44px; border-radius:10px; }
.stRadio [role="radiogroup"] > div { gap: 0.6rem; }

/* Explorer-specific widget background overrides: make dropdowns/selectboxes white */
.control-card div[data-testid="stSelectbox"] > div,
.control-card div[data-testid="stMultiSelect"] > div,
.control-card div[data-testid="stSlider"] > div,
.control-card div[data-testid="stRadio"] > div {
    background: #FFFFFF !important;
    border-radius: 12px !important;
    padding: 8px 12px !important;
    border: 1px solid #2E8B57 !important;
    box-shadow: 0 6px 18px rgba(34,50,30,0.02) inset;
    color: #102a1d !important;
}

/* Improve select arrow / inner combobox contrast */
.control-card div[data-testid="stSelectbox"] svg,
.control-card div[data-testid="stMultiSelect"] svg {
    fill: #1f3a2d !important;
}

/* Focus state to emphasize green outline */
.control-card div[data-testid="stSelectbox"] > div:focus-within,
.control-card div[data-testid="stMultiSelect"] > div:focus-within,
.control-card div[data-testid="stSlider"] > div:focus-within {
    outline: 3px solid rgba(46,139,87,0.12) !important;
    box-shadow: 0 8px 22px rgba(46,139,87,0.06) inset !important;
}

/* Make radio options sit on white rounded surface */
.control-card div[data-testid="stRadio"] [role="radiogroup"] > div {
    background: transparent !important;
    gap: 0.6rem;
}

/* Arrow / chevron contrast */
div[data-testid="stSelectbox"] svg,
div[data-testid="stMultiSelect"] svg {
    fill: var(--heading-color) !important;
}

/* Hover: slightly darker green border */
div[data-testid="stSelectbox"]:hover,
div[data-testid="stMultiSelect"]:hover,
div[data-testid="stTextInput"]:hover {
    border-color: #276b45 !important;
}

/* Focus / open: soft green glow */
div[data-testid="stSelectbox"]:focus-within,
div[data-testid="stMultiSelect"]:focus-within,
div[data-testid="stSelectbox"][aria-expanded="true"],
div[data-testid="stMultiSelect"][aria-expanded="true"] {
    outline: 3px solid rgba(46,139,87,0.10) !important;
    box-shadow: 0 8px 26px rgba(46,139,87,0.06) !important;
    border-color: var(--heading-color) !important;
}

/* Main selectbox container */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #168A4A !important;
    border-radius: 14px !important;
    min-height: 52px !important;
    padding: 0 14px !important;
    box-shadow: none !important;
}

/* Remove inner gray dropdown background */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div > div,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div > div {
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Dropdown text */
div[data-testid="stSelectbox"] div[data-baseweb="select"] span,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] span {
    color: #102A1D !important;
    font-size: 15px !important;
    font-weight: 500 !important;
}

/* Dropdown arrow */
div[data-testid="stSelectbox"] div[data-baseweb="select"] svg,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] svg {
    color: #168A4A !important;
}

/* Hover and focus */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div:hover {
    border-color: #116B39 !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within,
div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div:focus-within {
    box-shadow: 0 0 0 3px rgba(22, 138, 74, 0.12) !important;
}


/* =========================
   COMPACT SLIDER
========================= */

div[data-testid="stSlider"] {
    background-color: #FFFFFF !important;
    border: 1px solid #168A4A !important;
    border-radius: 14px !important;
    padding: 0.15rem 0.65rem 0.1rem 0.65rem !important;
    min-height: 42px !important;
    box-sizing: border-box !important;
}

/* Move slider track upward */
div[data-testid="stSlider"] [data-baseweb="slider"] {
    margin-top: 13px !important;
    margin-bottom: -8px !important;
}

/* Slider label spacing */
div[data-testid="stSlider"] label {
    margin-bottom: -3px !important;
    padding-bottom: 0 !important;
}

/* Slider thumb/value */
div[data-testid="stSlider"] [role="slider"] {
    margin-top: 0 !important;
    width: 14px !important;
    height: 14px !important;
    min-width: 14px !important;
    min-height: 14px !important;
    border-radius: 999px !important;
    box-shadow: 0 0 0 2px rgba(255,255,255,0.95) !important;
}

/* Reduce the thumb track container so the smaller handle feels proportional */
div[data-testid="stSlider"] [data-baseweb="slider"] > div {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* Hide only the slider value text */
.stSlider [data-baseweb="slider"] div[role="slider"] div {
    opacity: 0 !important;
    transition: opacity 0.15s ease !important;
}

/* Show value only when hovering the circle */
.stSlider [data-baseweb="slider"] div[role="slider"]:hover div {
    opacity: 1 !important;
}

/* Keep the slider handle visible */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background-color: #ff4b4b !important;
}

/* =========================
   CONTROL LABELS
========================= */

div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label,
div[data-testid="stSlider"] label,
div[data-testid="stRadio"] label {
    color: #168A4A !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

/* Explorer buttons */
div[data-testid="stButton"] > button {
    border: 1.5px solid rgba(46,139,87,0.35) !important;
    border-radius: 16px !important;

    background: rgba(255,255,255,0.72) !important;
    backdrop-filter: blur(8px);

    color: #1F2937 !important;
    font-weight: 600 !important;

    transition:
        transform 0.18s ease,
        box-shadow 0.18s ease,
        border 0.18s ease,
        background 0.18s ease !important;

    box-shadow:
        0 4px 14px rgba(0,0,0,0.04) !important;
}

/* Same hover feel as chart containers */
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px) scale(1.015) !important;

    border: 1.5px solid rgba(46,139,87,0.55) !important;

    background: rgba(255,255,255,0.88) !important;

    box-shadow:
        0 10px 24px rgba(46,139,87,0.10),
        0 2px 8px rgba(0,0,0,0.05) !important;
}

/* Prevent clipping */
div[data-testid="stButton"] {
    overflow: visible !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA LOADING
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("AUTISM_GREENSPACE_DATASET.csv")
    df.columns = df.columns.str.strip()

    # Create readable district label
    df["District"] = "District " + df["DistrictID"].astype(str)

    # Rebuild road density group from one-hot columns if available
    high_col = "Road_Density_Group_High Road Density"
    low_col = "Road_Density_Group_Low Road Density"
    if high_col in df.columns and low_col in df.columns:
        df["Road_Density_Group"] = np.select(
            [df[high_col] == True, df[low_col] == True],
            ["High Road Density", "Low Road Density"],
            default="Medium Road Density"
        )
    elif "Road_Density_Group" not in df.columns:
        df["Road_Density_Group"] = pd.qcut(
            df["Roadensity"],
            q=3,
            labels=["Low Road Density", "Medium Road Density", "High Road Density"],
            duplicates="drop"
        ).astype(str)

    # Fill missing environmental values conservatively for dashboard display only
    for col in ["Prdcan100", "Green_Buffer_Score"]:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # Composite dashboard scores using min-max normalization
    def minmax(series):
        if series.max() == series.min():
            return series * 0
        return (series - series.min()) / (series.max() - series.min())

    df["Rate_norm"] = minmax(df["Rate"])
    df["Road_norm"] = minmax(df["Roadensity"])
    df["Pop_norm"] = minmax(df["Popden"])
    df["Green_norm"] = minmax(df["Green_Buffer_Score"])
    df["Income_norm"] = minmax(df["Income_median"])

    # Higher risk = high autism prevalence + high road/pop density + weaker green buffer
    df["Environmental_Risk_Score"] = (
        0.40 * df["Rate_norm"] +
        0.25 * df["Road_norm"] +
        0.20 * df["Pop_norm"] +
        0.15 * (1 - df["Green_norm"])
    ) * 100

    # Higher protection = stronger green buffer relative to road pressure
    df["Green_Protection_Efficiency"] = df["Green_Buffer_Score"] / (df["Roadensity"] + 0.01)

    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("CSV file not found. Please place AUTISM_GREENSPACE_DATASET.csv in the same folder as this app.py file.")
    st.stop()

st.markdown("""
<style>

/* Sidebar range sliders: clean white card, one-line label, centered two-thumb rail */
section[data-testid="stSidebar"] div[data-testid="stSlider"] {
    background: rgba(255,255,255,0.96) !important;
    border: 1px solid #D7E5DA !important;
    border-radius: 22px !important;
    padding: 12px 16px 14px 16px !important;
    min-height: 88px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] div[data-testid="stSlider"] label {
    display: block !important;
    margin-bottom: 8px !important;
    line-height: 1.15 !important;
    color: #2E8B57 !important;
    font-weight: 600 !important;
    text-align: left !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

section[data-testid="stSidebar"] div[data-testid="stSlider"] label p {
    margin: 0 !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] {
    display: block !important;
    height: auto !important;
    min-height: 0 !important;
    margin-top: 0 !important;
    padding-top: 0 !important;
}

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] > div {
    width: 100% !important;
}

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] label {
    display: flex !important;
    align-items: center !important;
    gap: 0.35rem !important;
    margin-bottom: 0.35rem !important;
    line-height: 1.15 !important;
    color: #2E8B57 !important;
    font-weight: 600 !important;
    text-align: left !important;
    white-space: nowrap !important;
}

section[data-testid="stSidebar"] div[data-testid="stSelectbox"] button {
    margin-top: 0 !important;
}

section[data-testid="stSidebar"] div[data-baseweb="slider"] {
    position: relative !important;
    width: 100% !important;
    height: 28px !important;
    margin-top: 6px !important;
    display: flex !important;
    align-items: center !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] div[data-baseweb="slider"] > div {
    width: 100% !important;
    height: 4px !important;
    border-radius: 999px !important;
    overflow: visible !important;
}

section[data-testid="stSidebar"] div[role="slider"] {
    position: absolute !important;
    top: 50% !important;
    margin-top: -9px !important;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 0 !important;
    z-index: 4 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    opacity: 1 !important;
    visibility: visible !important;
    width: 18px !important;
    height: 18px !important;
    min-width: 18px !important;
    min-height: 18px !important;
    border-radius: 50% !important;
    background: #ff4b4b !important;
    border: 2px solid #FFFFFF !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.12) !important;
}

section[data-testid="stSidebar"] div[role="slider"] > div {
    display: none !important;
}

section[data-testid="stSidebar"] div[data-testid="stMultiSelect"] {
    margin-bottom: 16px !important;
}

section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div {
    gap: 0.8rem !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.markdown("## 🌿 Dashboard Controls")
st.sidebar.caption("Use these filters to dynamically update KPIs, charts, tables, and insights.")

# =========================================================
# DISTRICT FILTER WITH WORKING SELECT / CLEAR
# =========================================================
all_districts = sorted(df["District"].unique())

if "district_multiselect" not in st.session_state:
    st.session_state["district_multiselect"] = all_districts

def select_all_districts():
    st.session_state["district_multiselect"] = all_districts

def clear_all_districts():
    st.session_state["district_multiselect"] = []

btn1, btn2 = st.sidebar.columns(2)

with btn1:
    st.button(
        "Select All",
        key="select_all_districts_btn",
        use_container_width=True,
        on_click=select_all_districts
    )

with btn2:
    st.button(
        "Clear All",
        key="clear_all_districts_btn",
        use_container_width=True,
        on_click=clear_all_districts
    )

selected_districts = st.sidebar.multiselect(
    "Select Districts",
    options=all_districts,
    key="district_multiselect"
)


# =========================================================
# ROAD DENSITY FILTER WITH WORKING SELECT / CLEAR
# =========================================================
all_road_groups = sorted(df["Road_Density_Group"].unique())

if "road_group_multiselect" not in st.session_state:
    st.session_state["road_group_multiselect"] = all_road_groups

def select_all_road_groups():
    st.session_state["road_group_multiselect"] = all_road_groups

def clear_all_road_groups():
    st.session_state["road_group_multiselect"] = []

road_btn1, road_btn2 = st.sidebar.columns(2)

with road_btn1:
    st.button(
        "Select All",
        key="select_all_road_groups_btn",
        use_container_width=True,
        on_click=select_all_road_groups
    )

with road_btn2:
    st.button(
        "Clear All",
        key="clear_all_road_groups_btn",
        use_container_width=True,
        on_click=clear_all_road_groups
    )

selected_road_groups = st.sidebar.multiselect(
    "Road Density Group",
    options=all_road_groups,
    key="road_group_multiselect"
)


# =========================================================
# RANGE FILTERS
# =========================================================
rate_range = st.sidebar.slider(
    "Autism Prevalence Range",
    float(df["Rate"].min()),
    float(df["Rate"].max()),
    (float(df["Rate"].min()), float(df["Rate"].max()))
)

green_range = st.sidebar.slider(
    "Green Buffer Score Range",
    float(df["Green_Buffer_Score"].min()),
    float(df["Green_Buffer_Score"].max()),
    (float(df["Green_Buffer_Score"].min()), float(df["Green_Buffer_Score"].max()))
)

road_range = st.sidebar.slider(
    "Road Density Range",
    float(df["Roadensity"].min()),
    float(df["Roadensity"].max()),
    (float(df["Roadensity"].min()), float(df["Roadensity"].max()))
)

pop_range = st.sidebar.slider(
    "Population Density Range",
    float(df["Popden"].min()),
    float(df["Popden"].max()),
    (float(df["Popden"].min()), float(df["Popden"].max()))
)

income_range = st.sidebar.slider(
    "Median Income Range",
    int(df["Income_median"].min()),
    int(df["Income_median"].max()),
    (int(df["Income_median"].min()), int(df["Income_median"].max()))
)

risk_cutoff = st.sidebar.slider(
    "High-Risk Cutoff Score",
    0,
    100,
    60
)

sort_option = st.sidebar.selectbox(
    "Chart Sorting",
    ["Highest Autism Prevalence", "Highest Environmental Risk", "Strongest Green Buffer", "High Traffic Areas"],
    help="Controls the ranking used in the main district bar chart.",
    label_visibility="visible"
)


# =========================================================
# FILTERED DATA
# =========================================================
filtered = df[
    (df["District"].isin(selected_districts)) &
    (df["Road_Density_Group"].isin(selected_road_groups)) &
    (df["Rate"].between(rate_range[0], rate_range[1])) &
    (df["Green_Buffer_Score"].between(green_range[0], green_range[1])) &
    (df["Roadensity"].between(road_range[0], road_range[1])) &
    (df["Popden"].between(pop_range[0], pop_range[1])) &
    (df["Income_median"].between(income_range[0], income_range[1]))
].copy()

if filtered.empty:
    st.warning("No records match the selected filters. Please adjust the sidebar controls.")
    st.stop()


# =========================================================
# COLOR CONSTANTS
# =========================================================
COLORS = {
    "green": "#2E8B57",
    "blue": "#5DADE2",
    "gold": "#F4B942",
    "coral": "#E85D75",
    "purple": "#8E44AD",
    "teal": "#48C9B0",
    "text": "#2C3E50",
    "muted": "#6B7280"
}

plotly_palette = [COLORS["green"], COLORS["blue"], COLORS["gold"], COLORS["coral"], COLORS["purple"], COLORS["teal"]]

common_layout = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color=COLORS["text"], family="Poppins"),
    margin=dict(l=20, r=20, t=60, b=30),
    title_font=dict(size=20, color=COLORS["green"], family="Poppins"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# Keep chart cards visually consistent across all rows and columns.
UNIFORM_CHART_CONTAINER_HEIGHT = 760
UNIFORM_CHART_FIGURE_HEIGHT = 430
UNIFORM_CHART_HEADER_MIN_HEIGHT = 72

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def kpi_card(label, value, note, color="#2E8B57"):
    return f"""
    <div class="kpi-card" style="border-top: 5px solid {color}; --kpi-value-color: {color};">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-note">{note}</div>
    </div>
    """.strip()

def render_kpi_grid(cards):
    html = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    :root {{
        --font-family-base: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        --fw-regular: 400;
        --fw-medium: 500;
        --fw-semibold: 600;
        --fw-bold: 700;
        --fw-extrabold: 800;
        --heading-color: #2E8B57;
        --muted-color: #6B7280;
    }}

    body, .kpi-grid, .kpi-card, .kpi-label, .kpi-value, .kpi-note {{
        font-family: var(--font-family-base);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2C3E50;
    }}

    .kpi-grid {{
        --kpi-gap: 0.95rem;
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: var(--kpi-gap);
        margin-top: 0.25rem;
        margin-bottom: 0px;
    }}
    @media (max-width: 1200px) {{
        .kpi-grid {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}
    }}
    @media (max-width: 640px) {{
        .kpi-grid {{
            grid-template-columns: 1fr;
        }}
    }}
    .kpi-card {{
        background: #ffffff;
        padding: 0.9rem 1rem;
        border-radius: 22px;
        border: 1px solid rgba(215,229,218,0.6);
        box-shadow: 0 8px 18px rgba(44, 62, 80, 0.06);
        min-height: 110px;
        position: relative;
        overflow: hidden;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
        will-change: transform;
    }}
    .kpi-card::after {{
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 22px;
        pointer-events: none;
        opacity: 0;
        transition: opacity 180ms ease;
        background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0));
    }}
    .kpi-card:hover {{
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 12px 26px rgba(44, 62, 80, 0.08);
        border-color: rgba(46, 139, 87, 0.28);
    }}
    .kpi-card:hover::after {{
        opacity: 1;
    }}
    .kpi-label {{
        color: var(--muted-color);
        font-size: 0.76rem;
        font-weight: var(--fw-semibold);
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}
    .kpi-value {{
        font-size: clamp(2.15rem, 2.6vw, 3.1rem);
        font-weight: var(--fw-extrabold);
        color: var(--kpi-value-color, #2C3E50);
        margin-top: 0.55rem;
        line-height: 1.02;
        letter-spacing: -0.02em;
    }}
    .kpi-note {{
        margin-top: 0.25rem;
        color: #4A4A4A;
        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 450;
        line-height: 1.65;
        margin-bottom: 0.75rem;
    }}
    </style>
    <div class="kpi-grid">
        {''.join(cards)}
    </div>
    """
    components.html(html, height=350, scrolling=False)

def render_kpi_summary_block(cards, summary_html, summary_gap_px=20, height=470):
    html = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    :root {{
        --font-family-base: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        --fw-regular: 400;
        --fw-medium: 500;
        --fw-semibold: 600;
        --fw-bold: 700;
        --fw-extrabold: 800;
        --heading-color: #2E8B57;
        --muted-color: #6B7280;
    }}

    body, .kpi-grid, .kpi-card, .kpi-label, .kpi-value, .kpi-note, .scenario-summary-box {{
        font-family: var(--font-family-base);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2C3E50;
    }}

    .kpi-summary-shell {{
        display: flex;
        flex-direction: column;
        width: 100%;
    }}

    .kpi-grid {{
        --kpi-gap: 0.95rem;
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: var(--kpi-gap);
        margin-top: 0.25rem;
        margin-bottom: 0px;
    }}

    @media (max-width: 1200px) {{
        .kpi-grid {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}
    }}

    @media (max-width: 640px) {{
        .kpi-grid {{
            grid-template-columns: 1fr;
        }}
    }}

    .kpi-card {{
        background: #ffffff;
        padding: 0.9rem 1rem;
        border-radius: 22px;
        border: 1px solid rgba(215,229,218,0.6);
        box-shadow: 0 8px 18px rgba(44, 62, 80, 0.06);
        min-height: 110px;
        position: relative;
        overflow: hidden;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
        will-change: transform;
    }}

    .kpi-card::after {{
        content: "";
        position: absolute;
        inset: 0;
        border-radius: 22px;
        pointer-events: none;
        opacity: 0;
        transition: opacity 180ms ease;
        background: linear-gradient(135deg, rgba(255,255,255,0.18), rgba(255,255,255,0));
    }}

    .kpi-card:hover {{
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 12px 26px rgba(44, 62, 80, 0.08);
        border-color: rgba(46, 139, 87, 0.28);
    }}

    .kpi-card:hover::after {{
        opacity: 1;
    }}

    .kpi-label {{
        color: var(--muted-color);
        font-size: 0.76rem;
        font-weight: var(--fw-semibold);
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}

    .kpi-value {{
        font-size: clamp(2.15rem, 2.6vw, 3.1rem);
        font-weight: var(--fw-extrabold);
        color: var(--kpi-value-color, #2C3E50);
        margin-top: 0.55rem;
        line-height: 1.02;
        letter-spacing: -0.02em;
    }}

    .kpi-note {{
        margin-top: 0.25rem;
        color: #4A4A4A;
        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 450;
        line-height: 1.65;
        margin-bottom: 0.75rem;
    }}

    .scenario-summary-box {{
        margin-top: {summary_gap_px}px;
        margin-bottom: 0;
        color: #4A4A4A;
        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 450;
        line-height: 1.65;
    }}
    </style>
    <div class="kpi-summary-shell">
        <div class="kpi-grid">
            {''.join(cards)}
        </div>
        <div class="scenario-summary-box">
            {summary_html}
        </div>
    </div>
    """
    components.html(html, height=height, scrolling=False)

def render_chart_card(title, subtitle, fig, insight_html, height=UNIFORM_CHART_CONTAINER_HEIGHT):
    fixed_height = UNIFORM_CHART_CONTAINER_HEIGHT
    fig.update_layout(
        title=None,
        # tighter plot margins to reduce empty vertical space
        margin=dict(l=60, r=20, t=10, b=30),
        font=dict(size=10, color=COLORS["text"], family="Poppins"),
        height=UNIFORM_CHART_FIGURE_HEIGHT,
    )
    fig.update_xaxes(automargin=True, tickfont=dict(size=9), title_font=dict(size=11), title_standoff=10)
    fig.update_yaxes(automargin=True, tickfont=dict(size=9), title_font=dict(size=11), title_standoff=10)
    figure_html = fig.to_html(full_html=False, include_plotlyjs="cdn", config={"displaylogo": False, "responsive": True, "scrollZoom": True})
    html = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

    :root {{
        --font-family-base: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
        --heading-color: #2E8B57;
        --muted-color: #6B7280;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        background: transparent;
        font-family: var(--font-family-base);
        color: #2C3E50;
    }}

    .chart-shell {{
        width: 100%;
        box-sizing: border-box;
        padding: 2px 8px 8px 8px;
        min-height: {UNIFORM_CHART_CONTAINER_HEIGHT - 4}px;
        display: flex;
        flex-direction: column;
    }}

    .chart-card {{
        width: calc(100% - 2px);
        box-sizing: border-box;
        background: linear-gradient(135deg, rgba(235, 247, 238, 0.98) 0%, rgba(255, 255, 255, 0.99) 48%, rgba(247, 241, 212, 0.95) 100%);
        border: 1px solid var(--heading-color) !important;
        border-radius: 28px;
        box-shadow: 0 10px 26px rgba(44, 62, 80, 0.08), inset 0 0 0 1px rgba(255, 255, 255, 0.72);
        padding: 1rem 1rem 0.9rem;
        /* match global card gutters to keep rows tight and equal */
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        overflow: hidden;
        transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
        will-change: transform;
        display: flex;
        flex-direction: column;
        flex: 1 1 auto;
    }}

    .chart-card:hover {{
        transform: translateY(-4px) scale(1.01);
        transform-origin: center center;
        box-shadow: 0 16px 34px rgba(44, 62, 80, 0.12), inset 0 0 0 1px rgba(255, 255, 255, 0.75);
        border-color: var(--heading-color) !important;
    }}

    .chart-header {{
        margin-bottom: 0.45rem;
        min-height: {UNIFORM_CHART_HEADER_MIN_HEIGHT}px;
    }}

    .chart-title {{
        margin: 0;
        color: #2F855A;
        font-family: 'Poppins', sans-serif;
        font-size: 30px;
        font-weight: 600;
        line-height: 1.3;
    }}

    .chart-subtitle {{
        margin-top: 0.3rem;
        color: #4A4A4A;
        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 450;
        line-height: 1.65;
        margin-bottom: 0.75rem;
    }}

    .chart-figure {{
        width: 100%;
        flex: 1 1 auto;
    }}

    .chart-insight {{
        margin-top: 0.35rem;
        padding: 0.3rem 0.55rem;
        border-radius: 14px;
        background: rgba(241, 250, 244, 0.78);
        border: 1px solid rgba(203, 235, 214, 0.85);
        color: #4A4A4A;
        font-family: "Inter", sans-serif;
        font-size: 0.95rem;
        font-weight: 450;
        line-height: 1.65;
        margin-bottom: 0.75rem;
    }}
    </style>
        <div class="chart-shell">
            <div class="chart-card">
                <div class="chart-header">
                        <div class="chart-title">{title}</div>
                        <div class="chart-subtitle">{subtitle}</div>
        </div>
        <div class="chart-figure">{figure_html}</div>
            </div>
            <div class="chart-insight">{insight_html}</div>
        </div>
    """
    components.html(html, height=760, scrolling=False)

def section_header(title, subtitle):
    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">{title}</div>
        <div class="section-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)

def insight(text, warning=False):
    css_class = "warning-box" if warning else "insight-box"
    st.markdown(f"<div class='{css_class}'>{text}</div>", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown('<div class="top-spacer"></div>', unsafe_allow_html=True)
try:
    banner_image = Image.open("proj1.png")
    st.image(banner_image, caption="", use_container_width=True)
    st.markdown('<div class="banner-bottom-spacer"></div>', unsafe_allow_html=True)
except FileNotFoundError:
    pass

# =========================================================
# DASHBOARD OVERVIEW
# =========================================================

st.markdown("""
<div style="
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.96) 0%,
        rgba(244,250,246,0.95) 100%
    );
    border: 1px solid rgba(46,139,87,0.20);
    border-radius: 28px;
    padding: 2.3rem 2.5rem;
    box-shadow: 0 12px 30px rgba(44,62,80,0.08);
    margin-bottom: 1.5rem;
">

<div style="
    font-size: 3rem;
    font-weight: 800;
    color: #2E8B57;
    margin-bottom: 1.4rem;
">
<div class="dashboard-title">🌿 Dashboard Overview</div>
 
<div style="
    font-family: 'Cormorant Garamond', serif;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: -0.5px;
    line-height: 1.15;
    color: #0c4a2b;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
    font-style: italic;
">
What if the environments where children grow up quietly shape patterns we rarely notice?
</div>

<div style="
    font-size: 1.2rem;
    color: #4A4A4A;
    line-height: 1.5;
    margin-bottom: 1.2rem;
    font-weight: 400;
">
Across cities and communities, some districts experience heavier traffic,
denser development, and fewer green spaces than others. This dashboard
explores how these environmental conditions vary across districts and
how they may relate to differences in childhood autism prevalence.
Rather than seeking to prove causation, the goal is to uncover meaningful
patterns that can support healthier, more sustainable urban planning decisions.
</div>

<div style="
    font-size: 1.2rem;
    color: #4A4A4A;
    line-height: 1.5;
    margin-bottom: 1.2rem;
    font-weight: 400;
">
Drawing from the study
<span style="color:#F59E0B;font-weight:700;">
Inverse Relationship Between Urban Green Space and Childhood Autism
in California Elementary School Districts
</span>
by
<span style="font-weight:400;">
Wu & Jackson (2017)
</span>,
this analysis examines environmental vulnerability, urban pressure,
and the potential buffering role of green spaces in shaping community
environments.
</div>

<div class="badge-row">
        <span class="badge">SDG 3: Good Health & Well-being</span>
        <span class="badge">SDG 11: Sustainable Cities</span>
        <span class="badge">Environmental Health Analytics</span>
    </div>
</div>

</div>
""", unsafe_allow_html=True)



# =========================================================
# KPI SECTION
# =========================================================
median_rate = filtered["Rate"].median()
median_green = filtered["Green_Buffer_Score"].median()
median_road = filtered["Roadensity"].median()
median_pop = filtered["Popden"].median()
median_income = filtered["Income_median"].median()
median_risk = filtered["Environmental_Risk_Score"].median()
median_eff = filtered["Green_Protection_Efficiency"].median()
high_traffic_count = (filtered["Road_Density_Group"] == "High Road Density").sum()
autism_threshold = filtered["Rate"].quantile(0.75)
high_autism_risk_count = (filtered["Rate"] >= autism_threshold).sum()

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<div class='dashboard-title'>📌 Dynamic Key Performance Indicators</div>", unsafe_allow_html=True)
st.markdown("""
<div style="
    color: #4A4A4A;
    font-size: 1rem;
    font-weight: 500;
    line-height: 1.55;
    margin-bottom: 0.75rem;
">
These key indicators provide a high-level summary of environmental, socioeconomic, and urban conditions across districts, using robust statistical measures to support accurate and meaningful interpretation.
</div>
""", unsafe_allow_html=True)

render_kpi_grid([
    kpi_card("Autism Prevalence", f"{median_rate:.2f}", "Median autism prevalence across the selected districts.", COLORS["coral"]),
    kpi_card("Urban Green Coverage", f"{median_green:.2f}", "Median green coverage across the selected districts.", COLORS["green"]),
    kpi_card("Road Density Level", f"{median_road:.3f}", "Median road density across the selected districts.", "#D97706"),
    kpi_card("Population Density", f"{median_pop:,.1f}", "Median urban crowding among selected districts.", COLORS["blue"]),
    kpi_card("Household Income Level", f"{median_income:,.0f}", "Median household income across the selected districts.", "#3B82F6"),
    kpi_card("High Traffic Areas", f"{high_traffic_count}", "Districts classified as High Road Density.", "#F59E0B"),
    kpi_card("Environmental Protection Score", f"{median_eff:.2f}", "Computed index from green buffering and transportation exposure.", COLORS["green"]),
    kpi_card("High Autism Risk Areas", f"{high_autism_risk_count}", f">= 75th percentile prevalence threshold ({autism_threshold:.2f}).", COLORS["coral"]),
])

insight(f"<b>Summary:</b> Based on the current filters, <b>{len(filtered)}</b> district records are being analyzed. Median autism prevalence is <b>{median_rate:.2f}</b>, median road density is <b>{median_road:.3f}</b>, and median household income is <b>{median_income:,.0f}</b>. There are <b>{high_traffic_count}</b> high-traffic districts and <b>{high_autism_risk_count}</b> high-autism-risk districts under the current filter set.")

# =========================================================
# CENTER-START DOUBLE-SIDED CARD CAROUSEL
# =========================================================
components.html("""
<style>
body {
    margin: 0;
    background: transparent;
    font-family: Poppins, sans-serif;
}

.carousel-section {
    width: 100%;
    padding: 10px 18px 35px;
    text-align: left;
}

.carousel-title {
    font-family: 'Poppins', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    font-size: 2.4rem;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.02em;
    color: #2F855A;
    text-align: left;
    margin: 2rem 0 0.4rem 0;
}

.carousel-subtitle {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 1rem;
    font-weight: 450;
    line-height: 1.65;
    text-align: left;
    margin-bottom: 0.75rem;
}

.card-window {
    width: 100%;
    height: 470px;
    overflow: visible;
    position: relative;
    padding-top: 20px;
    padding-bottom: 30px;
}

.card-track {
    display: flex;
    gap: 22px;
    position: absolute;
    left: 50%;
    top: 20px;
    transition: transform 0.75s cubic-bezier(0.22, 1, 0.36, 1);
}

.flip-card {
    min-width: 300px;
    height: 390px;
    perspective: 1400px;
}

.flip-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.75s ease;
    transform-style: preserve-3d;
}

.flip-card:hover .flip-inner {
    transform: rotateY(180deg);
}

.flip-front,
.flip-back {
    position: absolute;
    inset: 0;
    border-radius: 18px;
    padding: 26px;
    box-sizing: border-box;
    color: white;
    box-shadow: 0 14px 32px rgba(44, 62, 80, 0.16);
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
}

.flip-front {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.flip-back {
    transform: rotateY(180deg);
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: auto;
}

.card-title {
    font-size: 1.5rem;
    font-weight: 800;
    line-height: 1.15;
}

.card-type {
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.3;
}

.card-line {
    width: 100%;
    height: 1px;
    background: rgba(255,255,255,0.65);
    margin: 0.9rem 0;
}

.card-desc {
    font-size: 0.74rem;
    line-height: 1.45;
    color: rgba(255,255,255,0.94);
}

.nav-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    z-index: 999;

    width: 48px;
    height: 48px;

    border-radius: 999px;
    border: 1.5px solid rgba(46,139,87,0.18);

    background: rgba(255,255,255,0.96);
    color: #2E8B57;

    font-size: 28px;
    line-height: 1;

    cursor: pointer;

    box-shadow: 0 10px 24px rgba(44,62,80,0.12);

    transition: all 0.25s ease;
}

.nav-btn:hover {
    background: #2E8B57;
    color: white;
    transform: translateY(-50%) scale(1.08);
}

.nav-btn:disabled {
    opacity: 0.30;
    cursor: not-allowed;
    transform: translateY(-50%);
}

.left-btn {
    left: 18px;
}

.right-btn {
    right: 18px;
}
</style>

<div class="carousel-section">
    <div class="carousel-title">📚 Understanding the Key Indicators</div>
    <div class="carousel-subtitle">
        Each indicator below represents a component of the environmental vulnerability framework used in this dashboard. Hover over each card to understand how the variable contributes to identifying urban stress, green buffering, and spatial health patterns.
    </div>

    <div class="card-window">

        <button class="nav-btn left-btn" id="leftBtn" onclick="moveCarousel(-1)">←</button>

        <button class="nav-btn right-btn" id="rightBtn" onclick="moveCarousel(1)">→</button>

        <div class="card-track" id="cardTrack"></div>

    </div>
</div>

<script>
const cards = [
    {
        title: "Autism Prevalence Rate",
        type: "Outcome Variable",
        definition: "Autism prevalence rate serves as the primary response variable to map spatial variations in neurodevelopmental outcomes against community-level characteristics. Rather than implying direct causation, epidemiological frameworks utilize localized prevalence rates to identify statistical patterns and geographical clusters (Hertz-Picciotto et al., 2006). This allows researchers to evaluate how shifting neighborhood-level attributes correlate with observed diagnostic frequencies across districts.",
        color: "#E85D75"
    },
    {
        title: "Green Space Coverage",
        type: "Environmental Predictor",
        definition: "Green space exposure is included as an environmental predictor based on literature suggesting potential correlative benefits of natural environments on child development. Cross-sectional cohorts look at vegetation indices to explore whether proximity to natural spaces correlates with lower environmental stress or altered neurodevelopmental patterns (Liu, 2025).",
        color: "#2E8B57"
    },
    {
        title: "Road Density",
        type: "Urban Stress Predictor",
        definition: "Road density is utilized as a proxy for traffic exposure and urban infrastructure intensity to examine potential environmental associations. Extensive literature identifies traffic corridors as sources of ambient stressors, which are explored as potential statistical predictors of spatial health variations.",
        color: "#D97706"
    },
    {
        title: "Population Density",
        type: "Urbanization Predictor",
        definition: "Population density is selected to control for urban crowding and concentrated human activity within the statistical model. Including this predictor allows the study to account for structural urbanization patterns when analyzing regional associations.",
        color: "#5DADE2"
    },
    {
        title: "Median Household Income",
        type: "Socioeconomic Control Variable",
        definition: "Median household income serves as a critical socioeconomic control variable to isolate non-environmental confounding factors. Controlling for this variable ensures that financial gradients do not skew the observed associations.",
        color: "#3B82F6"
    },
    {
        title: "Green Buffer Score",
        type: "Derived Environmental Predictor",
        definition: "The Green Buffer Score is derived by combining green space coverage and road density to evaluate the hypothetical interaction between environmental assets and infrastructure stressors.",
        color: "#48C9B0"
    }
];

let current = Math.floor(cards.length / 2);
const cardWidth = 322;

function renderCards() {
    const track = document.getElementById("cardTrack");
    track.innerHTML = "";

    cards.forEach(card => {
        const div = document.createElement("div");
        div.className = "flip-card";

        div.innerHTML = `
            <div class="flip-inner">
                <div class="flip-front" style="background:${card.color};">
                    <div class="card-title">${card.title}</div>
                </div>

                <div class="flip-back" style="background:${card.color};">
                    <div>
                        <div class="card-type">Type of Variable:<br>${card.type}</div>
                        <div class="card-line"></div>
                    </div>

                    <div class="card-desc">
                        <b>Variable Rationale:</b><br>${card.definition}
                    </div>
                </div>
            </div>
        `;

        track.appendChild(div);
    });

    updatePosition();
}

function updatePosition() {
    const moveX = -(current * cardWidth) - 150;
    document.getElementById("cardTrack").style.transform = `translateX(${moveX}px)`;

    document.getElementById("leftBtn").disabled = current === 0;
    document.getElementById("rightBtn").disabled = current === cards.length - 1;
}

function moveCarousel(direction) {
    current = current + direction;

    if (current < 0) current = 0;
    if (current >= cards.length) current = cards.length - 1;

    updatePosition();
}

renderCards();
</script>
""", height=580, scrolling=False)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# CHARTS SECTION - 8 CORE GRAPHS
# =========================================================
st.markdown("<div class='section-title'>📊 Main Environmental Health Visualizations</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-subtitle'>Explore district-level patterns across environmental, socioeconomic, and urban indicators to better understand variations in autism prevalence and community vulnerability.</div>",
    unsafe_allow_html=True,
)

numeric_cols = [
    "Rate", "Prdcan100", "Roadensity", "Popden", "Income_median",
    "Green_Buffer_Score", "Environmental_Risk_Score", "Green_Protection_Efficiency"
]

def grid_color(score, mode):
    """Return color and label for the population grid."""
    if mode == "Green Protection":
        if score >= risk_cutoff:
            return COLORS["green"], "Strong green protection"
        elif score >= 45:
            return COLORS["gold"], "Moderate green protection"
        return COLORS["coral"], "Weak green protection"
    else:
        if score >= risk_cutoff:
            return COLORS["coral"], "High risk"
        elif score >= 45:
            return COLORS["gold"], "Moderate risk"
        return COLORS["green"], "Lower risk"

def make_population_grid(data, mode):
    grid_df = data.copy()

    if mode == "Autism Risk":
        grid_df["Grid_Score"] = grid_df["Rate_norm"] * 100
        score_label = "Autism risk score"
        explanation = "Each icon represents one district record. Color is based on autism prevalence intensity."
    elif mode == "Green Protection":
        grid_df["Grid_Score"] = grid_df["Green_norm"] * 100
        score_label = "Green protection score"
        explanation = "Each icon represents one district record. Green icons indicate stronger environmental buffering, while coral icons show weaker green protection."
    elif mode == "Urban Stress":
        grid_df["Grid_Score"] = ((0.55 * grid_df["Road_norm"]) + (0.45 * grid_df["Pop_norm"])) * 100
        score_label = "Urban stress score"
        explanation = "Each icon represents one district record. Color is based on road density and population density pressure."
    else:
        grid_df["Grid_Score"] = grid_df["Environmental_Risk_Score"]
        score_label = "Environmental risk score"
        explanation = "Each icon represents one district record. Color is based on combined autism prevalence, road density, population density, and weak green buffering."

    grid_df = grid_df.sort_values("Grid_Score", ascending=False)

    icons_html = ""
    for _, row in grid_df.iterrows():
        color, label = grid_color(row["Grid_Score"], mode)
        tooltip = (
            f"{row['District']} | {score_label}: {row['Grid_Score']:.1f} | "
            f"Autism Prevalence: {row['Rate']:.2f} | Road Density: {row['Roadensity']:.3f} | "
            f"Green Buffer: {row['Green_Buffer_Score']:.2f} | {label}"
        )
        icons_html += f"<span class='person-icon' style='--person-color:{color};' title='{tooltip}'></span>"

    high_count = sum(grid_color(score, mode)[1] in ["High risk", "Weak green protection"] for score in grid_df["Grid_Score"])
    mid_count = sum(grid_color(score, mode)[1] in ["Moderate risk", "Moderate green protection"] for score in grid_df["Grid_Score"])
    low_count = len(grid_df) - high_count - mid_count

    html = f"""
    <div class="risk-grid-wrap">
        <div class="section-title">6. Environmental Risk Population Grid</div>
        <div class="section-subtitle">
            Gestalt-inspired figure/ground view. {explanation}
            Hover over each figure to view district details.
        </div>
        <span class="metric-pill">Mode: {mode}</span>
        <span class="metric-pill">Threshold: {risk_cutoff}</span>
        <span class="metric-pill">Records: {len(grid_df)}</span>
        <div class="risk-grid">{icons_html}</div>
        <div class="grid-legend">
            <span><span class="legend-dot" style="background:{COLORS['green']};"></span>Low risk / Strong protection: {low_count}</span>
            <span><span class="legend-dot" style="background:{COLORS['gold']};"></span>Moderate: {mid_count}</span>
            <span><span class="legend-dot" style="background:{COLORS['coral']};"></span>High risk / Weak protection: {high_count}</span>
        </div>
    </div>
    """
    return html, high_count, mid_count, low_count

# GRAPH 1 + GRAPH 2
col1, col2 = st.columns(2)

with col1:
    if sort_option == "Highest Environmental Risk":
        sort_col = "Environmental_Risk_Score"
    elif sort_option == "Strongest Green Buffer":
        sort_col = "Green_Buffer_Score"
    elif sort_option == "High Traffic Areas":
        sort_col = "Roadensity"
    else:
        sort_col = "Rate"

    top_rate = (
        filtered.groupby("District", as_index=False)
        .agg({
            "Rate": "median",
            "Environmental_Risk_Score": "median",
            "Green_Buffer_Score": "median",
            "Roadensity": "median"
        })
        .sort_values(sort_col, ascending=False)
        .head(20)
    )

    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=top_rate["Rate"],
        y=top_rate["District"],
        orientation="h",
        marker_color="rgba(200,200,200,0.18)",
        hoverinfo="skip",
        showlegend=False
    ))
    fig1.add_trace(go.Scatter(
        x=top_rate["Rate"],
        y=top_rate["District"],
        mode="markers",
        marker=dict(
            size=18,
            color=top_rate["Environmental_Risk_Score"],
            colorscale=["#DFF4E6", "#F4B942", "#E85D75"],
            showscale=True,
            colorbar=dict(title="Risk")
        ),
        hovertemplate="<b>%{y}</b><br>Rate: %{x:.2f}<br>Risk Score: %{marker.color:.1f}<extra></extra>"
    ))
    fig1.update_layout(
        xaxis_title="Autism Prevalence",
        yaxis_title="District",
        **common_layout,
        yaxis=dict(autorange="reversed")
    )
    render_chart_card(
        "Autism by District",
        "Lollipop ranking of district-level prevalence, with environmental risk encoded by color.",
        fig1,
        "<b>Insight:</b> Districts positioned farther to the right with darker colors indicate areas with both higher autism prevalence and higher environmental risk.",
        height=620,
    )

with col2:
    density_df = filtered[["Prdcan100", "Rate"]].replace([np.inf, -np.inf], np.nan).dropna()

    # Log transform reduces extreme stretching while keeping values readable
    density_df["Green_log"] = np.log1p(density_df["Prdcan100"])
    density_df["Rate_log"] = np.log1p(density_df["Rate"])

    fig2 = px.density_heatmap(
        density_df,
        x="Green_log",
        y="Rate_log",
        nbinsx=70,
        nbinsy=70,
        color_continuous_scale=[
            "#F8FFFA",
            "#B7E4C7",
            "#52B788",
            "#F4B942",
            "#E85D75",
            "#B00020"
        ],
        labels={
            "Green_log": "Green Space Exposure",
            "Rate_log": "Autism Prevalence"
        }
    )

    fig2.update_traces(
        opacity=0.95,
        colorbar=dict(title="District Count", thickness=14)
    )

    fig2.add_trace(go.Scatter(
        x=density_df["Green_log"],
        y=density_df["Rate_log"],
        mode="markers",
        marker=dict(
            size=4,
            color="rgba(31,41,55,0.28)"
        ),
        hovertemplate=(
            "Green Space: %{customdata[0]:.2f}<br>"
            "Autism Prevalence: %{customdata[1]:.2f}<extra></extra>"
        ),
        customdata=density_df[["Prdcan100", "Rate"]],
        showlegend=False
    ))

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.35)",
        font=dict(color=COLORS["text"], family="Poppins"),
        margin=dict(l=60, r=20, t=10, b=50),
        xaxis=dict(
            title="Green Space Exposure — compressed scale",
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        ),
        yaxis=dict(
            title="Autism Prevalence — compressed scale",
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        )
    )

    render_chart_card(
        "Green Space & Autism",
        "Log-compressed density map showing where green exposure and autism prevalence records are concentrated.",
        fig2,
        "<b>Insight:</b> Higher-density color clusters indicate where green space exposure and autism prevalence records are most concentrated across districts.",
        height=620,
    )

# GRAPH 3 + GRAPH 4
col3, col4 = st.columns(2)

with col3:
    order = sorted(filtered["Road_Density_Group"].dropna().unique().tolist())

    fig3 = px.violin(
        filtered,
        x="Rate",
        y="Road_Density_Group",
        color="Road_Density_Group",
        orientation="h",
        points=False,
        hover_data=["District", "Rate"],
        category_orders={"Road_Density_Group": order},
        color_discrete_sequence=plotly_palette,
        title=None
    )

    fig3.update_traces(side="positive", width=0.8)
    fig3.update_layout(
        **common_layout,
        yaxis=dict(autorange="reversed"),
        showlegend=False
    )

    render_chart_card(
        "Traffic & Autism",
        "Ridgeline-style distribution of autism prevalence across road-density groups.",
        fig3,
        "<b>Insight:</b> Wider and more extended distributions indicate that autism prevalence patterns vary more across districts with different levels of road density exposure.",
        height=620,
    )

with col4:
    contour_df = filtered[["Popden", "Rate"]].replace([np.inf, -np.inf], np.nan).dropna()
    contour_df["Popden_log"] = np.log1p(contour_df["Popden"])

    x_min, x_max = contour_df["Popden_log"].quantile([0.01, 0.99])
    y_min, y_max = contour_df["Rate"].quantile([0.01, 0.99])

    x_pad = (x_max - x_min) * 0.08 if x_max != x_min else 0.1
    y_pad = (y_max - y_min) * 0.08 if y_max != y_min else 0.1

    fig4 = px.density_contour(
        contour_df,
        x="Popden_log",
        y="Rate",
        nbinsx=70,
        nbinsy=70,
        labels={
            "Popden_log": "Population Density — compressed scale",
            "Rate": "Autism Prevalence"
        }
    )

    fig4.update_traces(
        contours_coloring="fill",
        contours_showlabels=False,
        ncontours=60,
        line_width=0,
        colorscale=[
            [0.00, "#F8FFFA"],
            [0.20, "#B7E4C7"],
            [0.40, "#52B788"],
            [0.65, "#F4B942"],
            [0.85, "#E85D75"],
            [1.00, "#B00020"]
        ],
        opacity=0.92
    )

    fig4.add_trace(go.Scatter(
        x=contour_df["Popden_log"],
        y=contour_df["Rate"],
        mode="markers",
        marker=dict(
            size=3,
            color="rgba(31,41,55,0.22)",
            line=dict(width=0)
        ),
        customdata=contour_df[["Popden", "Rate"]],
        hovertemplate=(
            "Population Density: %{customdata[0]:,.2f}<br>"
            "Autism Prevalence: %{customdata[1]:.2f}<extra></extra>"
        ),
        showlegend=False
    ))

    fig4.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.35)",
        font=dict(color=COLORS["text"], family="Poppins"),
        margin=dict(l=60, r=20, t=10, b=50),
        coloraxis_colorbar=dict(
            title="Density",
            thickness=14,
            outlinewidth=0
        ),
        xaxis=dict(
            title="Population Density — compressed scale",
            range=[x_min - x_pad, x_max + x_pad],
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        ),
        yaxis=dict(
            title="Autism Prevalence",
            range=[y_min - y_pad, y_max + y_pad],
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        )
    )

    render_chart_card(
        "Population Density & Autism",
        "Compressed contour density view of crowding patterns against autism prevalence.",
        fig4,
        "<b>Insight:</b> Brighter and denser contour clusters indicate where higher population density and autism prevalence records are more concentrated across districts.",
        height=620,
    )
# GRAPH 5 + GRAPH 6
col5, col6 = st.columns(2)

with col5:
    temp = filtered.copy()
    try:
        temp["Income_bin"] = pd.qcut(
            temp["Income_median"].rank(method="first"),
            q=4,
            labels=["Low", "Lower-Mid", "Upper-Mid", "High"]
        )
    except ValueError:
        temp["Income_bin"] = "Selected Districts"

    fig5 = px.violin(
        temp,
        x="Income_bin",
        y="Rate",
        color="Income_bin",
        box=True,
        points="all",
        color_discrete_sequence=plotly_palette,
        title=None,
        labels={"Income_bin": "Income Group", "Rate": "Autism Prevalence"}
    )
    fig5.update_layout(**common_layout, showlegend=False)
    render_chart_card(
        "Income & Autism",
        "Distribution of autism prevalence across income strata.",
        fig5,
        "<b>Insight:</b> Differences in the spread and concentration of each income group indicate how autism prevalence patterns vary across socioeconomic levels.",
        height=620,
    )

with col6:
    # Environmental Vulnerability Zones — Risk Quadrant Bubble Map
    x = filtered["Roadensity"]
    y = filtered["Green_Buffer_Score"]
    x_med = x.median()
    y_med = y.median()

    # size scaling for bubbles
    max_rate = filtered["Rate"].max() if not filtered["Rate"].isnull().all() else 1
    sizeref = 2.0 * max_rate / (60.0 ** 2)

    fig6 = px.scatter(
        filtered,
        x="Roadensity",
        y="Green_Buffer_Score",
        size="Rate",
        color="Environmental_Risk_Score",
        color_continuous_scale=["#EAF7EF", "#F4B942", "#E85D75"],
        hover_name="District",
        hover_data={
            "Rate": ":.3f",
            "Roadensity": ":.3f",
            "Green_Buffer_Score": ":.3f",
            "Environmental_Risk_Score": ":.2f",
        },
        title=None,
        labels={"Roadensity": "Road Density", "Green_Buffer_Score": "Green Buffer Score", "Environmental_Risk_Score": "Environmental Risk"},
        size_max=60,
    )

    fig6.update_traces(marker=dict(opacity=0.85, line=dict(width=0.6, color="rgba(0,0,0,0.12)")), selector=dict(mode="markers"))
    fig6.update_layout(**common_layout)

    # median reference lines to form quadrants
    fig6.add_vline(x=x_med, line_dash="dash", line_color="#6B7280")
    fig6.add_hline(y=y_med, line_dash="dash", line_color="#6B7280")

    # quadrant labels (positions chosen relative to data ranges)
    x_max, x_min = x.max(), x.min()
    y_max, y_min = y.max(), y.min()
    x_span = x_max - x_min if x_max != x_min else 1
    y_span = y_max - y_min if y_max != y_min else 1

    fig6.add_annotation(x=x_min + 0.75 * x_span, y=y_min + 0.75 * y_span, text="Buffered Urban Zones", showarrow=False, font=dict(color="#2E8B57", size=9))
    fig6.add_annotation(x=x_min + 0.75 * x_span, y=y_min + 0.25 * y_span, text="Critical Risk Zones", showarrow=False, font=dict(color="#E85D75", size=9))
    fig6.add_annotation(x=x_min + 0.25 * x_span, y=y_min + 0.75 * y_span, text="Protected Zones", showarrow=False, font=dict(color="#2E8B57", size=9))
    fig6.add_annotation(x=x_min + 0.25 * x_span, y=y_min + 0.25 * y_span, text="Emerging Risk Zones", showarrow=False, font=dict(color="#F4B942", size=9))

    # improve colorbar and marker sizing
    fig6.update_traces(marker=dict(sizemode="area", sizeref=sizeref))

    render_chart_card(
        "Environmental Vulnerability Zones",
        "Risk quadrant bubble map using road density, green buffering, prevalence, and environmental risk.",
        fig6,
        "<b>Insight:</b> Larger and darker bubbles located in the lower-right risk zones indicate districts experiencing higher road exposure, weaker green buffering, and greater overall environmental vulnerability.",
        height=620,
    )

# GRAPH 7 + GRAPH 8
col7, col8 = st.columns(2)

with col7:
    fig7 = px.violin(
        filtered,
        x="Road_Density_Group",
        y="Rate",
        color="Road_Density_Group",
        box=True,
        points="all",
        hover_data=["District"],
        color_discrete_sequence=plotly_palette,
        title=None
    )

    fig7.update_traces(meanline_visible=True)
    fig7.update_layout(**common_layout, showlegend=False)

    render_chart_card(
        "Autism by Traffic Level",
        "Raincloud-style comparison of prevalence across road-density groups.",
        fig7,
        "<b>Insight:</b> Wider distributions and higher outlier points indicate that autism prevalence varies more across districts with different levels of traffic exposure.",
        height=620,
    )

with col8:
    matrix_df = filtered[["Roadensity", "Green_Buffer_Score"]].replace([np.inf, -np.inf], np.nan).dropna()

    matrix_df["Roadensity_log"] = np.log1p(matrix_df["Roadensity"])

    x_med = matrix_df["Roadensity_log"].median()
    y_med = matrix_df["Green_Buffer_Score"].median()

    x_min, x_max = matrix_df["Roadensity_log"].quantile([0.01, 0.99])
    y_min, y_max = matrix_df["Green_Buffer_Score"].quantile([0.01, 0.99])

    x_pad = (x_max - x_min) * 0.08 if x_max != x_min else 0.1
    y_pad = (y_max - y_min) * 0.08 if y_max != y_min else 0.1

    fig8 = px.density_heatmap(
        matrix_df,
        x="Roadensity_log",
        y="Green_Buffer_Score",
        nbinsx=85,
        nbinsy=85,
        color_continuous_scale=[
            "#F8FFFA",
            "#B7E4C7",
            "#52B788",
            "#F4B942",
            "#E85D75",
            "#B00020"
        ],
        labels={
            "Roadensity_log": "Road Density — compressed scale",
            "Green_Buffer_Score": "Green Buffer Score"
        }
    )

    fig8.update_traces(
        opacity=0.95,
        zsmooth="best"
    )

    fig8.add_vline(
        x=x_med,
        line_dash="dot",
        line_color="rgba(80,80,80,0.55)",
        line_width=2
    )

    fig8.add_hline(
        y=y_med,
        line_dash="dot",
        line_color="rgba(80,80,80,0.55)",
        line_width=2
    )

    fig8.add_annotation(
    x=x_min + (x_max - x_min) * 0.18,
    y=y_max - (y_max - y_min) * 0.12,
    text="Protected Zones",
    showarrow=False,
    font=dict(size=9, color="#2E8B57")
)

    fig8.add_annotation(
    x=x_max - (x_max - x_min) * 0.18,
    y=y_max - (y_max - y_min) * 0.12,
    text="Buffered Urban Zones",
    showarrow=False,
    font=dict(size=9, color="#2E8B57")
)

    fig8.add_annotation(
    x=x_min + (x_max - x_min) * 0.18,
    y=y_min + (y_max - y_min) * 0.12,
    text="Emerging Risk Zones",
    showarrow=False,
    font=dict(size=9, color="#D97706")
)

    fig8.add_annotation(
    x=x_max - (x_max - x_min) * 0.18,
    y=y_min + (y_max - y_min) * 0.12,
    text="Critical Risk Zones",
    showarrow=False,
    font=dict(size=9, color="#E85D75")
)

    fig8.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.35)",
        font=dict(color=COLORS["text"], family="Poppins"),
        margin=dict(l=60, r=20, t=10, b=50),
        coloraxis_colorbar=dict(
            title="Density",
            thickness=14,
            outlinewidth=0
        ),
        xaxis=dict(
            title="Road Density — compressed scale",
            range=[x_min - x_pad, x_max + x_pad],
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        ),
        yaxis=dict(
            title="Green Buffer Score",
            range=[y_min - y_pad, y_max + y_pad],
            zeroline=False,
            showgrid=True,
            gridcolor="rgba(46,139,87,0.10)"
        )
    )

    render_chart_card(
        "Environmental Risk Matrix",
        "Quadrant heat matrix separating protected and high-risk exposure zones.",
        fig8,
        "<b>Insight:</b> Areas with warmer colors indicate where districts are most concentrated within the environmental risk quadrants, helping identify clusters of protected and higher-risk exposure zones.",
        height=620,
    )


# GRAPH 9
try:
    fig9 = px.treemap(
        filtered,
        path=["Road_Density_Group", "District"],
        values="Rate",
        color="Environmental_Risk_Score",
        color_continuous_scale=[
            "#EAF7EF",
            "#F4B942",
            "#E85D75"
        ],
        hover_data={
            "Rate": ":.2f",
            "Environmental_Risk_Score": ":.2f",
            "Green_Buffer_Score": ":.2f",
            "Roadensity": ":.3f",
        },
        title=None,
    )

    layout_copy = dict(common_layout)
    layout_copy["margin"] = dict(t=40, l=0, r=0, b=0)

    fig9.update_layout(**layout_copy)
    fig9.data[0].textinfo = "label+value+percent parent"

    render_chart_card(
        "Environmental Risk Treemap",
        "District contribution to risk and prevalence, grouped by road-density category.",
        fig9,
        "<b>Insight:</b> Larger and darker blocks indicate that certain districts contribute more heavily to overall environmental risk within their respective road-density groups.",
        height=UNIFORM_CHART_CONTAINER_HEIGHT,
    )

except Exception as e:
    st.error(f"Failed to render treemap: {e}")



# Modern Explorer-only CSS
st.markdown("""
<style>
/* =========================
   MODERN DISTRICT EXPLORER
========================= */
.explorer-hero {
    background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(241,250,244,0.86));
    border: 1px solid rgba(46,139,87,0.16);
    border-radius: 26px;
    padding: 1.15rem 1.25rem;
    box-shadow: 0 12px 28px rgba(44,62,80,0.06);
    margin-bottom: 0.95rem;
}
.explorer-hero-title {
    text-align: left;
}
.explorer-hero-subtitle {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 1rem;
    font-weight: 450;
    line-height: 1.65;
    margin: 10px 0 0.75rem 0;
}
.explorer-side-shell {
    background: rgba(255,255,255,0.70);
    border: 1px solid rgba(46,139,87,0.18);
    border-radius: 24px;
    padding: 1rem 1rem 0.9rem 1rem;
    box-shadow: 0 10px 24px rgba(44,62,80,0.05);
    margin-bottom: 0.85rem;
}
.explorer-side-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.7rem;
    margin-bottom: 0.65rem;
}
.explorer-side-title {
    color: #2E8B57;
    font-size: 1.2rem;
    font-weight: 800;
}
.explorer-side-chip {
    color: #2E8B57;
    background: rgba(223,244,230,0.85);
    border: 1px solid rgba(46,139,87,0.16);
    border-radius: 999px;
    padding: 0.28rem 0.55rem;
    font-size: 0.68rem;
    font-weight: 700;
}
.explorer-control-label {
    color: #2E8B57;
    font-size: 0.78rem;
    font-weight: 1000;
    margin: 0.85rem 0 0.35rem 0;
    letter-spacing: 0.01em;
}
.explorer-tip {
    margin-top: 0.9rem;
    background: linear-gradient(135deg, rgba(241,250,244,0.95), rgba(255,255,255,0.88));
    border: 1px solid rgba(203,235,214,0.95);
    border-radius: 16px;
    padding: 0.75rem 0.85rem;
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}
.explorer-table-shell {
    margin-top: 1rem;
    margin-bottom: 0.25rem;
}
.explorer-kpis {
    display: flex;
    gap: 0.55rem;
    flex-wrap: wrap;
    margin: 0.15rem 0 0.8rem 0;
}
.explorer-kpi {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(46,139,87,0.14);
    padding: 0.45rem 0.7rem;
    border-radius: 999px;
    font-weight: 800;
    color: #2E8B57;
    box-shadow: 0 6px 16px rgba(46,139,87,0.04);
    font-size: 0.76rem;
}
.explorer-chart-head {
    background: rgba(255,255,255,0.70);
    border: 1px solid rgba(46,139,87,0.14);
    border-radius: 20px;
    padding: 0.75rem 0.95rem;
    margin-bottom: 0.7rem;
    box-shadow: 0 8px 20px rgba(44,62,80,0.04);
}
.explorer-chart-title {
    color: #2F855A;
    font-family: 'Poppins', sans-serif;
    font-size: 20px;
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: 0.2rem;
}
.explorer-chart-subtitle {
    color: #4A4A4A;
    font-family: "Inter", sans-serif;
    font-size: 0.95rem;
    font-weight: 450;
    line-height: 1.65;
    margin-bottom: 0.75rem;
}

/* Softer widgets only in the explorer area as best-effort global Streamlit selectors */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    min-height: 46px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(46,139,87,0.28) !important;
    background: rgba(255,255,255,0.92) !important;
    box-shadow: 0 4px 14px rgba(46,139,87,0.025) !important;
}
div[data-testid="stRadio"] [role="radiogroup"] {
    background: rgba(255,255,255,0.65) !important;
    border: 1px solid rgba(46,139,87,0.14) !important;
    border-radius: 14px !important;
    padding: 0.45rem 0.55rem !important;
}
div[data-testid="stSlider"] {
    background: rgba(255,255,255,0.76) !important;
    border: 1px solid rgba(46,139,87,0.18) !important;
    border-radius: 16px !important;
    padding: 0.35rem 0.75rem 0.2rem 0.75rem !important;
}
            
/* Hide only the min/max range labels */
.stSlider [data-testid="stTickBarMin"],
.stSlider [data-testid="stTickBarMax"]{
    display: none !important;
}

/* Streamlit can render the 5 / 50 range labels in a tick-label row; hide that row too */
.stSlider [data-baseweb="slider"] [data-testid="stTickBar"],
.stSlider [data-baseweb="slider"] [data-testid="stTickBar"] * {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    min-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Some Streamlit builds render the min/max labels as the slider's second child row */
.stSlider [data-baseweb="slider"] > div:last-child,
.stSlider [data-baseweb="slider"] > div:last-child * {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    min-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 0 !important;
}

/* Keep slider value small */
.stSlider [role="slider"]{
    font-size: 11px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<div class='explorer-hero-title'>🧭 Interactive District Explorer</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='explorer-hero-subtitle'>Filter, group, sort, and compare district-level patterns in one focused workspace. Use the controls on the left and review the dynamic summary on the right.</div>",
    unsafe_allow_html=True,
)

# Safe reset callback: avoids Streamlit session_state mutation errors after widgets are created.
def reset_explorer_controls():
    for key in ["expl_group_by", "expl_metric", "expl_sort", "expl_chart_type", "expl_topn"]:
        st.session_state.pop(key, None)

explorer_col_left, explorer_col_right = st.columns([0.9, 1.85], gap="large")

with explorer_col_left:
    st.markdown("""
    <div class="explorer-side-shell">
            <div class="explorer-side-title-row">
            <div class="explorer-side-title">Controls</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='explorer-control-label'>Group districts by</div>", unsafe_allow_html=True)
    group_by = st.selectbox(
        "Group districts by",
        options=["District", "Road_Density_Group", "Income_bin", "Roadensity Quintile"],
        index=0,
        key="expl_group_by",
        label_visibility="collapsed"
    )

    st.markdown("<div class='explorer-control-label'>Metric</div>", unsafe_allow_html=True)
    metric = st.selectbox(
        "Metric",
        options=["Rate", "Environmental_Risk_Score", "Green_Buffer_Score", "Roadensity", "Popden", "Income_median", "Records"],
        index=0,
        key="expl_metric",
        label_visibility="collapsed"
    )

    st.markdown("<div class='explorer-control-label'>Chart type</div>", unsafe_allow_html=True)
    chart_type = st.selectbox(
        "Chart type",
        options=["Bar Chart", "Lollipop", "Horizontal Bar", "Treemap", "Scatter"],
        index=0,
        key="expl_chart_type",
        label_visibility="collapsed"
    )

    st.markdown("<div class='explorer-control-label'>Sort order</div>", unsafe_allow_html=True)
    sort_order = st.radio(
        "Sort order",
        options=["Highest First", "Lowest First"],
        index=0,
        horizontal=True,
        key="expl_sort",
        label_visibility="collapsed"
    )

    st.markdown("<div class='explorer-control-label'>Top groups to show</div>", unsafe_allow_html=True)
    top_n = st.slider(
        "Top groups to show",
        min_value=5,
        max_value=50,
        value=20,
        step=1,
        key="expl_topn",
        label_visibility="collapsed"
    )

    b1, b2 = st.columns(2)
    with b1:
        st.button("Reset", key="expl_reset", use_container_width=True, on_click=reset_explorer_controls)
    with b2:
        st.button("Apply", key="expl_apply", use_container_width=True)

    st.markdown("""
    <div class="explorer-tip">
        <b>Tip:</b> Use <b>Roadensity Quintile</b> or <b>Income_bin</b> for grouped comparisons instead of single-district rankings.
    </div>
    """, unsafe_allow_html=True)

with explorer_col_right:
    def build_explorer_fig(df_in, group_by, metric, chart_type, sort_order, top_n):
        tmp = df_in.copy()

        if group_by == "Income_bin":
            try:
                tmp["Income_bin"] = pd.qcut(
                    tmp["Income_median"].rank(method="first"),
                    q=4,
                    labels=["Low", "Lower-Mid", "Upper-Mid", "High"]
                )
            except Exception:
                tmp["Income_bin"] = "Selected"

        if group_by == "Roadensity Quintile":
            try:
                tmp["Roadensity Quintile"] = pd.qcut(
                    tmp["Roadensity"],
                    q=5,
                    labels=["Q1", "Q2", "Q3", "Q4", "Q5"]
                )
            except Exception:
                tmp["Roadensity Quintile"] = pd.qcut(
                    tmp["Roadensity"].rank(method="first"),
                    q=5,
                    labels=["Q1", "Q2", "Q3", "Q4", "Q5"]
                )

        if metric == "Records":
            agg = tmp.groupby(group_by).size().reset_index(name="MetricValue")
        else:
            if metric not in tmp.columns:
                tmp[metric] = np.nan
            agg = tmp.groupby(group_by)[metric].median().reset_index(name="MetricValue")

        agg = agg.dropna(subset=[group_by])
        ascending = sort_order == "Lowest First"
        agg = agg.sort_values("MetricValue", ascending=ascending).head(top_n)
        agg[group_by] = agg[group_by].astype(str)

        if chart_type == "Bar Chart":
            fig = px.bar(
                agg,
                x=group_by,
                y="MetricValue",
                text=agg["MetricValue"].round(2),
                labels={"MetricValue": metric, group_by: group_by}
            )
            fig.update_traces(
                marker_color=COLORS["green"],
                textposition="outside",
                marker_line_width=0,
                opacity=0.92
            )

        elif chart_type == "Horizontal Bar":
            fig = px.bar(
                agg,
                x="MetricValue",
                y=group_by,
                orientation="h",
                text=agg["MetricValue"].round(2),
                labels={"MetricValue": metric, group_by: group_by}
            )
            fig.update_traces(
                marker_color=COLORS["green"],
                textposition="outside",
                marker_line_width=0,
                opacity=0.92
            )

        elif chart_type == "Lollipop":
            fig = go.Figure()
            fig.add_trace(go.Bar(
                x=agg["MetricValue"],
                y=agg[group_by],
                orientation="h",
                marker_color="rgba(46,139,87,0.13)",
                hoverinfo="skip",
                showlegend=False
            ))
            fig.add_trace(go.Scatter(
                x=agg["MetricValue"],
                y=agg[group_by],
                mode="markers+text",
                text=agg["MetricValue"].round(2),
                textposition="middle right",
                marker=dict(size=13, color=COLORS["green"], line=dict(width=0)),
                showlegend=False
            ))
            fig.update_layout(yaxis=dict(categoryorder="total ascending"))

        elif chart_type == "Scatter":
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=agg[group_by],
                y=agg["MetricValue"],
                mode="markers",
                marker=dict(size=12, color=COLORS["green"], opacity=0.85, line=dict(width=0)),
                showlegend=False
            ))

        else:
            fig = px.treemap(
                agg,
                path=[group_by],
                values="MetricValue",
                color="MetricValue",
                color_continuous_scale=["#EAF7EF", "#F4B942", "#E85D75"]
            )

        explorer_layout = dict(common_layout)
        explorer_layout["margin"] = dict(l=45, r=18, t=18, b=50)
        explorer_layout["plot_bgcolor"] = "rgba(255,255,255,0.34)"
        explorer_layout["paper_bgcolor"] = "rgba(0,0,0,0)"

        fig.update_layout(
            **explorer_layout,
            showlegend=False,
            height=495,
            transition={"duration": 250, "easing": "cubic-in-out"}
        )
        fig.update_xaxes(
            automargin=True,
            tickfont=dict(size=9),
            title_font=dict(size=10),
            gridcolor="rgba(46,139,87,0.08)",
            zeroline=False
        )
        fig.update_yaxes(
            automargin=True,
            tickfont=dict(size=9),
            title_font=dict(size=10),
            gridcolor="rgba(46,139,87,0.08)",
            zeroline=False
        )

        return fig, agg

    fig_explorer, agg_df = build_explorer_fig(
        filtered, group_by, metric, chart_type, sort_order, top_n
    )

    st.markdown(f"""
    <div class="explorer-kpis">
        <div class="explorer-kpi">📊 Records: {len(filtered)}</div>
        <div class="explorer-kpi">🧩 Groups: {len(agg_df)}</div>
        <div class="explorer-kpi">📈 Metric: {metric}</div>
        <div class="explorer-kpi">↕ Sort: {sort_order}</div>
    </div>
    <div class="explorer-chart-head">
        <div class="explorer-chart-title">{metric} by {group_by}</div>
        <div class="explorer-chart-subtitle">Dynamic grouping, sorting, and chart-type comparison.</div>
    </div>
    """, unsafe_allow_html=True)

    render_chart_card(
        f"{metric} by {group_by}",
        "Interactive grouped comparison workspace.",
        fig_explorer,
        f"<b>Records:</b> {len(filtered)} · <b>Groups shown:</b> {len(agg_df)}",
        height=UNIFORM_CHART_CONTAINER_HEIGHT
    )



st.markdown("<div class='explorer-table-shell'></div>", unsafe_allow_html=True)
with st.expander("Show grouped data table", expanded=False):
    st.dataframe(
        agg_df.reset_index(drop=True),
        use_container_width=True,
        hide_index=True
    )

# =========================================================
# ENVIRONMENTAL SCENARIO SIMULATION SECTION
# =========================================================

st.markdown("""
<style>

/* =========================================================
SIMULATION CONTROL ALIGNMENT FIX
========================================================= */

.sim-control-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1.25rem;
    margin-top: 1rem;
    margin-bottom: 2rem;
}

.sim-control-box {
    background: rgba(255,255,255,0.96);
    border: 1px solid #D7E5DA;
    border-radius: 20px;
    padding: 1rem 1rem 0.9rem 1rem;
    min-height: 135px;
    box-shadow: 0 8px 20px rgba(44,62,80,0.05);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

.sim-control-label {
    font-size: 0.95rem;
    font-weight: 700;
    color: #2E8B57;
    margin-bottom: 0.65rem;
}

/* Make Streamlit widgets inside simulation section look aligned */
div[data-testid="stSelectbox"] label {
    color: #2E8B57 !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
}

div[data-testid="stSelectbox"] {
    margin-top: 0 !important;
    height: 58px !important;
    min-height: 58px !important;
    display: flex !important;
    align-items: center !important;
    box-sizing: border-box !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    height: 58px !important;
    min-height: 58px !important;
    border-radius: 16px !important;

    display: flex !important;
    align-items: center !important;

    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* Align question mark vertically */
div[data-testid="stSelectbox"] button {
    margin-top: 0px !important;
}

/* Align dropdown text vertically */
div[data-testid="stSelectbox"] span {
    display: flex !important;
    align-items: center !important;
}

/* Help icon positioning */
div[data-testid="stSelectbox"] button {
    margin-top: -2px !important;
}

/* Prevent vertical spacing jumps */
div[data-testid="stVerticalBlock"] > div {
    gap: 0.35rem !important;
}
            
.select-align-spacer {
height: 34px;
}

div[data-testid="stSelectbox"] {
margin-top: 0px !important;
padding-top: 0px !important;
height: 58px !important;
min-height: 58px !important;
display: flex !important;
align-items: center !important;
box-sizing: border-box !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
height: 58px !important;
min-height: 58px !important;
border-radius: 16px !important;
display: flex !important;
align-items: center !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<div class='section-title'>🌍 Environmental Scenario Simulation</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='section-subtitle'>Explore how changes in urban environmental conditions may affect environmental vulnerability patterns and protection levels across districts. This section is for exploratory environmental analytics only and does not imply direct causation or medical prediction of autism.</div>",
    unsafe_allow_html=True,
)

scenario_df = filtered.copy()

st.markdown("""
<div class="section-card">
    <div class="section-title">⚙️ Simulation Controls Panel</div>
    <div class="section-subtitle">
        Adjust environmental and urban conditions to explore hypothetical vulnerability shifts.
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Aligned Simulation Controls
# -----------------------------
control1, control2, control3, control4 = st.columns(
    [1, 1, 1, 1.08],
    gap="medium"
)

with control1:
    st.markdown('<div class="sim-control-label">Green Space Adjustment (%)</div>', unsafe_allow_html=True)
    green_adjustment = st.slider(
        "Green Space Adjustment (%)",
        min_value=-20,
        max_value=50,
        value=0,
        step=5,
        help="Simulates increase or decrease in urban green coverage.",
        label_visibility="collapsed"
    )

with control2:
    st.markdown('<div class="sim-control-label">Traffic Exposure Adjustment (%)</div>', unsafe_allow_html=True)
    traffic_adjustment = st.slider(
        "Traffic Exposure Adjustment (%)",
        min_value=-30,
        max_value=40,
        value=0,
        step=5,
        help="Simulates changes in transportation and road pressure.",
        label_visibility="collapsed"
    )

with control3:
    st.markdown('<div class="sim-control-label">Population Density Adjustment (%)</div>', unsafe_allow_html=True)
    population_adjustment = st.slider(
        "Population Density Adjustment (%)",
        min_value=-15,
        max_value=30,
        value=0,
        step=5,
        help="Simulates urban crowding changes.",
        label_visibility="collapsed"
    )

with control4:
    st.markdown('<div class="sim-control-label">Planning Priority</div>', unsafe_allow_html=True)

    scenario_priority = st.selectbox(
        "Planning Priority",
        [
            "Balanced Urban Planning",
            "Green Infrastructure Focus",
            "Traffic Reduction Focus",
            "High Urbanization Scenario"
        ],
        label_visibility="collapsed"
    )

def apply_scenario_priority(priority, green_adjustment, traffic_adjustment, population_adjustment):
    effective_green_adjustment = green_adjustment
    effective_traffic_adjustment = traffic_adjustment
    effective_population_adjustment = population_adjustment

    if priority == "Green Infrastructure Focus":
        effective_green_adjustment += 25
        effective_traffic_adjustment -= 5
    elif priority == "Traffic Reduction Focus":
        effective_traffic_adjustment -= 20
        effective_green_adjustment += 5
    elif priority == "High Urbanization Scenario":
        effective_population_adjustment += 20
        effective_traffic_adjustment += 20
        effective_green_adjustment -= 10
    else:
        effective_green_adjustment += 5
        effective_traffic_adjustment -= 5

    return effective_green_adjustment, effective_traffic_adjustment, effective_population_adjustment

# -----------------------------
# Apply Preset Scenario Effects
# -----------------------------
green_adjustment, traffic_adjustment, population_adjustment = apply_scenario_priority(
    scenario_priority,
    green_adjustment,
    traffic_adjustment,
    population_adjustment,
)

effective_green_adjustment = green_adjustment
effective_traffic_adjustment = traffic_adjustment
effective_population_adjustment = population_adjustment

# -----------------------------
# LITERATURE-SUPPORTED BASELINE NORMALIZATION
# Rule: simulated values are normalized using the original district baseline range,
# then clipped between 0 and 1 to avoid out-of-bound scaling.
# -----------------------------
def normalize_using_baseline(sim_series, baseline_series):
    baseline_min = baseline_series.min()
    baseline_max = baseline_series.max()

    if baseline_max == baseline_min:
        return pd.Series(0, index=sim_series.index)

    return ((sim_series - baseline_min) / (baseline_max - baseline_min)).clip(0, 1)


# -----------------------------
# Simulation Recalculation Engine
# -----------------------------
scenario_df = filtered.copy()

scenario_df["Sim_Green_Coverage"] = scenario_df["Prdcan100"] * (1 + effective_green_adjustment / 100)
scenario_df["Sim_Green_Buffer_Score"] = scenario_df["Green_Buffer_Score"] * (1 + effective_green_adjustment / 100)
scenario_df["Sim_Roadensity"] = scenario_df["Roadensity"] * (1 + effective_traffic_adjustment / 100)
scenario_df["Sim_Popden"] = scenario_df["Popden"] * (1 + effective_population_adjustment / 100)

for col in ["Sim_Green_Coverage", "Sim_Green_Buffer_Score", "Sim_Roadensity", "Sim_Popden"]:
    scenario_df[col] = scenario_df[col].clip(lower=0)

# Baseline-normalized simulated values
scenario_df["Sim_Green_norm"] = normalize_using_baseline(
    scenario_df["Sim_Green_Buffer_Score"],
    scenario_df["Green_Buffer_Score"]
)

scenario_df["Sim_Road_norm"] = normalize_using_baseline(
    scenario_df["Sim_Roadensity"],
    scenario_df["Roadensity"]
)

scenario_df["Sim_Pop_norm"] = normalize_using_baseline(
    scenario_df["Sim_Popden"],
    scenario_df["Popden"]
)

# Income is a socioeconomic control/adaptive-capacity layer, not changed by scenario sliders.
scenario_df["Sim_Income_norm"] = scenario_df["Income_norm"]


# -----------------------------
# Baseline Indices
# Literature-supported structure:
# USI = 60% road density + 40% population density
# EPS = 70% green buffering + 30% income context
# EVI = 45% urban stress + 35% autism prevalence context + 20% missing protection
# -----------------------------
scenario_df["Baseline_Urban_Stress_Index"] = (
    0.60 * scenario_df["Road_norm"] +
    0.40 * scenario_df["Pop_norm"]
) * 100

scenario_df["Baseline_Environmental_Protection_Score"] = (
    0.70 * scenario_df["Green_norm"] +
    0.30 * scenario_df["Income_norm"]
) * 100

scenario_df["Baseline_Exposure_Balance_Score"] = (
    scenario_df["Baseline_Environmental_Protection_Score"] -
    scenario_df["Baseline_Urban_Stress_Index"]
)

scenario_df["Baseline_Environmental_Vulnerability_Index"] = (
    0.45 * scenario_df["Baseline_Urban_Stress_Index"] +
    0.35 * scenario_df["Rate_norm"] * 100 +
    0.20 * (100 - scenario_df["Baseline_Environmental_Protection_Score"])
).clip(0, 100)


# -----------------------------
# Simulated Indices
# -----------------------------
scenario_df["Urban_Stress_Index"] = (
    0.60 * scenario_df["Sim_Road_norm"] +
    0.40 * scenario_df["Sim_Pop_norm"]
) * 100

scenario_df["Environmental_Protection_Score"] = (
    0.70 * scenario_df["Sim_Green_norm"] +
    0.30 * scenario_df["Sim_Income_norm"]
) * 100

scenario_df["Exposure_Balance_Score"] = (
    scenario_df["Environmental_Protection_Score"] -
    scenario_df["Urban_Stress_Index"]
)

scenario_df["Environmental_Vulnerability_Index"] = (
    0.45 * scenario_df["Urban_Stress_Index"] +
    0.35 * scenario_df["Rate_norm"] * 100 +
    0.20 * (100 - scenario_df["Environmental_Protection_Score"])
).clip(0, 100)


# -----------------------------
# Literature-supported Classification Thresholds
# Protected Zone: EVI < 35
# Moderate Exposure Zone: 35 <= EVI < 55
# High Vulnerability Zone: 55 <= EVI < 75
# Critical Urban Stress Zone: EVI >= 75
# -----------------------------
def classify_vulnerability(score):
    if score < 35:
        return "Protected Zone"
    elif score < 55:
        return "Moderate Exposure Zone"
    elif score < 75:
        return "High Vulnerability Zone"
    else:
        return "Critical Urban Stress Zone"

scenario_df["Baseline_Vulnerability_Zone"] = scenario_df["Baseline_Environmental_Vulnerability_Index"].apply(classify_vulnerability)
scenario_df["Simulated_Vulnerability_Zone"] = scenario_df["Environmental_Vulnerability_Index"].apply(classify_vulnerability)


# -----------------------------
# KPI Metrics
# -----------------------------
baseline_vulnerability = scenario_df["Baseline_Environmental_Vulnerability_Index"].median()
simulated_vulnerability = scenario_df["Environmental_Vulnerability_Index"].median()

baseline_stress = scenario_df["Baseline_Urban_Stress_Index"].median()
simulated_stress = scenario_df["Urban_Stress_Index"].median()

baseline_protection = scenario_df["Baseline_Environmental_Protection_Score"].median()
simulated_protection = scenario_df["Environmental_Protection_Score"].median()

baseline_balance = scenario_df["Baseline_Exposure_Balance_Score"].median()
exposure_balance = scenario_df["Exposure_Balance_Score"].median()

vulnerability_change = simulated_vulnerability - baseline_vulnerability
stress_change = simulated_stress - baseline_stress
protection_change = simulated_protection - baseline_protection
balance_change = exposure_balance - baseline_balance


# -----------------------------
# KPI Display
# -----------------------------
st.markdown("<div class='dashboard-title'>📌 Simulated Environmental Metrics</div>", unsafe_allow_html=True)

scenario_kpi_cards = [
    kpi_card(
        "Environmental Vulnerability Index",
        f"{simulated_vulnerability:.2f}",
        f"Change from baseline: {vulnerability_change:+.2f}",
        COLORS["coral"] if vulnerability_change > 0 else COLORS["green"]
    ),
    kpi_card(
        "Urban Stress Index",
        f"{simulated_stress:.2f}",
        f"Change from baseline: {stress_change:+.2f}",
        "#D97706" if stress_change >= 0 else COLORS["green"]
    ),
    kpi_card(
        "Environmental Protection Score",
        f"{simulated_protection:.2f}",
        f"Change from baseline: {protection_change:+.2f}",
        COLORS["green"] if protection_change >= 0 else COLORS["coral"]
    ),
    kpi_card(
        "Exposure Balance Score",
        f"{exposure_balance:.2f}",
        f"Change from baseline: {balance_change:+.2f}",
        COLORS["green"] if exposure_balance >= 0 else COLORS["coral"]
    )
]

scenario_summary_html = f"""
<div class="scenario-summary-box" style="
    background:#F1FAF4;
    border:1px solid #CBEBD6;
    border-radius:18px;
    padding:1rem 1.1rem;
">
<b>Dynamic Scenario Summary:</b><br>
    Under the <b>{scenario_priority}</b> scenario, green space changed by
    <b>{effective_green_adjustment:+}%</b>, traffic exposure changed by
    <b>{effective_traffic_adjustment:+}%</b>, and population density changed by
    <b>{effective_population_adjustment:+}%</b>. The simulated Environmental Vulnerability Index is
    <b>{simulated_vulnerability:.2f}</b>, with a baseline change of
    <b>{vulnerability_change:+.2f}</b>.
</div>
"""

render_kpi_summary_block(
    scenario_kpi_cards,
    scenario_summary_html,
    summary_gap_px=18,
    height=300
)


# -----------------------------
# Interpretation Panel
# -----------------------------
protected_count = int((scenario_df["Simulated_Vulnerability_Zone"] == "Protected Zone").sum())
moderate_count = int((scenario_df["Simulated_Vulnerability_Zone"] == "Moderate Exposure Zone").sum())
high_count = int((scenario_df["Simulated_Vulnerability_Zone"] == "High Vulnerability Zone").sum())
critical_count = int((scenario_df["Simulated_Vulnerability_Zone"] == "Critical Urban Stress Zone").sum())

st.markdown("""
<div class="section-card">
    <div class="section-title">🧠 Environmental Interpretation Panel</div>
    <div class="section-subtitle">
        Based on the selected simulation, the model classified districts into the following environmental vulnerability groups:
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="insight-box">
    <b>Protected Zone:</b> {protected_count} district(s)<br>
    <b>Moderate Exposure Zone:</b> {moderate_count} district(s)<br>
    <b>High Vulnerability Zone:</b> {high_count} district(s)<br>
    <b>Critical Urban Stress Zone:</b> {critical_count} district(s)
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Decision logic uses:
# ΔEVI = vulnerability movement
# ΔUSI = urban stress movement
# ΔEPS = protection movement
# EBS = protection minus stress
# -----------------------------
if vulnerability_change > 0 and stress_change > 0 and protection_change <= 0:
    planning_insight = (
        "The simulation indicates increasing environmental vulnerability. Urban stress has risen while environmental protection has weakened or remained unchanged, suggesting that exposure pressures may be growing faster than buffering capacity. Planning efforts should prioritize traffic reduction, green infrastructure expansion, and the preservation of open spaces."
    )

elif exposure_balance < 0 and stress_change > protection_change:
    planning_insight = (
        "The simulation indicates that urban stress currently exceeds environmental protection. This suggests that built-environment pressures may be outpacing the district's ecological and socioeconomic buffering capacity. Strengthening environmental protection measures may help improve resilience in vulnerable areas."
    )

elif exposure_balance >= 0 and protection_change >= stress_change:
    planning_insight = (
        "The simulation indicates that environmental protection currently matches or exceeds urban stress. Existing green buffers and adaptive capacities appear to be helping offset exposure pressures. Continued protection of green corridors and monitoring of high-road-density districts is recommended."
    )

elif stress_change > 0 and effective_population_adjustment > 0:
    planning_insight = (
        "The simulation indicates increasing urban density pressure. Growth in population concentration is contributing to higher environmental stress levels, which may increase exposure burdens over time. Planning strategies should focus on managing density while maintaining access to protective green spaces."
    )

elif effective_green_adjustment > 0 and protection_change > 0:
    planning_insight = (
        "The simulation indicates improved environmental protection capacity. Increased green infrastructure appears to strengthen buffering conditions and may help offset environmental exposure pressures. Continued investment in tree cover, green corridors, and open-space preservation is recommended."
    )

elif effective_traffic_adjustment < 0 and stress_change < 0:
    planning_insight = (
        "The simulation indicates reduced urban stress following lower traffic exposure levels. This suggests that transportation-related pressures contribute substantially to environmental vulnerability. Traffic-calming measures and low-exposure transport planning may support more resilient community environments."
    )

elif abs(vulnerability_change) < 2:
    planning_insight = (
        "The simulation indicates minimal change in overall environmental vulnerability. Current adjustments appear insufficient to substantially alter district-level vulnerability patterns. Larger interventions or combined planning strategies may be needed to produce meaningful shifts."
    )

else:
    planning_insight = (
        "The simulation indicates mixed environmental outcomes. While some conditions improved, others remained unchanged or moved in the opposite direction. A balanced planning approach that addresses both exposure pressures and protective buffering capacity may provide the most effective long-term strategy."
    )
    
st.markdown(f"""
<div class="insight-box">
    <b>Dynamic Planning Insight:</b><br>
    {planning_insight}
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="warning-box">
    <b>Ethical and Research Disclaimer:</b><br>
    This simulation explores environmental vulnerability and exposure patterns only.
    Results do not imply direct causation, diagnosis, or prediction of autism.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# =========================================================
# ANALYSIS AND INSIGHTS
# =========================================================

st.markdown(
    '<h2 style="color:#2E8B57;font-weight:800;font-size:2.2rem;font-family:Poppins,sans-serif;margin-bottom:1rem;">📊 Final Analysis & Insights</h2>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
<div style="background: linear-gradient(
    135deg,
    rgba(232, 247, 236, 0.98) 0%,
    rgba(255, 255, 255, 0.99) 50%,
    rgba(255, 245, 204, 0.96) 100%
);padding:28px;border-radius:22px;border:1px solid #D7E5DA;box-shadow:0 14px 32px rgba(44,62,80,0.10);border-top:5px solid #E85D75;min-height:650px;height:100%;
min-height:668px;display:flex;flex-direction:column;justify-content:flex-start;overflow:visible;padding-bottom:60px;">
<h3 style="color:#E85D75;font-size:1.55rem;font-weight:800;margin-bottom:18px;font-family:Poppins,sans-serif;">🌍 Environmental Vulnerability Patterns Across Districts</h3>
<p style="color:#4A4A4A;font-size:15px;line-height:1.85;font-family:Poppins,Segoe UI,Arial,sans-serif;margin:0;">
Environmental vulnerability in the dataset reflects the balance between urban exposure and environmental buffering capacity. Districts with denser road networks and higher population concentrations tend to experience greater environmental pressure, while districts with stronger green buffering and tree canopy coverage may be better protected from urban stressors.
<br><br>
This framework is supported by research showing that road density serves as a proxy for traffic-related exposures and urban development intensity, while green spaces and tree canopy can reduce exposure to air pollution and other environmental burdens. In their California school district study, <b>Wu and Jackson (2017)</b> incorporated road density, urban land, and multiple green space indicators because these variables capture differences in environmental conditions across communities.
Similarly, <b>Anderson et al. (2014)</b> found that children living near major roadways were more likely to have autism, suggesting that traffic-related environmental exposures may be an important environmental pressure indicator.
<br><br>
<span style="color:#F59E0B;font-weight:800;">👉 Insight:</span> Districts with high road density and population concentration but limited green buffering tend to exhibit greater environmental vulnerability, while districts with stronger tree canopy and green coverage appear more environmentally protected.
</p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div style="background: linear-gradient(
    135deg,
    rgba(232, 247, 236, 0.98) 0%,
    rgba(255, 255, 255, 0.99) 50%,
    rgba(255, 245, 204, 0.96) 100%
);padding:28px;border-radius:22px;border:1px solid #D7E5DA;box-shadow:0 14px 32px rgba(44,62,80,0.10);border-top:5px solid #2E8B57;min-height:650px;height:auto;overflow:visible;padding-bottom:60px;">
<h3 style="color:#2E8B57;font-size:1.55rem;font-weight:800;margin-bottom:18px;font-family:Poppins,sans-serif;">🧩 Autism Prevalence Patterns Across Districts</h3>
<p style="color:#4A4A4A;font-size:15px;line-height:1.85;font-family:Poppins,Segoe UI,Arial,sans-serif;margin:0;">
Autism prevalence varies across districts alongside differences in environmental and socioeconomic conditions. Districts with lower green buffering and greater road exposure often display different prevalence patterns than districts with stronger environmental protection. While these patterns do not establish causation, they reveal meaningful environmental associations.
<br><br>
This observation aligns with the findings of <b>Wu and Jackson (2017)</b>, who reported that higher tree canopy and green space coverage were associated with lower childhood autism prevalence, whereas urban land and road density showed positive associations with prevalence.
<br><br>
Supporting this relationship, <b>Weisskopf et al. (2015)</b> reported that residential proximity to freeways and major roads was associated with increased odds of autism spectrum disorder, highlighting the potential relevance of traffic-related environmental conditions.
<br><br>
<br>
<span style="color:#F59E0B;font-weight:800;">👉 Insight:</span> Districts with stronger green buffering and tree canopy coverage tend to exhibit different autism prevalence patterns than districts with greater road exposure and urban pressure, consistent with literature linking environmental conditions to autism prevalence patterns while avoiding direct causal conclusions.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""
<div style="
    background: linear-gradient(135deg, #E8F7EE 0%, #DFF3E7 50%, #D4EDDA 100%);
    border: 1px solid rgba(46,139,87,0.25);
    border-radius: 24px;
    padding: 30px 34px;
    margin-top: 40px;
    box-shadow: 0 14px 32px rgba(44,62,80,0.10);
">

<h2 style="
    color:#2E8B57;
    font-size:2.4rem;
    font-weight:800;
    margin-bottom:24px;
    font-family:Poppins,sans-serif;
">
🔎 References
</h2>

<div style="
    color:#4A4A4A;
    font-size:1.1rem;
    line-height:1.4;
    font-family:Poppins,'Segoe UI',Arial,sans-serif;
">

<p>
<b style="color:#2E8B57;">Carter, S., Rahman, M. M., Lin, J. C., Deng, H., Liu, J., Fan, Z., Eckel, S. P., Chen, Z., &amp; Xiang, A. H.</b>
(<b style="color:#2E8B57;">2022</b>).
<i>In utero exposure to near-roadway air pollution and autism spectrum disorder in children.</i>
Environment International, 158, 106898.<b style="color:#2E8B57;">https://doi.org/10.1016/j.envint.2021.106898</b>
</p>

<p>
<b style="color:#2E8B57;">Pagalan, L., Oberlander, T. F., Hanley, G. E., Sinyor, M., Henderson, S. B., &amp; van den Bosch, M.</b>
(<b style="color:#2E8B57;">2022</b>).
<i>The association between prenatal greenspace exposure and autism spectrum disorder, and the potentially mediating role of air pollution reduction: A population-based birth cohort study.</i>
Environment International, 170, 107582. <b style="color:#2E8B57;">https://doi.org/10.1016/j.envint.2022.107582</b>
</p>

<p>
<b style="color:#2E8B57;">Wu, J.</b>
(<b style="color:#2E8B57;">2017</b>).
<i>Autism and green space_clean [Data set].</i>
U.S. Environmental Protection Agency, Office of Research and Development.<b style="color:#2E8B57;">https://doi.org/10.23719/1374806</b>
</p>

<p>
<b style="color:#2E8B57;">Wu, J., & Jackson, L.</b>
(<b style="color:#2E8B57;">2017</b>).
<i>Inverse relationship between urban green space and childhood autism in California elementary school districts.</i>
Environment International, 107, 140–146. <b style="color:#2E8B57;">https://doi.org/10.1016/j.envint.2017.07.010</b>

</p>

<p>
<b style="color:#2E8B57;">Wu, J., Yu, H., & Jackson, L.</b>
(<b style="color:#2E8B57;">2024</b>).
<i>Association between autism spectrum disorder and environmental quality in the United States.</i>
ISPRS International Journal of Geo-Information, 13(9), 308.<b style="color:#2E8B57;">https://doi.org/10.3390/ijgi13090308</b>

</p>

<p>
<b style="color:#2E8B57;">Volk, H. E., Lurmann, F., Penfold, B., Hertz-Picciotto, I., &amp; McConnell, R.</b>
(<b style="color:#2E8B57;">2013</b>).
<i>Traffic-related air pollution, particulate matter, and autism.</i>
JAMA Psychiatry, 70(1), 71–77. <b style="color:#2E8B57;">https://doi.org/10.1001/jamapsychiatry.2013.266</b>
</p>

<p style="margin-bottom:0;">
<b style="color:#2E8B57;">Volk, H. E., Hertz-Picciotto, I., Delwiche, L., Lurmann, F., &amp; McConnell, R.</b>
(<b style="color:#2E8B57;">2011</b>).
<i>Residential proximity to freeways and autism in the CHARGE study.</i>
Environmental Health Perspectives, 119(6), 873–877.<b style="color:#2E8B57;">https://pmc.ncbi.nlm.nih.gov/articles/PMC3114825</b>
</p>

</div>
</div>
""", unsafe_allow_html=True)




st.markdown("""
<style>

/* =========================================================
   ENVIRONMENTAL DASHBOARD FOOTER
========================================================= */

.footer {
    margin-top: 3rem;
    padding: 2rem 1rem;

    text-align: center;

    color: #475569;
    font-size: 0.95rem;
    line-height: 1;

    border-top: 1px solid rgba(46,139,87,0.25);

    background: linear-gradient(
        90deg,
        rgba(235,247,238,0.15) 0%,
        rgba(255,255,255,0.05) 50%,
        rgba(247,241,212,0.10) 100%
    );
}

.footer b {
    color: #2E8B57;
    font-weight: 700;
}

.footer-highlight {
    color: #D4AF37;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">

Data Source: <b>Inverse Relationship Between Urban Green Space and Childhood Autism in California Elementary School Districts</b> (Wu & Jackson, 2017).<br>

This dashboard explores environmental vulnerability, urban stress, green buffering capacity, and autism prevalence patterns for academic and analytical purposes only.<br>

Built using <b>Python</b>, <b>Streamlit</b>, <b>Pandas</b>, <b>NumPy</b>, <b>Plotly</b>, and <b>Scikit-Learn</b>.

</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>


""", unsafe_allow_html=True)

st.markdown("""
<style>

            
/* =========================================================
MARQUEE
========================================================= */

.marquee-container {
    width: 100%;
    overflow: hidden;
    position: relative;
    background: #F3EBCB;
    );

    border:1px solid rgba(194, 165, 84, 0.45);
    border-radius: 999px;

    padding: 14px 0;
    margin: 1rem 0 2rem 0;

    box-shadow:
    0 0 4px rgba(194,165,84,0.12),
    0 4px 12px rgba(194,165,84,0.08),
    inset 0 0 6px rgba(255,255,255,0.35);
}

.marquee {
    display: flex;
    width: max-content;
    align-items: center;
    animation: marquee-scroll 28s linear infinite;
}

.marquee span {
    font-family: "Poppins", sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    white-space: nowrap;

    color: #1F6F4A;

    text-shadow:
        0 0 4px rgba(31,111,74,0.25),
        0 0 8px rgba(31,111,74,0.15);
}

.marquee-divider {
    margin: 0 3rem;

    color: #B8860B;

    text-shadow:
        0 0 6px rgba(212,175,55,0.60),
        0 0 12px rgba(212,175,55,0.40);

    font-size: 1.2rem;
}

@keyframes marquee-scroll {
    from {
        transform: translateX(0%);
    }
    to {
        transform: translateX(-50%);
    }
}

.marquee-container:hover .marquee {
    animation-play-state: paused;
}

</style>

<div class="marquee-container">
    <div class="marquee">
        <span>Florence Elaine G. Soleño • BSIS 3-B • Analytics Tools and Techniques • Environmental Vulnerability and Autism Pattern Dashboard • EST. 2026</span>
        <span class="marquee-divider">🟢</span>
        <span>Florence Elaine G. Soleño • BSIS 3-B • Analytics Tools and Techniques • Environmental Vulnerability and Autism Pattern Dashboard • EST. 2026</span>
        <span class="marquee-divider">🟢</span>
        <span>Florence Elaine G. Soleño • BSIS 3-B • Analytics Tools and Techniques • Environmental Vulnerability and Autism Pattern Dashboard • EST. 2026</span>
        <span class="marquee-divider">🟢</span>
    </div>
</div>
""", unsafe_allow_html=True)


