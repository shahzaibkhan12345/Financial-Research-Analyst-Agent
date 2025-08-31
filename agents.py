from crewai import Agent, LLM, Task, Crew
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize Serper Search Tool
serper_dev_tool = SerperDevTool(
    n=3,  # fetch 3 results for broader research
    api_key=os.getenv("SERPERDEV_API_KEY")
)

# Topic of research (can be changed freely)
topic = "The Impact of Agentic AI on Global Industries"

# Create First Agent: Senior Research Analyst
research_analyst = Agent(
    name="Senior Research Analyst",
    role="Conducts deep research on emerging technologies and trends across industries.",
    goal=(
    f"Conduct a thorough research study on: {topic}. "
    "Analyze and synthesize findings from multiple credible sources. "
    "Identify current applications, key trends, and gaps in adoption. "
    "Provide structured insights with citations for fact-checking."
   ),
    llm=llm,
    backstory=(
        "With over 12 years of experience in market and academic research, "
        "you specialize in analyzing emerging technologies across multiple industries. "
        "Your insights have guided organizations in making evidence-based decisions."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[serper_dev_tool]
)

#Now agent 2 Senior Content writer

content_writer = Agent(
    name="Senior Content Writer",
    role="Crafts detailed, well-structured reports and articles based on research findings.",
    goal=(
        f"Using the research findings on: {topic}, "
        "create a blog post that is clear, engaging, and informative. "  
        "Ensure the content is well-organized, with a logical flow and proper citations."
    ),
    llm=llm,
    backstory=(
        "With over 10 years of experience in technical writing and content creation, "
        "you excel at transforming complex information into clear, engaging narratives. "
        "Your work has been published in leading industry journals and platforms."
        "You work closely with great content writers by ensuring you write post using the Authentic Facts provided by the Research Analyst."
        "You have a talent of weaving facts into compelling stories that resonate with readers."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[]
)