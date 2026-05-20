import config

from pydantic_ai import Agent
from models.research_models import ResearchResults


research_agent = Agent(
    model='groq:llama-3.3-70b-versatile',

    output_type=ResearchResults,

    system_prompt="""
    You are a professional AI research agent.

    Research the given topic carefully.

    Return:
    - latest trends
    - important technologies
    - companies involved
    - future predictions

    Keep answers structured and professional.
    """
)