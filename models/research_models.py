from pydantic import BaseModel
from typing import List


class ResearchFinding(BaseModel):
    title: str
    summary: str
    source: str


class ResearchResults(BaseModel):
    topic: str
    findings: List[ResearchFinding]