import config

from pydantic import BaseModel
from pydantic_ai import Agent


class Summary(BaseModel):
    overview: str
    key_points: list[str]


summary_agent = Agent(
    model='groq:llama-3.3-70b-versatile',

    output_type=Summary,

    system_prompt="""
    You are a professional summarizer.

    Summarize the research data clearly and professionally.

    Return:
    - short overview
    - important key points
    """
)