from agents.researcher import research_agent
from agents.summarizer import summary_agent
from agents.citation import citation_agent


async def run_research_pipeline(query: str):

    # Step 1 → Research
    research = await research_agent.run(query)

    # Step 2 → Summarize
    summary = await summary_agent.run(
        str(research.output)
    )

    # Step 3 → Generate Citations
    citations = await citation_agent.run(
        str(research.output)
    )

    return {
        "research": research.output,
        "summary": summary.output,
        "citations": citations.output
    }