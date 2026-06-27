"""
Source Hunter Agent

This agent searches the curated paper corpus to retrieve evidence for each
sub-question in the research plan.
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

from tools.paper_rag_tool import search_papers

source_hunter = Agent(
    role="Source Discovery Investigator",
    goal=(
        "Find 8-12 high-quality, relevant passages from the paper corpus that "
        "directly support the research plan."
    ),
    backstory=(
        "You are a meticulous literature reviewer who does not stop at the first "
        "search result. You triangulate across papers, compare sections, and "
        "prioritize passages that are directly relevant, specific, and evidence-based."
    ),
    tools=[search_papers],
    verbose=True,
    memory=True,
    allow_delegation=False,
)
