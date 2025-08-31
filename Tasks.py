from crewai import Task
from textwrap import dedent

class FinancialAnalystTasks():
    def research_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                Conduct a comprehensive research on the topic: "{topic}".
                Your research must be thorough, analyzing information from various credible sources.
                Identify key trends, current applications, and potential future impacts.
                Make sure to include citations for all the facts and data points you find.
            """),
            expected_output=dedent(f"""
                A detailed research report on "{topic}".
                The report should be well-structured, with clear sections for:
                - Introduction
                - Key Trends
                - Current Applications
                - Future Projections & Impact
                - Challenges and Gaps in Adoption
                - Conclusion
                All claims and data must be backed by citations.
            """),
            agent=agent,
            async_execution=True
        )

    def content_creation_task(self, agent, topic, context):
        return Task(
            description=dedent(f"""
                Based on the provided research report on "{topic}", write an engaging and insightful blog post.
                The blog post should be easy to read for a general audience but still maintain technical accuracy.
                Structure the post with a catchy title, an introduction, a body that explains the key findings, and a conclusion.
                Incorporate the citations from the research report appropriately.
            """),
            expected_output=dedent(f"""
                A well-written blog post of at least 800 words on the topic "{topic}".
                The post should be formatted in markdown, with a clear title, headings, and subheadings.
                It must be engaging, informative, and include all necessary citations from the research.
            """),
            agent=agent,
            context=[context]
        )

