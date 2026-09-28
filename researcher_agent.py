import os
import streamlit as st
from crewai import Agent, LLM
from crewai_tools import SerperDevTool

def get_groq_llm():
    # Safely fetch API key from Streamlit Secrets or Environment
    groq_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    return LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=groq_key
    )

def create_researcher():
    search_tool = SerperDevTool()
    return Agent(
        role="Senior Technical Researcher",
        goal="Uncover the latest developments, trends, and detailed information about {topic}",
        backstory="You are an expert researcher with a keen eye for finding accurate and up-to-date information on the web. You carefully analyze search results to extract key facts.",
        tools=[search_tool],
        llm=get_groq_llm(),
        verbose=True
    )
