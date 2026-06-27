"""
Research Crew Configuration

This module creates the research crew, hooks up the agent pipeline, and runs the
workflow end to end for a given research question.
"""

# Load environment variables BEFORE importing crewai
from dotenv import load_dotenv

load_dotenv()

from crewai import Crew, Process

from agents import query_expander, report_writer, source_hunter, synthesizer
from tasks.task_definitions import create_research_tasks


def create_research_crew(research_question: str) -> Crew:
    """Create a research crew configured for the given question."""

    tasks = create_research_tasks(research_question)

    crew = Crew(
        agents=[query_expander, source_hunter, synthesizer, report_writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        memory=True,
    )
    return crew


def run_research(research_question: str) -> str:
    """Execute the research crew and return the final report as a string."""

    crew = create_research_crew(research_question)
    result = crew.kickoff()
    return str(result)


# Allow running crew.py directly for testing
if __name__ == "__main__":
    test_question = (
        "What are the main approaches to building AI agents that can reason and act?"
    )
    print(f"Testing crew with question: {test_question}\n")
    result = run_research(test_question)
    print("\n" + "=" * 50)
    print("FINAL REPORT:")
    print("=" * 50)
    print(result)
