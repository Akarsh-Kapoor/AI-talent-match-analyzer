import pyodbc


# SQL SERVER CONNECTION

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=MSI\sqlexpress;"
    "DATABASE=TalentAnalyzer;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()


# SAVE ANALYSIS

def save_analysis(
    candidate_name,
    score,
    matched,
    missing,
    summary
):

    try:

        # Remove old entry for same candidate

        cursor.execute(
            """
            DELETE FROM CandidateAnalysis
            WHERE CandidateName = ?
            """,
            candidate_name
        )

        conn.commit()

        # Insert latest analysis

        cursor.execute(
            """
            INSERT INTO CandidateAnalysis
            (
                CandidateName,
                MatchScore,
                MatchedSkills,
                MissingSkills,
                CandidateSummary
            )
            VALUES
            (?, ?, ?, ?, ?)
            """,
            candidate_name,
            score,
            ", ".join(matched),
            ", ".join(missing),
            summary
        )

        conn.commit()

        print(
            f"{candidate_name} saved successfully."
        )

    except Exception as e:

        print(
            f"Database Error: {e}"
        )


# OPTIONAL: FETCH ALL RECORDS

def get_all_candidates():

    cursor.execute(
        """
        SELECT *
        FROM CandidateAnalysis
        ORDER BY MatchScore DESC
        """
    )

    rows = cursor.fetchall()

    return rows


# OPTIONAL: FETCH SINGLE CANDIDATE

def get_candidate(
    candidate_name
):

    cursor.execute(
        """
        SELECT *
        FROM CandidateAnalysis
        WHERE CandidateName = ?
        """,
        candidate_name
    )

    row = cursor.fetchone()

    return row
    
def reset_table():

    cursor.execute(
        """
        DELETE FROM CandidateAnalysis
        """
    )

    conn.commit()

    cursor.execute(
        """
        DBCC CHECKIDENT
        (
            'CandidateAnalysis',
            RESEED,
            0
        )
        """
    )

    conn.commit()