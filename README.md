# 🚀 AI Talent Intelligence Platform

An end-to-end AI-powered recruitment analytics platform that automates resume screening, candidate-job matching, skill gap analysis, learning recommendations, PDF report generation, and hiring insights visualization.

---

## 📌 Project Overview

Recruiters often spend significant time manually reviewing resumes and comparing candidates against job requirements.

This platform streamlines the process by:

- Parsing resumes automatically
- Extracting technical skills using Gemini AI
- Matching candidates against Job Descriptions
- Identifying missing skills and skill gaps
- Recommending personalized learning paths
- Ranking candidates based on suitability
- Storing analysis results in SQL Server
- Generating downloadable PDF reports
- Visualizing hiring insights through Power BI

---

## 🏗️ System Architecture

![Architecture](screenshots/data-architecture.png)

### Workflow

Resume PDFs
→ Streamlit Application
→ Gemini AI Skill Analysis
→ Candidate Matching Engine
→ SQL Server Database
→ Power BI Dashboard
→ PDF Report Generation

---

## ✨ Key Features

### 🤖 AI Resume Analysis
- PDF resume parsing
- Skill extraction using Gemini AI
- Candidate profiling

### 🎯 Candidate Matching
- Job Description comparison
- Match score calculation
- Skill gap detection

### 📚 Learning Recommendations
- Personalized upskilling suggestions
- Missing skill analysis
- Career development guidance

### 🏆 Candidate Ranking
- Multi-candidate comparison
- Rank-based evaluation
- Recruiter-friendly insights

### 🗄️ SQL Server Integration
- Persistent candidate storage
- Historical analysis tracking
- Dashboard-ready data model

### 📊 Power BI Dashboard
- Candidate ranking visualization
- Match score analytics
- Skill gap trends
- Hiring insights

### 📄 Automated Report Generation
- Candidate assessment reports
- PDF export functionality
- Recruiter-ready summaries

---

# 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| AI Engine | Gemini AI |
| Programming Language | Python |
| Database | SQL Server (SSMS) |
| Analytics | Power BI |
| PDF Processing | PyPDF |
| Reporting | ReportLab |
| Data Handling | Pandas |
| Connectivity | PyODBC |

---

# 📁 Repository Structure

```text
AI-Talent-Match-Analyzer
│
├── insights-dashboard/
│
├── python-scripts/
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── report_generator.py
│   └── skill_extractor.py
│
├── screenshots/
│   ├── home-page.png
│   ├── home-page-with-details.png
│   ├── candidate-rankings.png
│   ├── analysis-matched-skills.png
│   ├── analysis-missing-skills.png
│   ├── analysis-learning-recommendations.png
│   ├── analysis-candidate-summary.png
│   ├── generated-pdf-report.png
│   ├── sql-server-data.png
│   ├── dashboard-insights.png
│   └── data-architecture.png
│
├── sql-db-script/
│   └── database-script.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📷 Application Screenshots

## Home Page

![Home Page](screenshots/home-page-with-details.png)

---

## Candidate Ranking

![Candidate Rankings](screenshots/candidate-rankings.png)

---

## Matched Skills Analysis

![Matched Skills](screenshots/analysis-matched-skills.png)

---

## Missing Skills Analysis

![Missing Skills](screenshots/analysis-missing-skills.png)

---

## Learning Recommendations

![Learning Recommendations](screenshots/analysis-learning-recommendations.png)

---

## Candidate Summary

![Candidate Summary](screenshots/analysis-candidate-summary.png)

---

## SQL Server Data Storage

![SQL Server Data](screenshots/sql-server-data.png)

---

## Power BI Dashboard

![Power BI Dashboard](screenshots/dashboard-insights.png)

---

## Generated PDF Report

![PDF Report](screenshots/generated-pdf-report.png)

---

# ⚙️ Installation Guide

## Clone Repository

```bash
git clone https://github.com/Akarsh-Kapoor/AI-talent-match-analyzer.git
cd AI-talent-match-analyzer
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Setup SQL Server

Run:

```sql
sql-db-script/database-script.sql
```

inside SQL Server Management Studio.

## Run Application

```bash
streamlit run python-scripts/app.py
```

---

# 📈 Power BI Dashboard Metrics

The dashboard provides:

- Total Candidates
- Average Match Score
- Highest Match Score
- Candidate Ranking Distribution
- Skill Gap Analysis
- Candidate Performance Insights

---

# 🎯 Business Value

This platform helps recruiters:

- Reduce manual screening effort
- Improve hiring efficiency
- Identify skill gaps quickly
- Compare candidates objectively
- Generate recruiter-ready reports
- Make data-driven hiring decisions

---

# 🔮 Future Enhancements

- Resume Batch Processing
- ATS Integration
- Interview Recommendation Engine
- Candidate Shortlisting Automation
- Resume Similarity Detection
- Real-Time Dashboard Refresh
- Cloud Deployment (Azure/AWS)

---

Note : Power BI dashboard source file intentionally excluded to protect sample candidate data.

---

## 🌟 About Me

Hi, I'm **Akarsh Kapoor** — a Data & Analytics professional passionate about solving business problems through technology, automation, and data-driven insights.
My interests include:

- Data Analytics & Business Intelligence
- SQL & Database Management
- Python Automation
- Cloud Technologies (AWS)
- AI & Data-Driven Solutions

Let's connect!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akarsh-kapoor/)


---
