import os
import json
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_intent(query: str) -> dict:
    prompt = f"""
You are a BI data analyst agent.

Return ONLY valid JSON.
Do NOT use markdown.

Keys:
- chart_type: pie | bar | line | histogram
- metric: count | average
- column: Grade | Marks | Semester | Subject | null
- student_name: string or null
- student_id: string or null

Query: "{query}"
JSON:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
