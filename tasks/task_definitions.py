"""
Task Definitions for Research Crew

The workflow is a sequential pipeline that first derives a research strategy,
then gathers evidence, synthesizes themes, and writes the final report.
"""

from crewai import Task

from agents import query_expander, report_writer, source_hunter, synthesizer


def create_research_tasks(research_question: str) -> list[Task]:
    """Create the four sequential tasks for the research workflow."""

    expand_task = Task(
        description=(
            f"Break the research question into a concrete research strategy. "
            f"For the question: {research_question}, identify the core concepts, "
            "sub-questions, important keywords, synonym variants, and useful "
            "search angles. Show a short ReAct-style reasoning trace with Thought, "
            "Action, Observation, and a proposed plan before listing the final strategy."
        ),
        agent=query_expander,
        expected_output=(
            "A structured research plan with: (1) a short ReAct-style reasoning trace, "
            "(2) 3-5 sub-questions, (3) 8-12 keywords or phrases, and (4) 3-4 search angles."
        ),
    )

    search_task = Task(
        description=(
            "Use the research plan from the previous step to retrieve evidence from "
            "the paper corpus. Search for passages that answer each sub-question, "
            "prioritize specific and defensible evidence, and include a short reasoning "
            "trace describing what you looked for and why."
        ),
        agent=source_hunter,
        context=[expand_task],
        expected_output=(
            "A curated set of 8-12 relevant passages with paper/source details, "
            "section labels, relevance notes, and a brief explanation of why each "
            "passage was selected."
        ),
    )

    synthesis_task = Task(
        description=(
            "Analyze the retrieved passages for repeated themes, agreements, tensions, "
            "and gaps. Produce a synthesis that explains what the literature says, "
            "where it disagrees, and what remains unresolved. Include a concise "
            "ReAct-style reasoning summary before the final synthesis."
        ),
        agent=synthesizer,
        context=[expand_task, search_task],
        expected_output=(
            "A synthesis document that summarizes the main themes, highlights consensus "
            "and disagreements, identifies open questions, and notes evidence-backed gaps."
        ),
    )

    report_task = Task(
        description=(
            "Write the final literature review as a polished markdown document. "
            "Use the planning notes, retrieved evidence, and synthesis to produce "
            "sections for Executive Summary, Introduction, Methodology, Findings, "
            "Discussion, Conclusion, and References. Ground every major claim in the "
            "paper corpus and include a short reasoning note before the final report."
        ),
        agent=report_writer,
        context=[expand_task, search_task, synthesis_task],
        expected_output=(
            "A complete markdown literature review with the required sections, clear "
            "organization, and source-based citations."
        ),
    )

    return [expand_task, search_task, synthesis_task, report_task]
