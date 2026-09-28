from crewai import Task

def create_research_task(agent, topic):
    return Task(
        description=f"Conduct comprehensive research on the topic: {topic}. "
                    f"Use your search tool to find the most recent and relevant information. "
                    f"Focus on key trends, facts, and major breakthroughs.",
        expected_output="A detailed summary of the research findings, including key bullet points and URLs of sources.",
        agent=agent
    )

def create_writing_task(agent, topic):
    return Task(
        description=f"Using the research provided, write a comprehensive and engaging report on {topic}. "
                    f"Structure the report with a clear introduction, main sections with headings, and a conclusion.",
        expected_output="A well-formatted markdown report that is ready for publication.",
        agent=agent
    )
