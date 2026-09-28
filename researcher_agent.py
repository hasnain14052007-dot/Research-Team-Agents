import os
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def get_groq_llm():
    # CrewAI natively supports Groq through its LLM class
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")
    )

def create_researcher():
    # Cloud-based search tool (requires no local installation)
    search_tool = SerperDevTool()
    
    return Agent(
        role="Senior Technical Researcher",
        goal="Uncover the latest developments, trends, and detailed information about {topic}",
        backstory="You are an expert researcher with a keen eye for finding accurate and up-to-date information on the web. You carefully analyze search results to extract key facts.",
        tools=[search_tool],
        llm=get_groq_llm(),
        verbose=True
    )