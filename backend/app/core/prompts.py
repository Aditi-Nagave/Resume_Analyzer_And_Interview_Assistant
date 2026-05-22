ATS_PROMPT = """
You are an expert ATS Resume Analyzer.

Analyze the resume context below.

Return:
1. ATS Score
2. Missing Skills
3. Resume Improvements
4. Suggested Projects
5. Strengths
6. Weaknesses

Resume Context:
{context}
"""

JD_PROMPT = """
Compare the resume with the job description.

Resume:
{resume}

Job Description:
{jd}

Return:
1. Match Percentage
2. Missing Skills
3. Suggestions
"""

INTERVIEW_PROMPT = """
Based on the resume context below,
generate:

1. Technical Questions
2. HR Questions
3. Project Questions

Resume Context:
{context}
"""