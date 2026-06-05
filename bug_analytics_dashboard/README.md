
# Bug Analytics Executive Dashboard

## Overview
This project analyzes Bugasura CSV exports and generates executive-level analytics dashboards.

Designed to look like a real-world analytics solution built by a mid-level Data Analyst.

## Features
- Automatic CSV detection from `/data`
- Executive KPI dashboard
- Severity trends
- QA productivity analysis
- Engineering risk analysis
- Business impact insights
- Sprint quality indicators
- Defect distribution
- Interactive visualizations

## Setup Guide

### Step 1 — Install Python
Download Python 3.11+ from:
https://www.python.org/downloads/

IMPORTANT:
Enable:
[x] Add Python to PATH

---

### Step 2 — Extract Project
Unzip the downloaded project folder.

---

### Step 3 — Open Terminal

Inside project folder:
Shift + Right Click → Open PowerShell here

---

### Step 4 — Install Requirements

Run:

pip install -r requirements.txt

---

### Step 5 — Add CSV Files

Place all Bugasura exports inside:

data/

Example:

data/
    sprint.csv
    live_support.csv

---

### Step 6 — Run Dashboard

Run:

streamlit run dashboard/app.py

---

### Step 7 — Open Browser

Streamlit will automatically open:

http://localhost:8501

---

## Interview Talking Points

### Executive Insights
- Which modules generate maximum business risk
- Which severity level dominates releases
- QA efficiency trends
- Defect leakage indicators
- Product stability metrics
- Release readiness analysis

### CEO-Level Narrative
- Areas causing customer-impacting defects
- Potential delivery bottlenecks
- Teams/modules requiring investment
- Trend of critical issues over time

### BA-Level Narrative
- Frequently impacted workflows
- User journey disruptions
- Functional instability hotspots

### Engineering Narrative
- Root-cause concentration
- Reopen-risk indicators
- Regression-heavy modules

