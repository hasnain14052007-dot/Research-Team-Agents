import os
from crewai import Agent, LLM

def get_groq_llm():
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")
    )

def create_writer():
    return Agent(
        role="Tech Content Strategist",
        goal="Craft compelling, well-structured, and easy-to-understand reports on {topic} based on research",
        backstory="You are a renowned technical writer known for transforming complex research into engaging, readable articles. You format information clearly using markdown.",
        llm=get_groq_llm(),
        verbose=True
    )