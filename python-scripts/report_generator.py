import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def generate_report(candidate):

    # Create reports folder if it doesn't exist

    reports_folder = "candidate-generated-reports"

    os.makedirs(
        reports_folder,
        exist_ok=True
    )

    # Create file path

    filename = os.path.join(
        reports_folder,
        candidate["Candidate"]
        .replace(" ", "_")
        + "_Report.pdf"
    )

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    # Title

    content.append(
        Paragraph(
            "AI Talent Intelligence Platform",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Candidate Assessment Report",
            styles["Heading2"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # Candidate Details

    content.append(
        Paragraph(
            f"<b>Candidate Name:</b> {candidate['Candidate']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Match Score:</b> {candidate['Match Score']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 15)
    )

    # Matched Skills

    content.append(
        Paragraph(
            "Matched Skills",
            styles["Heading2"]
        )
    )

    matched_skills = candidate.get(
        "Matched Skills",
        []
    )

    if isinstance(
        matched_skills,
        list
    ):
        matched_text = ", ".join(
            matched_skills
        )
    else:
        matched_text = str(
            matched_skills
        )

    content.append(
        Paragraph(
            matched_text,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # Missing Skills

    content.append(
        Paragraph(
            "Missing Skills",
            styles["Heading2"]
        )
    )

    missing_skills = candidate.get(
        "Missing Skills",
        []
    )

    if isinstance(
        missing_skills,
        list
    ):
        missing_text = ", ".join(
            missing_skills
        )
    else:
        missing_text = str(
            missing_skills
        )

    content.append(
        Paragraph(
            missing_text,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # Summary

    content.append(
        Paragraph(
            "Candidate Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            candidate.get(
                "Summary",
                ""
            ),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    # Learning Recommendations

    recommendations = candidate.get(
        "Learning Recommendations",
        []
    )

    if recommendations:

        content.append(
            Paragraph(
                "Learning Recommendations",
                styles["Heading2"]
            )
        )

        for rec in recommendations:

            if isinstance(
                rec,
                dict
            ):

                skill = rec.get(
                    "skill",
                    ""
                )

                content.append(
                    Paragraph(
                        f"<b>{skill}</b>",
                        styles["BodyText"]
                    )
                )

                for course in rec.get(
                    "recommendations",
                    []
                ):

                    content.append(
                        Paragraph(
                            f"• {course}",
                            styles["BodyText"]
                        )
                    )

            else:

                content.append(
                    Paragraph(
                        f"• {str(rec)}",
                        styles["BodyText"]
                    )
                )

    doc.build(
        content
    )

    return filename