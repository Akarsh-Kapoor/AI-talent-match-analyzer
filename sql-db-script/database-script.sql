/* =========================================================
   AI TALENT INTELLIGENCE PLATFORM
   COMPLETE DATABASE SETUP SCRIPT
   ========================================================= */

-- CREATE DATABASE

IF DB_ID('TalentAnalyzer') IS NULL
BEGIN
    CREATE DATABASE TalentAnalyzer;
END
GO

USE TalentAnalyzer;
GO


/* =========================================================
   CREATE TABLE
   ========================================================= */

IF OBJECT_ID('CandidateAnalysis', 'U') IS NULL
BEGIN

    CREATE TABLE CandidateAnalysis
    (
        CandidateID INT IDENTITY(1,1) PRIMARY KEY,

        CandidateName VARCHAR(200) NOT NULL,

        MatchScore INT NOT NULL,

        MatchedSkills VARCHAR(MAX),

        MissingSkills VARCHAR(MAX),

        CandidateSummary VARCHAR(MAX),

        AnalysisDate DATETIME DEFAULT GETDATE()
    );

END
GO


/* =========================================================
   CREATE POWER BI VIEW
   ========================================================= */

IF OBJECT_ID('vw_CandidateAnalytics', 'V') IS NOT NULL
DROP VIEW vw_CandidateAnalytics;
GO

CREATE VIEW vw_CandidateAnalytics
AS

SELECT

    CandidateID,

    CandidateName,

    MatchScore,

    MatchedSkills,

    MissingSkills,

    CandidateSummary,

    AnalysisDate,

    CASE
        WHEN MatchScore >= 80
            THEN 'Strong Match'

        WHEN MatchScore >= 60
            THEN 'Potential Match'

        ELSE 'Not Recommended'
    END AS Recommendation

FROM CandidateAnalysis;
GO


/* =========================================================
   RESET TABLE + RESET IDENTITY
   RUN WHENEVER YOU WANT A FRESH START
   ========================================================= */

-- DELETE FROM CandidateAnalysis;

-- DBCC CHECKIDENT
-- (
--     'CandidateAnalysis',
--     RESEED,
--     0
-- );


/* =========================================================
   SAMPLE ANALYTICS QUERIES
   ========================================================= */

-- TOTAL CANDIDATES

SELECT
    COUNT(*) AS TotalCandidates
FROM CandidateAnalysis;


-- AVERAGE MATCH SCORE

SELECT
    AVG(CAST(MatchScore AS FLOAT))
    AS AverageMatchScore
FROM CandidateAnalysis;


-- HIGHEST MATCH SCORE

SELECT
    MAX(MatchScore)
    AS HighestMatchScore
FROM CandidateAnalysis;


-- TOP 5 CANDIDATES

SELECT TOP 5
    CandidateName,
    MatchScore
FROM CandidateAnalysis
ORDER BY MatchScore DESC;


-- CANDIDATE RANKING

SELECT

    ROW_NUMBER()
    OVER (
        ORDER BY MatchScore DESC
    ) AS RankNo,

    CandidateName,

    MatchScore

FROM CandidateAnalysis;


-- ANALYSIS TREND

SELECT

    CAST(
        AnalysisDate AS DATE
    ) AS AnalysisDay,

    COUNT(*) AS TotalAnalyses

FROM CandidateAnalysis

GROUP BY
    CAST(
        AnalysisDate AS DATE
    )

ORDER BY
    AnalysisDay;


/* =========================================================
   VIEW ALL DATA
   ========================================================= */

SELECT *
FROM CandidateAnalysis
ORDER BY MatchScore DESC;