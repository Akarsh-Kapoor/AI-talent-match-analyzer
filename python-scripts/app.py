from database import (
    save_analysis,
    reset_table
)
from report_generator import (
    generate_report
)
from database import save_analysis

import streamlit as st
import json
import pandas as pd

from skill_extractor import (
    extract_resume_text,
    full_candidate_analysis
)

# PAGE CONFIG

st.set_page_config(
    page_title="AI Talent Intelligence Platform",
    page_icon="🤖",
    layout="wide"
)

# TITLE

st.title("🤖 AI Talent Intelligence Platform")

st.markdown(
    """
    Upload multiple resumes and compare them against a Job Description using AI.
    """
)

# MULTIPLE RESUME UPLOAD

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# JOB DESCRIPTION

jd = st.text_area(
    "Paste Job Description",
    height=200
)

# MAIN LOGIC

if uploaded_files and jd:

    if st.button("Analyze Candidates"):

        reset_table()
        
        results = []

        with st.spinner("Analyzing resumes..."):

            for file in uploaded_files:

                try:
                    resume_text = extract_resume_text(
                            uploaded_file
                        )

                    analysis = full_candidate_analysis(
                                resume_text,
                                jd
                            )
                    import json
                    data = json.loads(
                        analysis
                    )

                    save_analysis(
                        candidate_name=data["candidate_name"],
                        score=data["match_score"],
                        matched=data["matched_skills"],
                        missing=data["missing_skills"],
                        summary=data["candidate_summary"]
                    )

                    results.append(
                        {
                                "Candidate": data.get(
                                "candidate_name",
                                file.name
                            ),
                            "Match Score": data.get(
                                "match_score",
                                0
                            ),
                            "Matched Skills": data.get(
                                "matched_skills",
                                []
                            ),
                            "Missing Skills": data.get(
                                "missing_skills",
                                []
                            ),
                            "Learning Recommendations": data.get(
                                "learning_recommendations",
                                []
                            ),
                            "Summary": data.get(
                                "candidate_summary",
                                ""
                            )
                        }
                    )

                except Exception as e:

                    st.error(
                        f"Error processing {file.name}"
                    )

                    st.exception(e)

        # RANKING TABLE

        if results:

            df = pd.DataFrame(results)

            df = df.sort_values(
                by="Match Score",
                ascending=False
            )

            df.insert(
                0,
                "Rank",
                range(
                    1,
                    len(df) + 1
                )
            )

            st.divider()

            st.subheader(
                "🏆 Candidate Rankings"
            )

            st.dataframe(
                df[
                    [
                        "Rank",
                        "Candidate",
                        "Match Score"
                    ]
                ],
                use_container_width=True
            )

            st.divider()

            st.subheader(
                "📋 Candidate Details"
            )

            for row in df.to_dict(
                orient="records"
            ):

                with st.expander(
                    f"#{row['Rank']} - {row['Candidate']} ({row['Match Score']}%)"
                ):

                    # MATCH SCORE

                    st.metric(
                        "Match Score",
                        f"{row['Match Score']}%"
                    )

                    st.progress(
                        float(
                            row["Match Score"]
                        ) / 100
                    )

                    # MATCHED SKILLS

                    st.subheader(
                        "✅ Matched Skills"
                    )

                    matched = row[
                        "Matched Skills"
                    ]

                    if matched:

                        for skill in matched:

                            st.success(
                                str(skill)
                            )

                    else:

                        st.warning(
                            "No matched skills found."
                        )

                    # MISSING SKILLS

                    st.subheader(
                        "❌ Missing Skills"
                    )

                    missing = row[
                        "Missing Skills"
                    ]

                    if missing:

                        for skill in missing:

                            st.error(
                                str(skill)
                            )

                    else:

                        st.success(
                            "No missing skills."
                        )

                    # LEARNING RECOMMENDATIONS

                    st.subheader(
                        "📚 Learning Recommendations"
                    )

                    recommendations = row[
                        "Learning Recommendations"
                    ]

                    if recommendations:

                        for rec in recommendations:

                            if isinstance(rec, dict):

                                skill = rec.get(
                                    "skill",
                                    "Unknown Skill"
                                )

                                st.markdown(
                                    f"### 🎯 {skill}"
                                )

                                for course in rec.get(
                                    "recommendations",
                                    []
                                ):

                                    st.info(course)

                            else:

                                st.info(str(rec))

                    else:

                        st.success(
                            "No recommendations needed."
                        )

                    # SUMMARY

                    st.subheader(
                        "📝 Candidate Summary"
                    )

                    st.info(
                        row["Summary"]
                    )
                    pdf_file = generate_report(
                        row
                    )

                    with open(
                        pdf_file,
                        "rb"
                    ) as file:

                        st.download_button(
                            label="📄 Download Report",
                            data=file,
                            file_name=pdf_file,
                            mime="application/pdf"
                        )
