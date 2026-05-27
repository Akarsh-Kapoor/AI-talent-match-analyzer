from pypdf import PdfReader
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()

# Replace with your Gemini API Key
genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

def extract_resume_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text[:3000]


def analyze_candidate(
    resume_text,
    job_description
):

    model = genai.GenerativeModel(
        "gemini-3.5-flash"
    )

    prompt = f"""
    Compare the resume and job description.

    Return ONLY valid JSON.

    STRICT FORMAT:

    {{
      "candidate_name": "",
      "match_score": 0,
      "matched_skills": [],
      "missing_skills": [],
      "learning_recommendations": [
        {{
          "skill": "",
          "recommendations": []
        }}
      ],
      "candidate_summary": ""
    }}

    Rules:

    1. learning_recommendations MUST ALWAYS be an array of objects.
    2. Each object must contain:
       - skill
       - recommendations
    3. recommendations must contain exactly 3 learning topics/courses.
    4. Return ONLY JSON.
    5. No markdown.
    6. No explanation.
    7. Extract the candidate's full name from the resume.
    8. Store it in candidate_name.
    9. Return ONLY valid JSON.

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = model.generate_content(
        prompt
    )

    result = response.text

    result = result.replace(
        "```json",
        ""
    )

    result = result.replace(
        "```",
        ""
    )

    return result.strip()
