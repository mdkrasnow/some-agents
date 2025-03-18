# AI Agent Interface

A Streamlit application for interacting with various AI agents built with CrewAI, now using OpenRouter for access to multiple AI models.

## Features

- Choose from multiple AI agent crews for different tasks
- Select from a wide range of AI models organized by company (via OpenRouter)
- Input your OpenRouter API key securely
- Create custom task descriptions
- View and edit results in markdown format
- Copy results to clipboard
- User-friendly interface

## Available Agents

1. **Document Refining** - Generate and refine document content with a team of researcher and writer agents.
2. **Blog Writing** - Create blog posts with research, writing, and content refinement agents.
3. **Trip Planner** - Plan trips with research, itinerary planning, and local expert agents.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/some-agents.git
   cd some-agents
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Sign up for an OpenRouter account at [openrouter.ai](https://openrouter.ai/) and get your API key.

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter your OpenRouter API key in the sidebar

4. Select a company and model from the dropdown menus in the sidebar

5. Select an agent from the dropdown menu

6. Enter your task description in the text area:
   - For the blog-writing agent, you can specify a topic using "topic: [your topic]"
   - For the trip-planner agent, you can specify a destination using "destination: [your destination]"

7. Click "Run Agent" to start the process

8. The output will appear below in two tabs:
   - "Rendered Markdown" shows the formatted output
   - "Edit Output" allows you to modify the output

9. Use the "Copy Output" button to copy the result to your clipboard

## About OpenRouter

This application uses [OpenRouter](https://openrouter.ai/) as a unified API for accessing various AI models from different providers, including:

- OpenAI (GPT-4o, GPT-3.5-Turbo)
- Anthropic (Claude 3.5 Sonnet, Claude 2)
- Mistral AI (Mistral Large, Medium, Small)
- Meta/Llama (Llama 3.1, Llama 3)
- Google (Gemini Pro, Gemma)
- And many other models from various providers

OpenRouter allows you to access all these models through a single API, making it easy to switch between different models for your AI tasks.

## Adding New Agents

To add a new agent:

1. Create a new Python file in the `agents` directory
2. Implement a `run_agent(task_description)` function that returns a string result
3. The new agent will automatically appear in the dropdown menu in the app

To make your agent compatible with model selection:
1. Import the necessary modules: `from langchain_openai import ChatOpenAI`
2. Add a parameter for the LLM in your agent creation: `llm=llm`
3. Use the provided setup functions or create your own to initialize the LLM

## Requirements

- Python 3.7+
- OpenRouter API key
- Streamlit
- CrewAI
- LangChain and appropriate providers

## License

[Include license information here]
