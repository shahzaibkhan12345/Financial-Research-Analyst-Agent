from crewai import Agent,LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize LLM
# Using ChatGoogleGenerativeAI for Gemini.
# Note: "gemini-1.5-flash" is a valid and performant model.
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize Serper Search Tool

serper_dev_tool = SerperDevTool(n_results=3)

class FinancialAnalystAgents():
    def research_analyst(self):
        return Agent(
            name="Senior Research Analyst",
            role="Conducts deep research on emerging technologies and trends across industries.",
            goal=(
                "Conduct a thorough research study on the provided topic. "
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

    def content_writer(self):
        return Agent(
            name="Senior Content Writer",
            role="Crafts detailed, well-structured reports and articles based on research findings.",
            goal=(
                "Using the research findings on the provided topic, "
                "create a blog post that is clear, engaging, and informative. "
                "Ensure the content is well-organized, with a logical flow and proper citations."
            ),
            llm=llm,
            backstory=(
                "With over 10 years of experience in technical writing and content creation, "
                "you excel at transforming complex information into clear, engaging narratives. "
                "Your work has been published in leading industry journals and platforms."
                "You work closely with the Research Analyst to ensure you write posts using authentic facts."
                "You have a talent for weaving facts into compelling stories that resonate with readers."
            ),
            verbose=True,
            allow_delegation=False,
            tools=[]
        )