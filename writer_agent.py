import os
import streamlit as st
from crewai import Agent, LLM

def get_groq_llm():
    groq_key = st.secrets.get("GROQ_API_KEY") or os.environ.get("GROQ_API_KEY")
    return LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=groq_key
    )

def create_writer():
    return Agent(
        role="Tech Content Strategist",
        goal="Craft compelling, well-structured, and easy-to-understand reports on {topic} based on research",
        backstory="You are a renowned technical writer known for transforming complex research into engaging, readable articles. You format information clearly using markdown.",
        llm=get_groq_llm(),
        verbose=True
    )
