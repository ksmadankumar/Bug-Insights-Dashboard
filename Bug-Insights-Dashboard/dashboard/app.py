
import streamlit as st
import pandas as pd
import plotly.express as px
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))

from data_loader import load_bug_data

st.set_page_config(
    page_title="Executive Bug Analytics Dashboard",
    layout="wide"
)

st.title("Executive Bug Analytics Dashboard")
st.caption("Portfolio-grade QA & Product Analytics")

try:
    df = load_bug_data("data")
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

st.sidebar.header("Filters")

severity_filter = st.sidebar.multiselect(
    "Severity",
    options=sorted(df["Severity"].dropna().unique()),
    default=sorted(df["Severity"].dropna().unique())
)

status_filter = st.sidebar.multiselect(
    "Status",
    options=sorted(df["Issue Status"].dropna().unique()),
    default=sorted(df["Issue Status"].dropna().unique())
)

filtered = df[
    df["Severity"].isin(severity_filter) &
    df["Issue Status"].isin(status_filter)
]

critical_count = len(filtered[filtered["Severity"].astype(str).str.contains("CRITICAL", case=False, na=False)])
high_count = len(filtered[filtered["Severity"].astype(str).str.contains("HIGH", case=False, na=False)])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Bugs", len(filtered))
col2.metric("Critical Bugs", critical_count)
col3.metric("High Severity", high_count)
col4.metric("Unique Testers", filtered["Tester"].nunique())

st.markdown("---")

st.subheader("Severity Distribution")

fig1 = px.pie(
    filtered,
    names="Severity",
    title="Bug Severity Breakdown"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Bug Reporting Trend")

if "Reported Date" in filtered.columns:
    trend = (
        filtered.groupby(filtered["Reported Date"].dt.date)
        .size()
        .reset_index(name="Bug Count")
    )

    fig2 = px.line(
        trend,
        x="Reported Date",
        y="Bug Count",
        markers=True,
        title="Daily Bug Reporting Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Top Impact Areas")

if "Tags" in filtered.columns:
    tags = (
        filtered["Tags"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
        .head(10)
        .reset_index()
    )

    tags.columns = ["Tag", "Count"]

    fig3 = px.bar(
        tags,
        x="Tag",
        y="Count",
        title="Top Risk Areas"
    )

    st.plotly_chart(fig3, use_container_width=True)

st.subheader("Tester Productivity")

if "Tester" in filtered.columns:
    tester = (
        filtered["Tester"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    tester.columns = ["Tester", "Bug Count"]

    fig4 = px.bar(
        tester,
        x="Tester",
        y="Bug Count",
        title="Top Testers by Bug Count"
    )

    st.plotly_chart(fig4, use_container_width=True)

st.subheader("Executive Insights")

insights = []

if critical_count > 100:
    insights.append("High volume of CRITICAL defects indicates elevated production risk.")

if high_count > critical_count:
    insights.append("HIGH severity defects dominate releases, suggesting incomplete regression coverage.")

if filtered["Tester"].nunique() < 3:
    insights.append("Testing ownership concentration risk detected due to limited tester diversity.")

if "Tags" in filtered.columns:
    top_tag = (
        filtered["Tags"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .value_counts()
    )

    if len(top_tag) > 0:
        insights.append(f"Most unstable functional area: {top_tag.index[0]}.")

if not insights:
    insights.append("System quality appears operationally stable based on current dataset.")

for i in insights:
    st.info(i)

st.markdown("---")

