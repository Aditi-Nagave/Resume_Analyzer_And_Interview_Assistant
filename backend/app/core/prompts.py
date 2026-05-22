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

MOCK_INTERVIEW_PROMPT = """
You are an AI interviewer.

Based on the candidate resume:

{resume}

Ask one professional interview question.
"""

FEEDBACK_PROMPT = """
Evaluate the following interview answer.

Question:
{question}

Answer:
{answer}

Evaluate:
1. Confidence
2. Technical Accuracy
3. Communication
4. Relevance

Give scores out of 10 and feedback.
"""