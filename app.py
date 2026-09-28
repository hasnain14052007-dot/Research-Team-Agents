import streamlit as st
import os
from crewai import Crew, Process
from researcher_agent import create_researcher
from writer_agent import create_writer
from tasks import create_research_task, create_writing_task

st.set_page_config(page_title="AI Research Team", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent Research Team")
st.markdown("Powered by **CrewAI**, **Groq (Llama 3.3)**, and **Streamlit**.")

# Sidebar for API Keys
with st.sidebar:
    st.header("🔑 API Keys Setup")
    groq_api_key = st.text_input("Groq API Key", type="password")
    serper_api_key = st.text_input("Serper API Key (Search Tool)", type="password")
    st.markdown("Get a free Serper API key at [serper.dev](https://serper.dev/).")

topic = st.text_input("Enter a research topic:", placeholder="e.g., The future of solid-state batteries in EVs")

if st.button("Start Research"):
    if not groq_api_key or not serper_api_key:
        st.error("Please enter both API keys in the sidebar to continue.")
    elif not topic:
        st.error("Please enter a research topic.")
    else:
        # Inject API keys into the environment for tools and agents to access
        os.environ["GROQ_API_KEY"] = groq_api_key
        os.environ["SERPER_API_KEY"] = serper_api_key
        
        with st.spinner("Agents are assembling and researching... This usually takes 30-60 seconds."):
            try:
                # 1. Initialize Agents
                researcher = create_researcher()
                writer = create_writer()
                
                # 2. Initialize Tasks
                research_task = create_research_task(researcher, topic)
                writing_task = create_writing_task(writer, topic)
                
                # 3. Assemble Crew
                research_crew = Crew(
                    agents=[researcher, writer],
                    tasks=[research_task, writing_task],
                    process=Process.sequential,
                    verbose=True
                )
                
                # 4. Kickoff Execution
                result = research_crew.kickoff()
                
                st.success("Research Complete!")
                st.markdown("### 📄 Final Report")
                
                # Modern CrewAI returns a CrewOutput object; cast to string for Streamlit
                st.markdown(str(result))
                
            except Exception as e:
                st.error(f"An error occurred during execution: {e}")