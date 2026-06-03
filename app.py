

# ============================================================
# PATHWISE AI: PERSONALIZED LEARNING PATH RECOMMENDER
# STREAMLIT DASHBOARD
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PathWise AI",
    page_icon="🎓",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    data = pd.read_csv("processed_data/recommendation_ready_data.csv")
    return data


data = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎓 PathWise AI")
st.sidebar.write("Personalized Learning Path Recommender")

page = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Risk Analytics",
        "Skill Gap Analysis",
        "Student Recommendation",
        "About the Project"
    ]
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def format_probability(x):
    return f"{x * 100:.2f}%"


def split_text_items(text):
    if pd.isna(text):
        return []
    return [item.strip() for item in str(text).split("|")]


# ============================================================
# PAGE 1: OVERVIEW
# ============================================================

if page == "Overview":

    st.title("🎓 PathWise AI: University Student Learning Path Recommender")

    st.markdown(
        """
        PathWise AI is a machine learning-based decision-support dashboard that predicts student academic risk,
        identifies likely learning gaps, and recommends personalized support pathways for university students.
        """
    )

    total_students = data.shape[0]
    high_risk_students = data[data["risk_level"] == "High Risk"].shape[0]
    medium_risk_students = data[data["risk_level"] == "Medium Risk"].shape[0]
    low_risk_students = data[data["risk_level"] == "Low Risk"].shape[0]

    avg_risk_probability = data["at_risk_probability"].mean()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Student Records", f"{total_students:,}")
    col2.metric("High Risk", f"{high_risk_students:,}")
    col3.metric("Medium Risk", f"{medium_risk_students:,}")
    col4.metric("Low Risk", f"{low_risk_students:,}")
    col5.metric("Average Risk Probability", format_probability(avg_risk_probability))

    st.divider()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Predicted Risk Level Distribution")

        risk_counts = data["risk_level"].value_counts().reset_index()
        risk_counts.columns = ["Risk Level", "Number of Students"]

        risk_order = ["Low Risk", "Medium Risk", "High Risk"]
        risk_counts["Risk Level"] = pd.Categorical(
            risk_counts["Risk Level"],
            categories=risk_order,
            ordered=True
        )
        risk_counts = risk_counts.sort_values("Risk Level")

        fig = px.bar(
            risk_counts,
            x="Risk Level",
            y="Number of Students",
            text="Number of Students",
            title="Distribution of Predicted Student Risk Levels"
        )
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        st.subheader("Support Priority Distribution")

        priority_counts = data["support_priority"].value_counts().reset_index()
        priority_counts.columns = ["Support Priority", "Number of Students"]

        fig = px.pie(
            priority_counts,
            names="Support Priority",
            values="Number of Students",
            title="Support Priority Summary",
            hole=0.35
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Project Logic")

    st.markdown(
        """
        **The system follows a simple decision-support workflow:**

        Student academic records and VLE engagement data  
        ↓  
        Machine learning risk prediction  
        ↓  
        Risk level classification  
        ↓  
        Skill gap identification  
        ↓  
        Personalized learning pathway recommendation
        """
    )


# ============================================================
# PAGE 2: RISK ANALYTICS
# ============================================================

elif page == "Risk Analytics":

    st.title("📊 Risk Analytics")

    st.markdown(
        """
        This page explores how predicted risk varies across student characteristics,
        academic performance, and engagement indicators.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Risk Level by Previous Education")

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
            title="Risk Level by Previous Education"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Risk Level by Disability Status")

        disability_risk = (
            data.groupby(["disability", "risk_level"])
            .size()
            .reset_index(name="Number of Students")
        )

        fig = px.bar(
            disability_risk,
            x="disability",
            y="Number of Students",
            color="risk_level",
            barmode="group",
            title="Risk Level by Disability Status"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Assessment Score by Risk Level")

        fig = px.box(
            data,
            x="risk_level",
            y="avg_score",
            title="Average Assessment Score by Risk Level",
            category_orders={"risk_level": ["Low Risk", "Medium Risk", "High Risk"]}
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.subheader("VLE Engagement by Risk Level")

        if "log_total_clicks" not in data.columns:
            data["log_total_clicks"] = np.log1p(data["total_clicks"])

        fig = px.box(
            data,
            x="risk_level",
            y="log_total_clicks",
            title="Log Total VLE Clicks by Risk Level",
            category_orders={"risk_level": ["Low Risk", "Medium Risk", "High Risk"]}
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.subheader("Assessment Score and VLE Engagement")

    sample_data = data.sample(n=min(5000, len(data)), random_state=42).copy()

    if "log_total_clicks" not in sample_data.columns:
        sample_data["log_total_clicks"] = np.log1p(sample_data["total_clicks"])

    fig = px.scatter(
        sample_data,
        x="log_total_clicks",
        y="avg_score",
        color="risk_level",
        hover_data=["id_student", "code_module", "highest_education"],
        title="Sampled Relationship between Assessment Score and VLE Engagement"
    )
    st.plotly_chart(fig, use_container_width=True)


# ============================================================
# PAGE 3: SKILL GAP ANALYSIS
# ============================================================

elif page == "Skill Gap Analysis":

    st.title("🧩 Skill Gap Analysis")

    st.markdown(
        """
        This page summarizes the main learning gaps detected by the recommendation engine.
        """
    )

    skill_gap_series = (
        data["skill_gaps"]
        .dropna()
        .str.split(" | ")
        .explode()
        .str.strip()
    )

    skill_gap_counts = skill_gap_series.value_counts().reset_index()
    skill_gap_counts.columns = ["Skill Gap", "Number of Students"]

    st.subheader("Top Detected Skill Gaps")

    fig = px.bar(
        skill_gap_counts.head(10),
        y="Skill Gap",
        x="Number of Students",
        orientation="h",
        title="Top 10 Detected Student Skill Gaps"
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        selected_gap = st.selectbox(
            "Select a skill gap to view affected students",
            skill_gap_counts["Skill Gap"].tolist()
        )

    with col2:
        selected_risk_level = st.selectbox(
            "Filter by risk level",
            ["All", "Low Risk", "Medium Risk", "High Risk"]
        )

    filtered_gap_data = data[data["skill_gaps"].str.contains(selected_gap, na=False)]

    if selected_risk_level != "All":
        filtered_gap_data = filtered_gap_data[
            filtered_gap_data["risk_level"] == selected_risk_level
        ]

    st.write(f"Students with **{selected_gap}**: {filtered_gap_data.shape[0]:,}")

    st.dataframe(
        filtered_gap_data[
            [
                "id_student",
                "code_module",
                "code_presentation",
                "risk_level",
                "support_priority",
                "at_risk_probability",
                "skill_gaps"
            ]
        ].head(100),
        use_container_width=True
    )


# ============================================================
# PAGE 4: STUDENT RECOMMENDATION
# ============================================================

elif page == "Student Recommendation":

    st.title("🎯 Individual Student Recommendation")

    st.markdown(
        """
        Use this page to search for a student and view their predicted risk level,
        detected learning gaps, and personalized support pathway.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        module_options = ["All"] + sorted(data["code_module"].dropna().unique().tolist())
        selected_module = st.selectbox("Select Module", module_options)

    filtered_data = data.copy()

    if selected_module != "All":
        filtered_data = filtered_data[filtered_data["code_module"] == selected_module]

    with col2:
        risk_options = ["All", "Low Risk", "Medium Risk", "High Risk"]
        selected_risk = st.selectbox("Select Risk Level", risk_options)

    if selected_risk != "All":
        filtered_data = filtered_data[filtered_data["risk_level"] == selected_risk]

    with col3:
        student_options = sorted(filtered_data["id_student"].unique().tolist())
        selected_student = st.selectbox("Select Student ID", student_options)

    student_record = filtered_data[filtered_data["id_student"] == selected_student].iloc[0]

    st.divider()

    st.subheader("Student Risk Profile")

    col_a, col_b, col_c, col_d = st.columns(4)

    col_a.metric("Student ID", int(student_record["id_student"]))
    col_b.metric("Module", student_record["code_module"])
    col_c.metric("Risk Level", student_record["risk_level"])
    col_d.metric("At-Risk Probability", format_probability(student_record["at_risk_probability"]))

    st.write("**Support Priority:**", student_record["support_priority"])
    st.write("**Predicted Label:**", student_record["predicted_label"])

    st.divider()

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Academic and Engagement Indicators")

        indicator_table = pd.DataFrame({
            "Indicator": [
                "Average Assessment Score",
                "Assessment Count",
                "Late Submissions",
                "Total VLE Clicks",
                "Active Learning Days",
                "Previous Attempts",
                "Studied Credits",
                "Previous Education",
                "Disability Status"
            ],
            "Value": [
                round(student_record["avg_score"], 2),
                int(student_record["assessment_count"]),
                int(student_record["late_submission_count"]),
                int(student_record["total_clicks"]),
                int(student_record["active_days"]),
                int(student_record["num_of_prev_attempts"]),
                int(student_record["studied_credits"]),
                student_record["highest_education"],
                student_record["disability"]
            ]
        })

        st.dataframe(indicator_table, use_container_width=True)

    with col_right:
        st.subheader("Detected Skill Gaps")

        skill_gaps = split_text_items(student_record["skill_gaps"])

        for gap in skill_gaps:
            st.warning(gap)

    st.divider()

    st.subheader("Recommended Learning Pathway")

    recommendations = split_text_items(student_record["recommended_pathway"])

    for idx, rec in enumerate(recommendations, start=1):
        st.write(f"**{idx}.** {rec}")

    st.divider()

    st.subheader("Similar Students in Same Risk Level")

    similar_students = data[
        (data["risk_level"] == student_record["risk_level"]) &
        (data["code_module"] == student_record["code_module"]) &
        (data["id_student"] != student_record["id_student"])
    ]

    st.dataframe(
        similar_students[
            [
                "id_student",
                "code_module",
                "code_presentation",
                "risk_level",
                "at_risk_probability",
                "support_priority",
                "skill_gaps"
            ]
        ].head(20),
        use_container_width=True
    )


# ============================================================
# PAGE 5: ABOUT THE PROJECT
# ============================================================

elif page == "About the Project":

    st.title("ℹ️ About PathWise AI")

    st.markdown(
        """
        ## Project Summary

        **PathWise AI** is a personalized learning path recommender for university students.
        It uses machine learning to predict academic risk and recommends targeted support pathways.

        ## Problem

        Universities often identify struggling students too late, after poor performance,
        course failure, or withdrawal has already occurred.

        ## Solution

        PathWise AI uses student academic records, assessment activity, previous education,
        and VLE engagement to classify students into low, medium, and high-risk groups.

        ## Model Used

        Three models were trained and compared:

        - Logistic Regression
        - Random Forest
        - Gradient Boosting

        The best-performing model was selected based on ROC-AUC and recall.

        ## Recommendation Logic

        The system identifies learning gaps such as:

        - Academic Performance Gap
        - Low Engagement Gap
        - Assessment Participation Gap
        - Time Management Gap
        - Academic Preparation Gap
        - Accessibility Support Gap

        It then recommends personalized learning pathways, including:

        - Foundation revision modules
        - Tutor support
        - Weekly VLE engagement targets
        - Academic advising
        - Accessibility support
        - Time management resources

        ## Deployment Note

        The model was first trained on full academic and engagement records to understand key risk patterns.
        For real-time university use, it can be restricted to early-semester data so support teams can identify
        and assist students before failure or withdrawal occurs.
        """
    )
