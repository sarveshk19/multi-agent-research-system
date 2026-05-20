import config

from pydantic import BaseModel
from pydantic_ai import Agent


class Citation(BaseModel):
    citations: list[str]


citation_agent = Agent(
    model='groq:llama-3.3-70b-versatile',

    output_type=Citation,

    system_prompt="""
    Generate clean citations from the research findings.
    """
)