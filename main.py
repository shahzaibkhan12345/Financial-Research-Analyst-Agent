from crewai import Crew
from agents import research_analyst, content_writer, topic
from Tasks import research_task,writing_task
from colorama import Fore, init
init(autoreset=True)
crew=Crew(
    agents=[research_analyst,content_writer],
    tasks=[research_task,writing_task],
    verbose=True
)
result=crew.kickoff(inputs={"topic":topic})
with open("research_blog.md","w") as f:
    f.write(str(result))
print(f"{Fore.CYAN}{result}{Fore.CYAN}")