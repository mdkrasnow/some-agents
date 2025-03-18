import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from models import get_models_by_company
from model_utils import setup_openrouter, prompt_for_openrouter_config

def run_agent(task_description):
    # Set up OpenRouter API key and model
    api_key, selected_model = prompt_for_openrouter_config()
    if not api_key:
        return "Error: OpenRouter API key is required."
    
    # Set up the LLM with the selected model
    llm = setup_openrouter(api_key, selected_model)
    if not llm:
        return "Error: Unable to set up language model with the provided credentials."
    
    # Define your agents
    researcher = Agent(
        role="Researcher",
        goal="Conduct thorough research and analysis on AI and AI agents",
        backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
        allow_delegation=False,
        llm=llm,
    )

    writer = Agent(
        role="Senior Writer",
        goal="Create compelling content about AI and AI agents",
        backstory="You're a senior writer, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently writing content for a new client.",
        allow_delegation=False,
        llm=llm,
    )

    # Define your task with the user's input
    task = Task(
        description=task_description,
        expected_output="Comprehensive response based on the task description.",
    )

    # Define the manager agent
    manager = Agent(
        role="Project Manager",
        goal="Efficiently manage the crew and ensure high-quality task completion",
        backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
        allow_delegation=True,
        llm=llm,
    )

    # Instantiate your crew with a custom manager
    crew = Crew(
        agents=[researcher, writer],
        tasks=[task],
        manager_agent=manager,
        process=Process.hierarchical,
    )

    # Start the crew's work
    result = crew.kickoff()
    return result

# This code only runs when the file is executed directly, not when imported
if __name__ == "__main__":
    sample_task = "Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes."
    print(run_agent(sample_task))