"""
Report Writer Agent

This agent turns synthesized evidence into a polished literature review in
markdown with clear sections and explicit source attribution.
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

report_writer = Agent(
    role="Academic Report Writer",
    goal=(
        "Produce a clear, well-structured literature review in markdown with "
        "executive summary, introduction, methodology, findings, discussion, "
        "conclusion, and references."
    ),
    backstory=(
        "You are an expert academic communicator who turns raw evidence into "
        "concise, well-organized prose. You prioritize clarity, logical flow, "
        "and careful attribution so the final report is trustworthy and easy to read."
    ),
    tools=[],
    verbose=True,
    memory=True,
    allow_delegation=False,
)
