import sqlite3
import pandas as pd


conn = sqlite3.connect(
    "talent_analyzer.db",
    check_same_thread=False
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS CandidateAnalysis (
    CandidateID INTEGER PRIMARY KEY AUTOINCREMENT,
    CandidateName TEXT,
    MatchScore INTEGER,
    MatchedSkills TEXT,
    MissingSkills TEXT,
    CandidateSummary TEXT,
    AnalysisDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


conn.commit()


def reset_table():

    cursor.execute(
        "DELETE FROM CandidateAnalysis"
    )

    cursor.execute(
        "DELETE FROM sqlite_sequence WHERE name='CandidateAnalysis'"
    )

    conn.commit()


def save_analysis(
    candidate_name,
    match_score,
    matched_skills,
    missing_skills,
    summary
):

    cursor.execute("""
    INSERT INTO CandidateAnalysis (
        CandidateName,
        MatchScore,
        MatchedSkills,
        MissingSkills,
        CandidateSummary
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        candidate_name,
        match_score,
        matched_skills,
        missing_skills,
        summary
    ))

    conn.commit()


def fetch_all_candidates():

    query = """
    SELECT *
    FROM CandidateAnalysis
    ORDER BY MatchScore DESC
    """

    return pd.read_sql(
        query,
        conn
    )
