import os
import streamlit as st

# Set page config first
st.set_page_config(page_title="AI Research Team", page_icon="🤖", layout="wide")

st.title("🤖 Multi-Agent Research Team")
st.markdown("Powered by **CrewAI**, **Groq (Openai)**, and **Streamlit**.")

# Inject secrets into environment variables for tools
if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

if "SERPER_API_KEY" in st.secrets:
    os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

# Fallback UI sidebar inputs if st.secrets is not set up
with st.sidebar:
    st.header("🔑 API Keys Setup")
    if "GROQ_API_KEY" not in os.environ:
        groq_api_key = st.text_input("Groq API Key", type="password")
        if groq_api_key:
            os.environ["GROQ_API_KEY"] = groq_api_key
    else:
        st.success("Groq API Key loaded!")

    if "SERPER_API_KEY" not in os.environ:
        serper_api_key = st.text_input("Serper API Key", type="password")
        if serper_api_key:
            os.environ["SERPER_API_KEY"] = serper_api_key
    else:
        st.success("Serper API Key loaded!")

# Import CrewAI modules
from crewai import Crew, Process
from researcher_agent import create_researcher
from writer_agent import create_writer
from tasks import create_research_task, create_writing_task

topic = st.text_input("Enter a research topic:", placeholder="e.g., Solid-state batteries breakthrough")

if st.button("Start Research"):
    if not os.environ.get("GROQ_API_KEY") or not os.environ.get("SERPER_API_KEY"):
        st.error("Please provide both GROQ_API_KEY and SERPER_API_KEY.")
    elif not topic:
        st.error("Please enter a research topic.")
    else:
        with st.spinner("Agents are researching and writing... (~30-60 seconds)"):
            try:
                researcher = create_researcher()
                writer = create_writer()

                research_task = create_research_task(researcher, topic)
                writing_task = create_writing_task(writer, topic)

                research_crew = Crew(
                    agents=[researcher, writer],
                    tasks=[research_task, writing_task],
                    process=Process.sequential,
                    verbose=True
                )

                result = research_crew.kickoff()

                st.success("Research Complete!")
                st.markdown("### 📄 Final Report")
                st.markdown(str(result))

            except Exception as e:
                st.error(f"An error occurred: {e}")
