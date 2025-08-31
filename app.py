import streamlit as st
from crewai import Crew, Process
from textwrap import dedent

# Assuming agents.py and tasks.py are in the same directory
from agents import FinancialAnalystAgents
from Tasks import FinancialAnalystTasks

# Initialize the session state for storing the result
if 'result' not in st.session_state:
    st.session_state.result = None

# --- Streamlit UI ---
st.set_page_config(page_title="AI Research & Blog Assistant", page_icon="🤖")

st.title("🤖 AI-Powered Research & Blog Post Generator")
st.markdown(dedent("""
    **Welcome!** Enter a topic below, and our AI agents will conduct research and write a comprehensive blog post for you.
    - **Senior Research Analyst:** Gathers and analyzes information.
    - **Senior Content Writer:** Crafts an engaging blog post from the research.
"""))

st.sidebar.header("About")
st.sidebar.info(dedent("""
    This application leverages a multi-agent system built with CrewAI to automate the process of research and content creation.
    
    **Libraries Used:**
    - Streamlit
    - CrewAI
    - LangChain (for LLM integration)
    - Serper (for search)
"""))

st.sidebar.header("API Keys")
st.sidebar.info(dedent("""
    Please make sure you have your `GEMINI_API_KEY` and `SERPER_API_KEY` set in a `.env` file in the project root.
"""))

# --- Main App Logic ---
topic = st.text_input("Enter the topic for your blog post:", placeholder="e.g., The Future of Renewable Energy")

if st.button("Generate Blog Post", type="primary"):
    if not topic:
        st.error("Please enter a topic to begin.")
    else:
        with st.spinner("🤖 Agents at work... Researching and writing your blog post. This may take a few minutes..."):
            try:
                # Initialize agents and tasks
                agents = FinancialAnalystAgents()
                tasks = FinancialAnalystTasks()

                research_analyst = agents.research_analyst()
                content_writer = agents.content_writer()

                research_task = tasks.research_task(research_analyst, topic)
                content_creation_task = tasks.content_creation_task(content_writer, topic, research_task)

                # Create and run the crew
                crew = Crew(
                    agents=[research_analyst, content_writer],
                    tasks=[research_task, content_creation_task],
                    process=Process.sequential,
                    verbose=True
                )

                result = crew.kickoff()
                st.session_state.result = result

            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.result = None

# --- Display Results ---
if st.session_state.result:
    st.subheader("Generated Blog Post:")
    st.markdown(str(st.session_state.result))   # ✅ force string here too

    st.download_button(
        label="📥 Download Blog Post",
        data=str(st.session_state.result),      # ✅ string for download
        file_name=f"{topic.replace(' ', '_').lower()}_blog_post.md",
        mime="text/markdown",
    )


