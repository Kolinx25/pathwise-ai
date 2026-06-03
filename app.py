# ============================================================
# PATHWISE AI
# UNIVERSITY STUDENT RISK AND LEARNING PATHWAY DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path
from streamlit_echarts import st_echarts


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PathWise AI",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>
    .main {
        background-color: #F8FAFC;
    }

    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
        padding-left: 2.5rem;
        padding-right: 2.5rem;
        max-width: 1550px;
    }

    html, body, [class*="css"] {
        font-family: "Segoe UI", Arial, sans-serif;
    }

    header[data-testid="stHeader"] {
        background: transparent;
        height: 0rem;
    }

    div[data-testid="stAppViewContainer"] {
        padding-top: 0rem !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #023047;
        top: 0rem !important;
        height: 100vh !important;
    }

    section[data-testid="stSidebar"] * {
        color: #F8FAFC;
    }

    div[data-testid="stSidebarUserContent"] {
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] .stRadio label {
        font-size: 0.98rem !important;
        font-weight: 500 !important;
    }

    section[data-testid="stSidebar"] label {
        padding: 0.25rem 0rem;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background-color: rgba(142, 202, 230, 0.12);
        border-radius: 10px;
    }

    .dashboard-title {
        font-size: 2.45rem;
        font-weight: 850;
        color: #023047;
        margin-top: 0.4rem;
        margin-bottom: 0.65rem;
        letter-spacing: -0.025em;
        line-height: 1.35;
        overflow: visible;
    }

    .dashboard-subtitle {
        font-size: 1.03rem;
        color: #475569;
        margin-bottom: 1.6rem;
        line-height: 1.65;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #023047;
        margin-top: 2rem;
        margin-bottom: 1rem;
        line-height: 1.4;
        overflow: visible;
    }

    h1, h2, h3 {
        line-height: 1.35 !important;
        overflow: visible !important;
        padding-top: 0.15rem;
    }

    .top-brand-row {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }

    .top-brand-title {
        font-size: 3rem;
        font-weight: 850;
        color: #023047;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -0.04em;
    }

    .top-brand-subtitle {
        font-size: 1rem;
        color: #475569;
        margin-top: 0.35rem;
        line-height: 1.5;
    }

    .institution-label {
        font-size: 0.82rem;
        color: #64748B;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.25rem;
    }

    .hero-card {
        background: linear-gradient(135deg, #023047 0%, #219EBC 100%);
        border-radius: 24px;
        padding: 2.5rem 2.5rem 2.2rem 2.5rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
        overflow: visible;
        box-shadow: 0px 18px 45px rgba(2, 48, 71, 0.20);
    }

    .hero-kicker {
        color: #8ECAE6;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        letter-spacing: 0.06em;
    }

    .hero-title {
        color: white;
        font-size: 2.75rem;
        font-weight: 850;
        line-height: 1.15;
        margin-bottom: 1rem;
        white-space: normal;
        word-break: normal;
    }

    .hero-subtitle {
        color: #F8FAFC;
        font-size: 1.08rem;
        line-height: 1.8;
        max-width: 1050px;
    }

    .kpi-card {
        background-color: #FFFFFF;
        padding: 1.15rem;
        border-radius: 18px;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 8px 24px rgba(2, 48, 71, 0.07);
        height: 150px;
    }

    .kpi-label {
        font-size: 0.75rem;
        color: #64748B;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.055em;
    }

    .kpi-value {
        font-size: 1.9rem;
        color: #023047;
        font-weight: 850;
        margin-top: 0.5rem;
    }

    .kpi-note {
        font-size: 0.8rem;
        color: #64748B;
        margin-top: 0.35rem;
        line-height: 1.45;
    }

    .insight-box {
        background-color: #FFFFFF;
        padding: 1.15rem 1.2rem;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #219EBC;
        box-shadow: 0px 8px 24px rgba(2, 48, 71, 0.055);
        margin-bottom: 1rem;
        line-height: 1.65;
        color: #0F172A;
    }

    .warning-box {
        background-color: #FFF8E6;
        padding: 1rem;
        border-radius: 14px;
        border: 1px solid #FDE68A;
        border-left: 5px solid #FFB703;
        margin-bottom: 0.8rem;
        color: #0F172A;
    }

    .success-box {
        background-color: #EAF7FB;
        padding: 1rem;
        border-radius: 14px;
        border: 1px solid #BCE3EE;
        border-left: 5px solid #219EBC;
        margin-bottom: 0.8rem;
        color: #0F172A;
    }

    .support-chip {
        background-color: #FFFFFF;
        padding: 0.95rem 1rem;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #219EBC;
        margin-bottom: 0.75rem;
        font-weight: 650;
        color: #0F172A;
        box-shadow: 0px 5px 15px rgba(2, 48, 71, 0.04);
    }

    .support-chip-high {
        background-color: #FFF4E8;
        border-left: 5px solid #FB8500;
    }

    .support-chip-medium {
        background-color: #FFF8E6;
        border-left: 5px solid #FFB703;
    }

    .support-chip-low {
        background-color: #EAF7FB;
        border-left: 5px solid #219EBC;
    }

    .risk-high {
        background-color: #FFF4E8;
        color: #9A3D00;
        padding: 0.42rem 0.85rem;
        border-radius: 999px;
        font-weight: 800;
        display: inline-block;
        border: 1px solid #FED7AA;
    }

    .risk-medium {
        background-color: #FFF8E6;
        color: #8A5A00;
        padding: 0.42rem 0.85rem;
        border-radius: 999px;
        font-weight: 800;
        display: inline-block;
        border: 1px solid #FDE68A;
    }

    .risk-low {
        background-color: #EAF7FB;
        color: #075985;
        padding: 0.42rem 0.85rem;
        border-radius: 999px;
        font-weight: 800;
        display: inline-block;
        border: 1px solid #BAE6FD;
    }

    .slide-card {
        background-color: #FFFFFF;
        border-radius: 18px;
        padding: 1.4rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 8px 24px rgba(2, 48, 71, 0.06);
        min-height: 210px;
    }

    .slide-number {
        color: #219EBC;
        font-weight: 850;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .slide-heading {
        color: #023047;
        font-weight: 850;
        font-size: 1.25rem;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    .slide-text {
        color: #475569;
        line-height: 1.6;
        font-size: 0.95rem;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 14px;
    }

    div[data-testid="stChatMessage"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 1.2rem;
        box-shadow: 0px 6px 20px rgba(2, 48, 71, 0.045);
        margin-bottom: 1rem;
    }

    div[data-testid="stChatMessage"] p {
        line-height: 1.6;
    }

    div[data-testid="stChatMessage"] table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 0.7rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stChatMessage"] th,
    div[data-testid="stChatMessage"] td {
        padding: 0.55rem 0.75rem;
        border-bottom: 1px solid #E2E8F0;
    }

    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    textarea {
        background-color: #F8FAFC !important;
        border: 1px solid #D9E2EC !important;
        border-radius: 12px !important;
    }

    .stButton > button {
        background: #219EBC;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.55rem 1.1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #023047;
        color: white;
    }

    iframe {
        border-radius: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    df = pd.read_csv("processed_data/recommendation_ready_data.csv")

    if "log_total_clicks" not in df.columns:
        df["log_total_clicks"] = np.log1p(df["total_clicks"])

    df["at_risk_probability_pct"] = df["at_risk_probability"] * 100

    return df


data = load_data()


# ============================================================
# GLOBAL SETTINGS
# ============================================================

logo_path = Path("assets/ucc_logo.png")

risk_order = ["Low Risk", "Medium Risk", "High Risk"]

risk_colors = {
    "Low Risk": "#219EBC",
    "Medium Risk": "#FFB703",
    "High Risk": "#FB8500",
    "Normal Monitoring": "#219EBC",
    "Targeted Support Recommended": "#FFB703",
    "Immediate Support Required": "#FB8500"
}

brand_colors = {
    "sky": "#8ECAE6",
    "blue_green": "#219EBC",
    "deep_blue": "#023047",
    "amber": "#FFB703",
    "orange": "#FB8500",
    "soft_bg": "#F8FAFC",
    "card_bg": "#FFFFFF",
    "muted_bg": "#F1F5F9",
    "text": "#0F172A",
    "muted_text": "#64748B"
}

plot_template = "plotly_white"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_int(x):
    return f"{int(x):,}"


def format_pct(x):
    return f"{x:.1f}%"


def split_pipe_items(text):
    if pd.isna(text):
        return []
    return [item.strip() for item in str(text).split("|") if item.strip()]


def risk_badge(risk_level):
    if risk_level == "High Risk":
        return '<span class="risk-high">High Risk</span>'
    elif risk_level == "Medium Risk":
        return '<span class="risk-medium">Medium Risk</span>'
    else:
        return '<span class="risk-low">Low Risk</span>'


def kpi_card(label, value, note=""):
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def clean_axis_labels(fig):
    fig.update_layout(
        template=plot_template,
        font=dict(family="Arial", size=13, color="#023047"),
        title_font=dict(size=16, color="#023047"),
        legend_title_text="",
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    return fig


def create_skill_gap_table(df):
    skill_gap_series = (
        df["skill_gaps"]
        .dropna()
        .str.split("|", regex=False)
        .explode()
        .str.strip()
    )

    skill_gap_counts = skill_gap_series.value_counts().reset_index()
    skill_gap_counts.columns = ["Skill Gap", "Number of Students"]

    return skill_gap_counts


def clean_gap_label(gap):
    replacements = {
        "Academic Performance Gap": "Academic Performance",
        "Moderate Performance Gap": "Moderate Performance",
        "Low Engagement Gap": "Learning Engagement",
        "Learning Platform Access Gap": "Platform Access",
        "Time Management Gap": "Time Management",
        "Academic Preparation Gap": "Academic Preparation",
        "Accessibility Support Gap": "Accessibility Support",
        "Repeat Attempt Support Gap": "Repeat Attempt Support",
        "Assessment Participation Gap": "Assessment Participation",
        "Study Consistency Gap": "Study Consistency",
        "No Major Gap Detected": "No Major Support Area Detected"
    }

    return replacements.get(gap, gap.replace(" Gap", ""))


def display_support_chip(label, risk_level="Medium Risk"):
    if risk_level == "High Risk":
        chip_class = "support-chip support-chip-high"
    elif risk_level == "Medium Risk":
        chip_class = "support-chip support-chip-medium"
    elif risk_level == "Low Risk":
        chip_class = "support-chip support-chip-low"
    else:
        chip_class = "support-chip"

    st.markdown(
        f"""
        <div class="{chip_class}">
            {label}
        </div>
        """,
        unsafe_allow_html=True
    )


def min_max_scale(series):
    if series.max() == series.min():
        return pd.Series([50] * len(series), index=series.index)

    return ((series - series.min()) / (series.max() - series.min())) * 100


def build_performance_tracker_data(df):
    tracker = df.copy()

    tracker["score_index"] = tracker["avg_score"].clip(0, 100)
    tracker["engagement_index"] = min_max_scale(tracker["total_clicks"])
    tracker["active_days_index"] = min_max_scale(tracker["active_days"])
    tracker["assessment_participation_index"] = min_max_scale(tracker["assessment_count"])
    tracker["late_submission_penalty"] = min_max_scale(tracker["late_submission_count"])

    tracker["performance_index"] = (
        0.40 * tracker["score_index"] +
        0.25 * tracker["engagement_index"] +
        0.20 * tracker["active_days_index"] +
        0.15 * tracker["assessment_participation_index"] -
        0.10 * tracker["late_submission_penalty"]
    )

    tracker["performance_index"] = tracker["performance_index"].clip(0, 100)

    tracker["performance_band"] = pd.cut(
        tracker["performance_index"],
        bins=[-1, 39, 69, 100],
        labels=[
            "Weak Performance",
            "Developing Performance",
            "Strong Performance"
        ]
    )

    return tracker


# ============================================================
# ECHARTS INTERACTIVE VISUAL HELPERS
# ============================================================

def render_echart(options, height="430px", key=None):
    return st_echarts(
        options=options,
        height=height,
        key=key
    )


def echarts_bar(
    df,
    x_col,
    y_col,
    title,
    x_name=None,
    y_name=None,
    color="#219EBC",
    horizontal=False,
    key=None,
    height="430px"
):
    if horizontal:
        options = {
            "color": [color],
            "title": {
                "text": title,
                "left": "center",
                "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "backgroundColor": "#FFFFFF",
                "borderColor": "#D9E2EC",
                "borderWidth": 1,
                "textStyle": {"color": "#023047"}
            },
            "toolbox": {
                "show": True,
                "right": 15,
                "feature": {
                    "saveAsImage": {"show": True},
                    "dataView": {"show": True, "readOnly": True},
                    "restore": {"show": True}
                }
            },
            "grid": {"left": "22%", "right": "8%", "top": "18%", "bottom": "10%"},
            "xAxis": {
                "type": "value",
                "name": x_name or x_col,
                "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
                "axisLabel": {"color": "#475569"},
                "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
            },
            "yAxis": {
                "type": "category",
                "name": y_name or y_col,
                "data": df[y_col].astype(str).tolist(),
                "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
                "axisLabel": {"color": "#475569"}
            },
            "series": [
                {
                    "name": x_name or x_col,
                    "type": "bar",
                    "data": df[x_col].round(2).tolist(),
                    "barWidth": "55%",
                    "itemStyle": {
                        "borderRadius": [0, 8, 8, 0],
                        "color": color
                    },
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 12,
                            "shadowColor": "rgba(2, 48, 71, 0.28)"
                        }
                    },
                    "label": {
                        "show": True,
                        "position": "right",
                        "color": "#023047"
                    }
                }
            ],
            "animationDuration": 900,
            "animationEasing": "cubicOut"
        }

    else:
        options = {
            "color": [color],
            "title": {
                "text": title,
                "left": "center",
                "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {"type": "shadow"},
                "backgroundColor": "#FFFFFF",
                "borderColor": "#D9E2EC",
                "borderWidth": 1,
                "textStyle": {"color": "#023047"}
            },
            "toolbox": {
                "show": True,
                "right": 15,
                "feature": {
                    "saveAsImage": {"show": True},
                    "dataView": {"show": True, "readOnly": True},
                    "restore": {"show": True}
                }
            },
            "grid": {"left": "8%", "right": "6%", "top": "18%", "bottom": "12%"},
            "xAxis": {
                "type": "category",
                "name": x_name or x_col,
                "data": df[x_col].astype(str).tolist(),
                "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
                "axisLabel": {"color": "#475569"}
            },
            "yAxis": {
                "type": "value",
                "name": y_name or y_col,
                "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
                "axisLabel": {"color": "#475569"},
                "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
            },
            "series": [
                {
                    "name": y_name or y_col,
                    "type": "bar",
                    "data": df[y_col].round(2).tolist(),
                    "barWidth": "48%",
                    "itemStyle": {
                        "borderRadius": [8, 8, 0, 0],
                        "color": color
                    },
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 12,
                            "shadowColor": "rgba(2, 48, 71, 0.28)"
                        }
                    },
                    "label": {
                        "show": True,
                        "position": "top",
                        "color": "#023047"
                    }
                }
            ],
            "animationDuration": 900,
            "animationEasing": "cubicOut"
        }

    return render_echart(options, height=height, key=key)


def echarts_risk_bar(df, key=None):
    risk_color_map = {
        "Low Risk": "#219EBC",
        "Medium Risk": "#FFB703",
        "High Risk": "#FB8500"
    }

    data_items = [
        {
            "value": int(row["Number of Students"]),
            "itemStyle": {"color": risk_color_map.get(row["Risk Level"], "#219EBC")}
        }
        for _, row in df.iterrows()
    ]

    options = {
        "title": {
            "text": "Predicted Risk Segmentation",
            "left": "center",
            "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "shadow"},
            "backgroundColor": "#FFFFFF",
            "borderColor": "#D9E2EC",
            "borderWidth": 1,
            "textStyle": {"color": "#023047"},
            "formatter": "{b}<br/>Students: {c}"
        },
        "toolbox": {
            "show": True,
            "right": 15,
            "feature": {
                "saveAsImage": {"show": True},
                "dataView": {"show": True, "readOnly": True},
                "restore": {"show": True}
            }
        },
        "grid": {"left": "8%", "right": "6%", "top": "18%", "bottom": "12%"},
        "xAxis": {
            "type": "category",
            "data": df["Risk Level"].astype(str).tolist(),
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}}
        },
        "yAxis": {
            "type": "value",
            "name": "Students",
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
            "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
        },
        "series": [
            {
                "name": "Students",
                "type": "bar",
                "data": data_items,
                "barWidth": "48%",
                "itemStyle": {"borderRadius": [8, 8, 0, 0]},
                "label": {
                    "show": True,
                    "position": "top",
                    "color": "#023047"
                },
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 16,
                        "shadowColor": "rgba(2, 48, 71, 0.30)"
                    }
                }
            }
        ],
        "animationDuration": 900,
        "animationEasing": "cubicOut"
    }

    return render_echart(options, height="430px", key=key)


def echarts_donut(df, name_col, value_col, title, key=None):
    data_items = [
        {"name": str(row[name_col]), "value": int(row[value_col])}
        for _, row in df.iterrows()
    ]

    options = {
        "color": ["#219EBC", "#8ECAE6", "#FFB703", "#FB8500", "#023047"],
        "title": {
            "text": title,
            "left": "center",
            "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
        },
        "tooltip": {
            "trigger": "item",
            "formatter": "{b}<br/>Students: {c}<br/>Share: {d}%",
            "backgroundColor": "#FFFFFF",
            "borderColor": "#D9E2EC",
            "borderWidth": 1,
            "textStyle": {"color": "#023047"}
        },
        "legend": {
            "orient": "vertical",
            "right": "2%",
            "top": "middle",
            "textStyle": {"color": "#475569"}
        },
        "toolbox": {
            "show": True,
            "right": 15,
            "feature": {
                "saveAsImage": {"show": True},
                "restore": {"show": True}
            }
        },
        "series": [
            {
                "name": title,
                "type": "pie",
                "radius": ["48%", "72%"],
                "center": ["42%", "55%"],
                "avoidLabelOverlap": True,
                "data": data_items,
                "label": {
                    "show": True,
                    "formatter": "{d}%",
                    "color": "#023047"
                },
                "emphasis": {
                    "scale": True,
                    "scaleSize": 10,
                    "itemStyle": {
                        "shadowBlur": 18,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(2, 48, 71, 0.28)"
                    }
                }
            }
        ],
        "animationDuration": 900,
        "animationEasing": "cubicOut"
    }

    return render_echart(options, height="430px", key=key)


def echarts_line_compare(df, x_col, y_cols, title, key=None):
    colors = ["#219EBC", "#FFB703", "#023047"]

    series = []
    for i, col in enumerate(y_cols):
        series.append(
            {
                "name": col,
                "type": "line",
                "smooth": True,
                "symbol": "circle",
                "symbolSize": 9,
                "data": df[col].round(2).tolist(),
                "lineStyle": {"width": 4, "color": colors[i % len(colors)]},
                "itemStyle": {"color": colors[i % len(colors)]},
                "areaStyle": {"opacity": 0.08},
                "emphasis": {"focus": "series"}
            }
        )

    options = {
        "title": {
            "text": title,
            "left": "center",
            "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
        },
        "tooltip": {
            "trigger": "axis",
            "backgroundColor": "#FFFFFF",
            "borderColor": "#D9E2EC",
            "borderWidth": 1,
            "textStyle": {"color": "#023047"}
        },
        "legend": {
            "top": "9%",
            "textStyle": {"color": "#475569"}
        },
        "toolbox": {
            "show": True,
            "right": 15,
            "feature": {
                "saveAsImage": {"show": True},
                "dataZoom": {"show": True},
                "restore": {"show": True}
            }
        },
        "grid": {"left": "7%", "right": "5%", "top": "22%", "bottom": "13%"},
        "xAxis": {
            "type": "category",
            "data": df[x_col].astype(str).tolist(),
            "axisLabel": {"color": "#475569", "rotate": 0},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}}
        },
        "yAxis": {
            "type": "value",
            "min": 0,
            "max": 100,
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
            "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
        },
        "series": series,
        "animationDuration": 1000,
        "animationEasing": "cubicOut"
    }

    return render_echart(options, height="460px", key=key)


def echarts_scatter(df, title, key=None):
    risk_color_map = {
        "Low Risk": "#219EBC",
        "Medium Risk": "#FFB703",
        "High Risk": "#FB8500"
    }

    series = []

    for risk in ["Low Risk", "Medium Risk", "High Risk"]:
        sub = df[df["risk_level"] == risk]
        data_points = [
            [
                float(row["performance_index"]),
                float(row["at_risk_probability_pct"]),
                int(row["id_student"]),
                str(row["code_module"]),
                float(row["avg_score"]),
                int(row["total_clicks"])
            ]
            for _, row in sub.iterrows()
        ]

        series.append(
            {
                "name": risk,
                "type": "scatter",
                "data": data_points,
                "symbolSize": 8,
                "itemStyle": {
                    "color": risk_color_map.get(risk, "#219EBC"),
                    "opacity": 0.68
                },
                "emphasis": {
                    "focus": "series",
                    "itemStyle": {
                        "shadowBlur": 15,
                        "shadowColor": "rgba(2, 48, 71, 0.30)"
                    }
                }
            }
        )

    options = {
        "title": {
            "text": title,
            "left": "center",
            "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
        },
        "tooltip": {
            "trigger": "item",
            "backgroundColor": "#FFFFFF",
            "borderColor": "#D9E2EC",
            "borderWidth": 1,
            "textStyle": {"color": "#023047"},
            "formatter": """
                function (params) {
                    return 'Student ID: ' + params.data[2] +
                    '<br/>Module: ' + params.data[3] +
                    '<br/>Performance Index: ' + params.data[0].toFixed(1) +
                    '<br/>Risk Probability: ' + params.data[1].toFixed(1) + '%' +
                    '<br/>Average Score: ' + params.data[4].toFixed(1) +
                    '<br/>VLE Clicks: ' + params.data[5];
                }
            """
        },
        "legend": {
            "top": "9%",
            "textStyle": {"color": "#475569"}
        },
        "toolbox": {
            "show": True,
            "right": 15,
            "feature": {
                "saveAsImage": {"show": True},
                "dataZoom": {"show": True},
                "restore": {"show": True}
            }
        },
        "grid": {"left": "7%", "right": "5%", "top": "22%", "bottom": "13%"},
        "xAxis": {
            "type": "value",
            "name": "Performance Index",
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
            "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
        },
        "yAxis": {
            "type": "value",
            "name": "Risk Probability (%)",
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
            "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
        },
        "dataZoom": [
            {"type": "inside"},
            {"type": "slider", "bottom": 5}
        ],
        "series": series,
        "animationDuration": 1000,
        "animationEasing": "cubicOut"
    }

    return render_echart(options, height="520px", key=key)


# ============================================================
# CHATBOT FUNCTIONS
# ============================================================

def get_student_summary(df, student_id):
    student_records = df[df["id_student"] == student_id]

    if student_records.empty:
        return f"I could not find a record for Student ID **{student_id}**. Check the ID and try again."

    row = student_records.iloc[0]

    gaps = split_pipe_items(row["skill_gaps"])
    gaps_clean = [clean_gap_label(gap) for gap in gaps]

    recommendations = split_pipe_items(row["recommended_pathway"])

    response = f"""
## Student Risk Brief

### Student {int(row['id_student'])}

**Risk level:** {row['risk_level']}  
**Risk probability:** {row['at_risk_probability_pct']:.1f}%  
**Support priority:** {row['support_priority']}

---

### Course Information

| Item | Details |
|---|---|
| Module | {row['code_module']} |
| Presentation | {row['code_presentation']} |
| Predicted label | {row['predicted_label']} |

---

### Academic and Engagement Profile

| Indicator | Value |
|---|---:|
| Average assessment score | {row['avg_score']:.1f} |
| Assessments completed | {int(row['assessment_count'])} |
| Late submissions | {int(row['late_submission_count'])} |
| Total VLE clicks | {int(row['total_clicks'])} |
| Active learning days | {int(row['active_days'])} |

---

### Student Background

| Indicator | Value |
|---|---|
| Previous education | {row['highest_education']} |
| Disability status | {"Reported" if row["disability"] == "Y" else "Not reported"} |

---

### Detected Support Areas
"""

    if gaps_clean:
        for gap in gaps_clean:
            response += f"\n- {gap}"
    else:
        response += "\n- No major support area detected"

    if recommendations:
        response += "\n\n---\n\n### Recommended Actions\n"
        for i, rec in enumerate(recommendations[:6], start=1):
            response += f"\n{i}. {rec}"

    return response


def get_module_summary(df, module_code):
    module_code = module_code.upper()
    module_df = df[df["code_module"].str.upper() == module_code]

    if module_df.empty:
        return f"No records were found for module **{module_code}**."

    total = len(module_df)
    risk_counts = module_df["risk_level"].value_counts()
    high = risk_counts.get("High Risk", 0)
    medium = risk_counts.get("Medium Risk", 0)
    low = risk_counts.get("Low Risk", 0)

    avg_score = module_df["avg_score"].mean()
    avg_clicks = module_df["total_clicks"].mean()
    avg_risk = module_df["at_risk_probability_pct"].mean()

    response = f"""
## Module Summary: {module_code}

| Indicator | Value |
|---|---:|
| Total student records | {total:,} |
| High Risk | {high:,} |
| Medium Risk | {medium:,} |
| Low Risk | {low:,} |
| Average assessment score | {avg_score:.1f} |
| Average VLE clicks | {avg_clicks:.1f} |
| Average risk probability | {avg_risk:.1f}% |
"""

    return response


def chatbot_response(user_query, df):
    query = user_query.lower().strip()

    if query in ["help", "what can you do", "commands", "examples"]:
        return """
## What I can help with

You can ask me questions such as:

- How many students are high risk?
- What are the top support areas?
- Show support priority summary
- Show student 6516
- What support does student 30268 need?
- Summarize module AAA
- Which students need immediate support?
- What is the average risk probability?
"""

    if "student" in query:
        numbers = [int(s) for s in query.split() if s.isdigit()]

        if len(numbers) > 0:
            return get_student_summary(df, numbers[0])

        return "Please include a student ID. Example: **show student 6516**"

    if "module" in query:
        words = query.replace(",", " ").split()
        possible_modules = df["code_module"].str.lower().unique().tolist()

        for word in words:
            if word.lower() in possible_modules:
                return get_module_summary(df, word)

        return "Please include a valid module code. Example: **summarize module AAA**"

    if "high risk" in query:
        total = len(df)
        high = df[df["risk_level"] == "High Risk"].shape[0]
        pct = high / total * 100
        return f"There are **{high:,} high-risk student records**, representing **{pct:.1f}%** of all records."

    if "medium risk" in query:
        total = len(df)
        medium = df[df["risk_level"] == "Medium Risk"].shape[0]
        pct = medium / total * 100
        return f"There are **{medium:,} medium-risk student records**, representing **{pct:.1f}%** of all records."

    if "low risk" in query:
        total = len(df)
        low = df[df["risk_level"] == "Low Risk"].shape[0]
        pct = low / total * 100
        return f"There are **{low:,} low-risk student records**, representing **{pct:.1f}%** of all records."

    if "support priority" in query or "support summary" in query:
        priority_counts = df["support_priority"].value_counts()

        response = "## Support Priority Summary\n\n"
        response += "| Support Priority | Students | Share |\n"
        response += "|---|---:|---:|\n"

        for priority, count in priority_counts.items():
            pct = count / len(df) * 100
            response += f"| {priority} | {count:,} | {pct:.1f}% |\n"

        return response

    if "skill gap" in query or "learning gap" in query or "support area" in query or "top support" in query:
        gap_table = create_skill_gap_table(df)
        gap_table["Display Label"] = gap_table["Skill Gap"].apply(clean_gap_label)

        response = "## Top Detected Support Areas\n\n"
        response += "| Support Area | Students |\n"
        response += "|---|---:|\n"

        for _, row in gap_table.head(10).iterrows():
            response += f"| {row['Display Label']} | {int(row['Number of Students']):,} |\n"

        return response

    if "immediate support" in query:
        immediate_df = df[df["support_priority"] == "Immediate Support Required"]
        count = len(immediate_df)
        pct = count / len(df) * 100

        return f"**{count:,} student records** require immediate support. This represents **{pct:.1f}%** of all records."

    if "average risk" in query or "mean risk" in query:
        avg_risk = df["at_risk_probability_pct"].mean()
        return f"The average predicted risk probability across all student records is **{avg_risk:.1f}%**."

    if "best model" in query or "model used" in query:
        return """
## Model Used

The best-performing model used for the dashboard was **Gradient Boosting**.

It was selected because it achieved strong ROC-AUC and recall performance.

The model used academic performance indicators, VLE engagement variables,
assessment participation, submission behaviour, and student background features.
"""

    return """
I could not understand that question yet.

Try asking:

- How many students are high risk?
- What are the top support areas?
- Show student 6516
- Summarize module AAA
- Show support priority summary
"""


# ============================================================
# SIDEBAR
# ============================================================

if logo_path.exists():
    st.sidebar.image(str(logo_path), width=100)

st.sidebar.markdown(
    """
    <div style="padding: 0.6rem 0rem 1rem 0rem;">
        <h2 style="color:white; margin-bottom:0;">PathWise AI</h2>
        <p style="color:#EAF6FA; font-size:0.86rem; line-height:1.4;">
            Student Risk Intelligence and Learning Pathway Recommendation System
        </p>
        <p style="color:#8ECAE6; font-size:0.75rem; margin-top:0.6rem;">
            University of Cape Coast
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Risk",
        "Tracker",
        "Support Areas",
        "Student Desk",
        "Chatbot"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    """
    <p style="font-size:0.8rem; color:#EAF6FA; line-height:1.5;">
    Built for academic support teams, programme coordinators, and student success units.
    </p>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1: HOME
# ============================================================

if page == "Home":

    total_students = len(data)
    high_risk = data[data["risk_level"] == "High Risk"].shape[0]
    medium_risk = data[data["risk_level"] == "Medium Risk"].shape[0]
    intervention_load = high_risk + medium_risk
    intervention_rate = intervention_load / total_students * 100
    avg_prob = data["at_risk_probability_pct"].mean()

    home_col1, home_col2 = st.columns([1.2, 8])

    with home_col1:
        if logo_path.exists():
            st.image(str(logo_path), width=145)

    with home_col2:
        st.markdown(
            """
            <div style="padding-top:0.45rem;">
                <div class="institution-label">University of Cape Coast</div>
                <div class="top-brand-title">PathWise AI</div>
                <div class="top-brand-subtitle">
                    University Student Learning Intelligence and Support Dashboard
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">STUDENT SUCCESS INTELLIGENCE PLATFORM</div>
            <div class="hero-title">Student Success Intelligence and Early Support</div>
            <div class="hero-subtitle">
                PathWise AI helps academic support teams identify students who may be at risk,
                track academic and engagement performance, detect learning support needs,
                and recommend targeted support actions before failure or withdrawal occurs.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        kpi_card("Student Records", format_int(total_students), "Learner profiles analysed")

    with c2:
        kpi_card("High Risk", format_int(high_risk), "Immediate support group")

    with c3:
        kpi_card("Medium Risk", format_int(medium_risk), "Targeted monitoring group")

    with c4:
        kpi_card("Support Load", format_int(intervention_load), f"{format_pct(intervention_rate)} require action")

    with c5:
        kpi_card("Mean Risk Score", format_pct(avg_prob), "Average predicted risk")

    st.markdown('<div class="section-title">What PathWise AI Does</div>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)

    with s1:
        st.markdown(
            """
            <div class="slide-card">
                <div class="slide-number">Capability 01</div>
                <div class="slide-heading">Predict academic risk</div>
                <div class="slide-text">
                The system estimates each student’s likelihood of being at academic risk using assessment,
                engagement, background, and course activity indicators.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:
        st.markdown(
            """
            <div class="slide-card">
                <div class="slide-number">Capability 02</div>
                <div class="slide-heading">Detect support areas</div>
                <div class="slide-text">
                It translates risk signals into understandable support areas such as academic performance,
                engagement, time management, preparation, and accessibility support.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with s3:
        st.markdown(
            """
            <div class="slide-card">
                <div class="slide-number">Capability 03</div>
                <div class="slide-heading">Recommend learning pathways</div>
                <div class="slide-text">
                Each student receives a recommended pathway that can guide advisors, tutors,
                and student success teams toward timely support.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Executive Risk Snapshot</div>', unsafe_allow_html=True)

    left, right = st.columns([1.1, 0.9])

    with left:
        risk_counts = data["risk_level"].value_counts().reset_index()
        risk_counts.columns = ["Risk Level", "Number of Students"]
        risk_counts["Risk Level"] = pd.Categorical(
            risk_counts["Risk Level"],
            categories=risk_order,
            ordered=True
        )
        risk_counts = risk_counts.sort_values("Risk Level")

        echarts_risk_bar(
            risk_counts,
            key="home_risk_bar"
        )

    with right:
        priority_counts = data["support_priority"].value_counts().reset_index()
        priority_counts.columns = ["Support Priority", "Number of Students"]

        echarts_donut(
            priority_counts,
            name_col="Support Priority",
            value_col="Number of Students",
            title="Student Support Priority Mix",
            key="home_support_donut"
        )

    st.markdown('<div class="section-title">Decision Workflow</div>', unsafe_allow_html=True)

    workflow_cols = st.columns(5)

    workflow_items = [
        ("Step 1", "Student Data", "Assessment records, prior education, and VLE activity are combined."),
        ("Step 2", "Risk Prediction", "The model estimates each student's academic risk probability."),
        ("Step 3", "Risk Banding", "Students are grouped into low, medium, or high-risk bands."),
        ("Step 4", "Support Areas", "The system identifies the likely barriers behind the risk."),
        ("Step 5", "Action Pathway", "A practical support pathway is recommended for the student.")
    ]

    for col, item in zip(workflow_cols, workflow_items):
        with col:
            st.markdown(
                f"""
                <div class="slide-card">
                    <div class="slide-number">{item[0]}</div>
                    <div class="slide-heading">{item[1]}</div>
                    <div class="slide-text">{item[2]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# PAGE 2: RISK
# ============================================================

elif page == "Risk":

    st.markdown('<div class="dashboard-title">Risk Intelligence</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dashboard-subtitle">
        Explore how academic risk varies across student background, performance, and digital engagement.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Risk Distribution by Student Characteristics</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        education_risk = (
            data.groupby(["highest_education", "risk_level"])
            .size()
            .reset_index(name="Number of Students")
        )

        fig = px.bar(
            education_risk,
            y="highest_education",
            x="Number of Students",
            color="risk_level",
            barmode="group",
            color_discrete_map=risk_colors,
            title="Risk Level by Previous Education"
        )
        fig.update_layout(
            yaxis_title="Previous Education",
            xaxis_title="Number of Students"
        )
        fig = clean_axis_labels(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        disability_risk = (
            data.groupby(["disability", "risk_level"])
            .size()
            .reset_index(name="Number of Students")
        )

        disability_risk["disability"] = disability_risk["disability"].replace({
            "N": "No reported disability",
            "Y": "Reported disability"
        })

        fig = px.bar(
            disability_risk,
            x="disability",
            y="Number of Students",
            color="risk_level",
            barmode="group",
            color_discrete_map=risk_colors,
            title="Risk Level by Disability Status"
        )
        fig.update_layout(
            xaxis_title="Disability Status",
            yaxis_title="Number of Students"
        )
        fig = clean_axis_labels(fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Academic and Engagement Risk Patterns</div>', unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        fig = px.box(
            data,
            x="risk_level",
            y="avg_score",
            color="risk_level",
            color_discrete_map=risk_colors,
            category_orders={"risk_level": risk_order},
            title="Assessment Performance by Risk Level"
        )
        fig.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Average Assessment Score"
        )
        fig = clean_axis_labels(fig)
        st.plotly_chart(fig, use_container_width=True)

    with c4:
        fig = px.box(
            data,
            x="risk_level",
            y="log_total_clicks",
            color="risk_level",
            color_discrete_map=risk_colors,
            category_orders={"risk_level": risk_order},
            title="Learning Platform Engagement by Risk Level"
        )
        fig.update_layout(
            xaxis_title="Risk Level",
            yaxis_title="Log Total VLE Clicks"
        )
        fig = clean_axis_labels(fig)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">Risk Score Distribution</div>', unsafe_allow_html=True)

    sample_data = data.sample(n=min(6000, len(data)), random_state=42)

    fig = px.scatter(
        sample_data,
        x="log_total_clicks",
        y="avg_score",
        color="risk_level",
        color_discrete_map=risk_colors,
        hover_data=[
            "id_student",
            "code_module",
            "highest_education",
            "at_risk_probability_pct"
        ],
        title="Relationship between Assessment Score and VLE Engagement"
    )
    fig.update_layout(
        xaxis_title="Log Total VLE Clicks",
        yaxis_title="Average Assessment Score"
    )
    fig.update_traces(marker=dict(size=7, opacity=0.55))
    fig = clean_axis_labels(fig)
    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# PAGE 3: TRACKER
# ============================================================

elif page == "Tracker":

    st.markdown('<div class="dashboard-title">Performance Tracker</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dashboard-subtitle">
        Interactive student performance monitoring based on assessment performance,
        VLE engagement, active learning days, assessment participation, and submission behaviour.
        </div>
        """,
        unsafe_allow_html=True
    )

    tracker_data = build_performance_tracker_data(data)

    c1, c2, c3 = st.columns(3)

    with c1:
        selected_module_tracker = st.selectbox(
            "Module",
            ["All"] + sorted(tracker_data["code_module"].dropna().unique().tolist()),
            key="tracker_module"
        )

    filtered_tracker = tracker_data.copy()

    if selected_module_tracker != "All":
        filtered_tracker = filtered_tracker[
            filtered_tracker["code_module"] == selected_module_tracker
        ]

    with c2:
        selected_band = st.selectbox(
            "Performance Band",
            ["All", "Weak Performance", "Developing Performance", "Strong Performance"],
            key="tracker_band"
        )

    if selected_band != "All":
        filtered_tracker = filtered_tracker[
            filtered_tracker["performance_band"].astype(str) == selected_band
        ]

    with c3:
        selected_student_tracker = st.selectbox(
            "Student ID",
            sorted(filtered_tracker["id_student"].unique().tolist()),
            key="tracker_student"
        )

    student_tracker = filtered_tracker[
        filtered_tracker["id_student"] == selected_student_tracker
    ].iloc[0]

    module_peer_group = tracker_data[
        tracker_data["code_module"] == student_tracker["code_module"]
    ].copy()

    student_position = module_peer_group[
        module_peer_group["id_student"] == selected_student_tracker
    ]

    if not student_position.empty:
        student_percentile = (
            module_peer_group["performance_index"].rank(pct=True)
            .loc[student_position.index[0]] * 100
        )
    else:
        student_percentile = 0

    st.markdown('<div class="section-title">Student Performance Snapshot</div>', unsafe_allow_html=True)

    p1, p2, p3, p4, p5 = st.columns(5)

    with p1:
        kpi_card(
            "Performance Index",
            format_pct(student_tracker["performance_index"]),
            "Composite academic progress score"
        )

    with p2:
        kpi_card(
            "Module Percentile",
            format_pct(student_percentile),
            "Relative to students in same module"
        )

    with p3:
        kpi_card(
            "Assessment Score",
            round(student_tracker["avg_score"], 1),
            "Average assessment score"
        )

    with p4:
        kpi_card(
            "VLE Clicks",
            format_int(student_tracker["total_clicks"]),
            "Total learning platform activity"
        )

    with p5:
        kpi_card(
            "Risk Probability",
            format_pct(student_tracker["at_risk_probability_pct"]),
            "Predicted academic risk"
        )

    st.markdown(
        f"""
        <div class="insight-box">
        <b>Performance Band:</b> {student_tracker["performance_band"]}
        <br><br>
        <b>Interpretation:</b> This tracker combines performance, engagement, activity consistency,
        assessment participation, and submission behaviour into one monitoring view.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">Interactive Performance Profile</div>', unsafe_allow_html=True)

    profile_df = pd.DataFrame({
        "Indicator": [
            "Assessment Score",
            "VLE Engagement",
            "Active Learning Days",
            "Assessment Participation",
            "Submission Discipline"
        ],
        "Selected Student": [
            student_tracker["score_index"],
            student_tracker["engagement_index"],
            student_tracker["active_days_index"],
            student_tracker["assessment_participation_index"],
            100 - student_tracker["late_submission_penalty"]
        ],
        "Module Average": [
            module_peer_group["score_index"].mean(),
            module_peer_group["engagement_index"].mean(),
            module_peer_group["active_days_index"].mean(),
            module_peer_group["assessment_participation_index"].mean(),
            100 - module_peer_group["late_submission_penalty"].mean()
        ]
    })

    echarts_line_compare(
        profile_df,
        x_col="Indicator",
        y_cols=["Selected Student", "Module Average"],
        title="Student Performance Profile Compared with Module Average",
        key="tracker_line_profile"
    )

    st.markdown('<div class="section-title">Performance and Risk Positioning</div>', unsafe_allow_html=True)

    scatter_sample = tracker_data.sample(n=min(7000, len(tracker_data)), random_state=42)

    echarts_scatter(
        scatter_sample,
        title="Performance Index versus Predicted Risk Probability",
        key="tracker_scatter_positioning"
    )

    st.markdown('<div class="section-title">Module Peer Benchmark</div>', unsafe_allow_html=True)

    benchmark_df = pd.DataFrame({
        "Metric": [
            "Average Assessment Score",
            "Total VLE Clicks",
            "Active Learning Days",
            "Assessment Count",
            "Late Submissions",
            "Performance Index"
        ],
        "Selected Student": [
            student_tracker["avg_score"],
            student_tracker["total_clicks"],
            student_tracker["active_days"],
            student_tracker["assessment_count"],
            student_tracker["late_submission_count"],
            student_tracker["performance_index"]
        ],
        "Module Average": [
            module_peer_group["avg_score"].mean(),
            module_peer_group["total_clicks"].mean(),
            module_peer_group["active_days"].mean(),
            module_peer_group["assessment_count"].mean(),
            module_peer_group["late_submission_count"].mean(),
            module_peer_group["performance_index"].mean()
        ]
    })

    benchmark_options = {
        "color": ["#219EBC", "#FFB703"],
        "title": {
            "text": "Selected Student versus Module Average",
            "left": "center",
            "textStyle": {"color": "#023047", "fontSize": 16, "fontWeight": "bold"}
        },
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "shadow"},
            "backgroundColor": "#FFFFFF",
            "borderColor": "#D9E2EC",
            "borderWidth": 1,
            "textStyle": {"color": "#023047"}
        },
        "legend": {
            "top": "9%",
            "textStyle": {"color": "#475569"}
        },
        "toolbox": {
            "show": True,
            "right": 15,
            "feature": {
                "saveAsImage": {"show": True},
                "dataView": {"show": True, "readOnly": True},
                "restore": {"show": True}
            }
        },
        "grid": {"left": "7%", "right": "5%", "top": "22%", "bottom": "18%"},
        "xAxis": {
            "type": "category",
            "data": benchmark_df["Metric"].astype(str).tolist(),
            "axisLabel": {"color": "#475569", "rotate": 20},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}}
        },
        "yAxis": {
            "type": "value",
            "axisLabel": {"color": "#475569"},
            "axisLine": {"lineStyle": {"color": "#CBD5E1"}},
            "splitLine": {"lineStyle": {"color": "#E2E8F0"}}
        },
        "series": [
            {
                "name": "Selected Student",
                "type": "bar",
                "data": benchmark_df["Selected Student"].round(2).tolist(),
                "barWidth": "32%",
                "itemStyle": {"borderRadius": [6, 6, 0, 0]}
            },
            {
                "name": "Module Average",
                "type": "bar",
                "data": benchmark_df["Module Average"].round(2).tolist(),
                "barWidth": "32%",
                "itemStyle": {"borderRadius": [6, 6, 0, 0]}
            }
        ],
        "animationDuration": 900,
        "animationEasing": "cubicOut"
    }

    render_echart(
        benchmark_options,
        height="480px",
        key="tracker_benchmark_bar"
    )

    st.markdown('<div class="section-title">Tracker-Based Support Signal</div>', unsafe_allow_html=True)

    if student_tracker["performance_index"] < 40 and student_tracker["at_risk_probability_pct"] >= 70:
        tracker_signal = "Critical support signal: weak performance and high academic risk."
        box_class = "warning-box"

    elif student_tracker["performance_index"] < 70 or student_tracker["at_risk_probability_pct"] >= 40:
        tracker_signal = "Monitoring signal: student requires targeted follow-up and structured support."
        box_class = "warning-box"

    else:
        tracker_signal = "Stable signal: student is currently performing within a healthy range."
        box_class = "success-box"

    st.markdown(
        f"""
        <div class="{box_class}">
        {tracker_signal}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PAGE 4: SUPPORT AREAS
# ============================================================

elif page == "Support Areas":

    st.markdown('<div class="dashboard-title">Support Areas</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dashboard-subtitle">
        Identify the most common student support areas behind predicted academic risk.
        </div>
        """,
        unsafe_allow_html=True
    )

    skill_gap_counts = create_skill_gap_table(data)
    skill_gap_counts["Display Label"] = skill_gap_counts["Skill Gap"].apply(clean_gap_label)

    st.markdown('<div class="section-title">Top Student Support Areas Detected</div>', unsafe_allow_html=True)

    support_chart_data = skill_gap_counts.head(10).sort_values("Number of Students")

    echarts_bar(
        support_chart_data,
        x_col="Number of Students",
        y_col="Display Label",
        title="Most Common Student Support Areas",
        x_name="Students",
        y_name="Support Area",
        color="#219EBC",
        horizontal=True,
        key="support_area_bar",
        height="520px"
    )

    st.markdown('<div class="section-title">Support Area Drill Down</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        gap_display_map = dict(zip(skill_gap_counts["Display Label"], skill_gap_counts["Skill Gap"]))

        selected_gap_display = st.selectbox(
            "Select support area",
            skill_gap_counts["Display Label"].tolist()
        )

        selected_gap = gap_display_map[selected_gap_display]

    with c2:
        selected_risk_level = st.selectbox(
            "Risk level filter",
            ["All", "Low Risk", "Medium Risk", "High Risk"]
        )

    with c3:
        selected_module = st.selectbox(
            "Module filter",
            ["All"] + sorted(data["code_module"].dropna().unique().tolist())
        )

    filtered_gap_data = data[
        data["skill_gaps"].fillna("").apply(
            lambda x: selected_gap in [gap.strip() for gap in str(x).split("|")]
        )
    ]

    if selected_risk_level != "All":
        filtered_gap_data = filtered_gap_data[
            filtered_gap_data["risk_level"] == selected_risk_level
        ]

    if selected_module != "All":
        filtered_gap_data = filtered_gap_data[
            filtered_gap_data["code_module"] == selected_module
        ]

    st.markdown(
        f"""
        <div class="insight-box">
        <b>{format_int(filtered_gap_data.shape[0])}</b> student records match the selected support area:
        <b>{selected_gap_display}</b>.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(
        filtered_gap_data[
            [
                "id_student",
                "code_module",
                "code_presentation",
                "risk_level",
                "support_priority",
                "at_risk_probability_pct",
                "skill_gaps"
            ]
        ].rename(columns={
            "id_student": "Student ID",
            "code_module": "Module",
            "code_presentation": "Presentation",
            "risk_level": "Risk Level",
            "support_priority": "Support Priority",
            "at_risk_probability_pct": "Risk Probability (%)",
            "skill_gaps": "Detected Support Areas"
        }).head(150),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 5: STUDENT DESK
# ============================================================

elif page == "Student Desk":

    st.markdown('<div class="dashboard-title">Student Desk</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dashboard-subtitle">
        Search a student record and review predicted risk, support areas, and recommended intervention pathway.
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        selected_module = st.selectbox(
            "Module",
            ["All"] + sorted(data["code_module"].dropna().unique().tolist())
        )

    filtered = data.copy()

    if selected_module != "All":
        filtered = filtered[filtered["code_module"] == selected_module]

    with c2:
        selected_risk = st.selectbox(
            "Risk Level",
            ["All", "Low Risk", "Medium Risk", "High Risk"]
        )

    if selected_risk != "All":
        filtered = filtered[filtered["risk_level"] == selected_risk]

    with c3:
        selected_student = st.selectbox(
            "Student ID",
            sorted(filtered["id_student"].unique().tolist())
        )

    student = filtered[filtered["id_student"] == selected_student].iloc[0]

    st.markdown('<div class="section-title">Student Risk Profile</div>', unsafe_allow_html=True)

    p1, p2, p3, p4, p5 = st.columns(5)

    with p1:
        kpi_card("Student ID", int(student["id_student"]), "Selected learner record")

    with p2:
        kpi_card("Module", student["code_module"], student["code_presentation"])

    with p3:
        kpi_card("Risk Probability", format_pct(student["at_risk_probability_pct"]), "Predicted risk score")

    with p4:
        kpi_card("Average Score", round(student["avg_score"], 1), "Assessment performance")

    with p5:
        kpi_card("Active Days", int(student["active_days"]), "Learning platform activity")

    st.markdown(
        f"""
        <div class="insight-box">
        <b>Risk Classification:</b> {risk_badge(student["risk_level"])}
        <br><br>
        <b>Support Priority:</b> {student["support_priority"]}
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([1, 1])

    with left:
        st.markdown('<div class="section-title">Academic and Engagement Profile</div>', unsafe_allow_html=True)

        profile_table = pd.DataFrame({
            "Indicator": [
                "Average Assessment Score",
                "Assessments Completed",
                "Late Submissions",
                "Total VLE Clicks",
                "Active Learning Days",
                "Previous Attempts",
                "Studied Credits",
                "Previous Education",
                "Disability Status"
            ],
            "Value": [
                round(student["avg_score"], 2),
                int(student["assessment_count"]),
                int(student["late_submission_count"]),
                int(student["total_clicks"]),
                int(student["active_days"]),
                int(student["num_of_prev_attempts"]),
                int(student["studied_credits"]),
                student["highest_education"],
                "Reported" if student["disability"] == "Y" else "Not reported"
            ]
        })

        st.dataframe(profile_table, use_container_width=True, hide_index=True)

    with right:
        st.markdown('<div class="section-title">Detected Support Areas</div>', unsafe_allow_html=True)

        skill_gaps = split_pipe_items(student["skill_gaps"])

        for gap in skill_gaps:
            cleaned_gap = clean_gap_label(gap)
            display_support_chip(cleaned_gap, student["risk_level"])

    st.markdown('<div class="section-title">Recommended Learning Pathway</div>', unsafe_allow_html=True)

    recommendations = split_pipe_items(student["recommended_pathway"])

    for i, recommendation in enumerate(recommendations, start=1):
        st.markdown(
            f"""
            <div class="insight-box">
            <b>Action {i}:</b> {recommendation}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Comparable Students</div>', unsafe_allow_html=True)

    similar = data[
        (data["risk_level"] == student["risk_level"]) &
        (data["code_module"] == student["code_module"]) &
        (data["id_student"] != student["id_student"])
    ]

    st.dataframe(
        similar[
            [
                "id_student",
                "code_module",
                "code_presentation",
                "risk_level",
                "at_risk_probability_pct",
                "support_priority",
                "skill_gaps"
            ]
        ].rename(columns={
            "id_student": "Student ID",
            "code_module": "Module",
            "code_presentation": "Presentation",
            "risk_level": "Risk Level",
            "at_risk_probability_pct": "Risk Probability (%)",
            "support_priority": "Support Priority",
            "skill_gaps": "Support Areas"
        }).head(30),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# PAGE 6: CHATBOT
# ============================================================

elif page == "Chatbot":

    st.markdown('<div class="dashboard-title">Student Success Chatbot</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="dashboard-subtitle">
        Ask questions about student risk, support priorities, support areas, module summaries,
        and individual student recommendations.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="insight-box">
        This chatbot answers questions using the dashboard dataset. It is designed for academic support teams
        who need quick summaries without manually searching through tables.
        </div>
        """,
        unsafe_allow_html=True
    )

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": (
                    "Welcome. I am the PathWise Student Success Assistant. "
                    "I can summarize student risk, explain support areas, review module-level patterns, "
                    "and retrieve student-specific recommendations from the dashboard data."
                )
            }
        ]

    for message in st.session_state.chat_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], unsafe_allow_html=False)

    user_prompt = st.chat_input(
        "Ask about student risk, support priorities, support areas, or a student ID"
    )

    if user_prompt:
        st.session_state.chat_messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(user_prompt, unsafe_allow_html=False)

        response = chatbot_response(user_prompt, data)

        st.session_state.chat_messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response, unsafe_allow_html=False)

    st.markdown('<div class="section-title">Example Questions</div>', unsafe_allow_html=True)

    example_cols = st.columns(3)

    with example_cols[0]:
        st.markdown(
            """
            <div class="insight-box">
            <b>Risk questions</b><br>
            How many students are high risk?<br>
            What is the average risk probability?<br>
            Show support priority summary
            </div>
            """,
            unsafe_allow_html=True
        )

    with example_cols[1]:
        st.markdown(
            """
            <div class="insight-box">
            <b>Student questions</b><br>
            Show student 6516<br>
            What support does student 30268 need?<br>
            Show student 23698
            </div>
            """,
            unsafe_allow_html=True
        )

    with example_cols[2]:
        st.markdown(
            """
            <div class="insight-box">
            <b>Module and support questions</b><br>
            Summarize module AAA<br>
            What are the top support areas?<br>
            Which students need immediate support?
            </div>
            """,
            unsafe_allow_html=True
        )
