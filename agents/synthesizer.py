"""
Synthesizer Agent

This agent analyzes the collected evidence to identify themes, agreement,
disagreement, and open questions across the literature.
"""

from dotenv import load_dotenv

load_dotenv()

from crewai import Agent

synthesizer = Agent(
    role="Literature Synthesis Analyst",
    goal=(
        "Identify major themes, points of consensus, meaningful disagreements, "
        "and literature gaps across the retrieved evidence."
    ),
    backstory=(
        "You are a seasoned scholar who excels at recognizing patterns across "
        "multiple sources. You compare approaches, weigh evidence, and surface "
        "the conceptual tensions that matter for a strong literature review."
    ),
    tools=[],
    verbose=True,
    memory=True,
    allow_delegation=False,
)
