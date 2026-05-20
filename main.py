from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from agents.coordinator import run_research_pipeline


app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Multi-Agent Research System Running"
    }


@app.get("/research")
async def research(query: str):

    result = await run_research_pipeline(query)

    return result