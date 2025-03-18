import os
import importlib
import streamlit as st
import glob
from pathlib import Path
import time
from collections import defaultdict

# Set page configuration
st.set_page_config(
    page_title="AI Agent Interface",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'output' not in st.session_state:
    st.session_state.output = ""
if 'edited_output' not in st.session_state:
    st.session_state.edited_output = ""
if 'show_output' not in st.session_state:
    st.session_state.show_output = False
if 'models_by_company' not in st.session_state:
    # Models grouped by company
    models_list = [
        "cohere/command-r-08-2024", "cohere/command-r-plus-08-2024", "sao10k/l3.1-euryale-70b", "google/gemini-flash-1.5-8b-exp",
        "qwen/qwen-2.5-vl-7b-instruct", "ai21/jamba-1-5-large", "ai21/jamba-1-5-mini", "microsoft/phi-3.5-mini-128k-instruct",
        "nousresearch/hermes-3-llama-3.1-70b", "nousresearch/hermes-3-llama-3.1-405b", "openai/chatgpt-4o-latest", "sao10k/l3-lunaris-8b",
        "aetherwiing/mn-starcannon-12b", "openai/gpt-4o-2024-08-06", "meta-llama/llama-3.1-405b", "nothingiisreal/mn-celeste-12b",
        "perplexity/llama-3.1-sonar-small-128k-chat", "perplexity/llama-3.1-sonar-large-128k-chat", "perplexity/llama-3.1-sonar-large-128k-online",
        "perplexity/llama-3.1-sonar-small-128k-online", "meta-llama/llama-3.1-405b-instruct", "meta-llama/llama-3.1-8b-instruct:free",
        "meta-llama/llama-3.1-8b-instruct", "meta-llama/llama-3.1-70b-instruct", "mistralai/mistral-nemo:free", "mistralai/mistral-nemo",
        "mistralai/codestral-mamba", "openai/gpt-4o-mini", "openai/gpt-4o-mini-2024-07-18", "qwen/qwen-2-7b-instruct:free",
        "qwen/qwen-2-7b-instruct", "google/gemma-2-27b-it", "alpindale/magnum-72b", "google/gemma-2-9b-it:free", "google/gemma-2-9b-it",
        "01-ai/yi-large", "ai21/jamba-instruct", "anthropic/claude-3.5-sonnet-20240620:beta", "anthropic/claude-3.5-sonnet-20240620",
        "sao10k/l3-euryale-70b", "cognitivecomputations/dolphin-mixtral-8x22b", "qwen/qwen-2-72b-instruct", "mistralai/mistral-7b-instruct:free",
        "mistralai/mistral-7b-instruct", "mistralai/mistral-7b-instruct-v0.3", "nousresearch/hermes-2-pro-llama-3-8b",
        "microsoft/phi-3-mini-128k-instruct:free", "microsoft/phi-3-mini-128k-instruct", "microsoft/phi-3-medium-128k-instruct:free",
        "microsoft/phi-3-medium-128k-instruct", "neversleep/llama-3-lumimaid-70b", "google/gemini-flash-1.5", "openai/gpt-4o-2024-05-13",
        "meta-llama/llama-guard-2-8b", "openai/gpt-4o", "openai/gpt-4o:extended", "neversleep/llama-3-lumimaid-8b:extended",
        "neversleep/llama-3-lumimaid-8b", "sao10k/fimbulvetr-11b-v2", "meta-llama/llama-3-8b-instruct:free", "meta-llama/llama-3-8b-instruct",
        "meta-llama/llama-3-70b-instruct", "mistralai/mistral-large", "google/gemma-7b-it", "openai/gpt-3.5-turbo-0613",
        "openai/gpt-4-turbo-preview", "nousresearch/nous-hermes-2-mixtral-8x7b-dpo", "mistralai/mistral-small", "mistralai/mistral-tiny",
        "mistralai/mistral-medium", "mistralai/mistral-7b-instruct-v0.2", "cognitivecomputations/dolphin-mixtral-8x7b", "google/gemini-pro-vision",
        "google/gemini-pro", "mistralai/mixtral-8x7b", "mistralai/mixtral-8x7b-instruct", "openchat/openchat-7b:free", "openchat/openchat-7b",
        "neversleep/noromaid-20b", "anthropic/claude-2:beta", "anthropic/claude-2", "anthropic/claude-2.1:beta", "anthropic/claude-2.1",
        "teknium/openhermes-2.5-mistral-7b", "undi95/toppy-m-7b:free", "undi95/toppy-m-7b", "alpindale/goliath-120b", "openrouter/auto",
        "openai/gpt-3.5-turbo-1106", "openai/gpt-4-1106-preview", "google/palm-2-chat-bison-32k", "google/palm-2-codechat-bison-32k",
        "jondurbin/airoboros-l2-70b", "xwin-lm/xwin-lm-70b", "openai/gpt-3.5-turbo-instruct", "mistralai/mistral-7b-instruct-v0.1",
        "pygmalionai/mythalion-13b", "openai/gpt-3.5-turbo-16k", "openai/gpt-4-32k", "openai/gpt-4-32k-0314", "nousresearch/nous-hermes-llama2-13b",
        "mancer/weaver", "huggingfaceh4/zephyr-7b-beta:free", "anthropic/claude-2.0:beta", "anthropic/claude-2.0", "undi95/remm-slerp-l2-13b",
        "google/palm-2-chat-bison", "google/palm-2-codechat-bison", "gryphe/mythomax-l2-13b:free", "gryphe/mythomax-l2-13b",
        "meta-llama/llama-2-13b-chat", "meta-llama/llama-2-70b-chat", "openai/gpt-3.5-turbo", "openai/gpt-3.5-turbo-0125", "openai/gpt-4",
        "openai/gpt-4-0314"
    ]
    
    # Group models by company
    models_by_company = defaultdict(list)
    for model in models_list:
        company = model.split('/')[0]
        models_by_company[company].append(model)
    
    st.session_state.models_by_company = models_by_company
    st.session_state.selected_company = None
    st.session_state.selected_model = None

# Function to copy text to clipboard using JavaScript
def copy_to_clipboard():
    st.toast("Copied to clipboard!", icon="✅")

# Sidebar for configuration
st.sidebar.title("Configuration")

# API Key input in sidebar
api_key = st.sidebar.text_input("OpenRouter API Key", type="password")
if api_key:
    os.environ["OPENROUTER_API_KEY"] = api_key

# Model selection in sidebar
st.sidebar.markdown("## Model Selection")

# Company selection
companies = sorted(st.session_state.models_by_company.keys())
selected_company = st.sidebar.selectbox(
    "Select Company", 
    companies,
    format_func=lambda x: x.capitalize()
)

if selected_company:
    st.session_state.selected_company = selected_company
    # Model selection for the chosen company
    company_models = st.session_state.models_by_company[selected_company]
    
    # Format model names to show only what's after the slash
    selected_model = st.sidebar.selectbox(
        f"Select {selected_company.capitalize()} Model",
        company_models,
        format_func=lambda x: x.split('/')[-1]
    )
    
    if selected_model:
        st.session_state.selected_model = selected_model
        # Store the selected model in environment variables
        os.environ["SELECTED_MODEL"] = selected_model

# Additional API keys (optional)
with st.sidebar.expander("Additional API Keys (Optional)"):
    serper_api_key = st.text_input("Serper API Key (for search)", type="password")
    if serper_api_key:
        os.environ["SERPER_API_KEY"] = serper_api_key

# Main content area
st.title("AI Agent Interface")

# Get available agent files
agent_files = [Path(f).stem for f in glob.glob("agents/*.py")]

# Agent info dictionary
agent_info = {
    "document-refining": "Generate and refine document content with a team of researcher and writer agents.",
    "blog-writing": "Create blog posts with research, writing, and content refinement agents.",
    "trip-planner": "Plan trips with research, itinerary planning, and local expert agents.",
    "code-documentation": "Chat with code documentation using semantic search. Provide a documentation URL in your task description."
}

# Agent selection
col1, col2 = st.columns([3, 1])
with col1:
    selected_agent = st.selectbox("Select an Agent", agent_files)
with col2:
    st.write("")
    st.write("")
    st.info(agent_info.get(selected_agent, "Select an agent to get started"))

# Task description input
task_description = st.text_area("Task Description", height=150, 
                               placeholder="Enter your task description here...")

# Run button
if st.button("Run Agent"):
    if not api_key:
        st.error("Please enter your OpenRouter API key in the sidebar.")
    elif not st.session_state.selected_model:
        st.error("Please select a model.")
    elif not task_description:
        st.error("Please enter a task description.")
    else:
        with st.spinner(f"Running {selected_agent} agent with {st.session_state.selected_model.split('/')[-1]}..."):
            try:
                # Dynamically import the selected agent module
                agent_module = importlib.import_module(f"agents.{selected_agent}")
                
                # Run the agent with the task description
                # Pass the API key to avoid command-line prompt
                if hasattr(agent_module, 'run_agent'):
                    # Create a wrapper function to avoid the command-line prompts
                    def run_without_prompt(task_description):
                        # Save the original config in case we need to restore it
                        from model_utils import prompt_for_openrouter_config
                        original_prompt = prompt_for_openrouter_config
                        
                        # Override the model selection to use our UI selections
                        import model_utils
                        model_utils.prompt_for_openrouter_config = lambda: (api_key, st.session_state.selected_model)
                        
                        # Run the agent with our configuration
                        if selected_agent == "code-documentation":
                            # Special handling for code-documentation agent which needs a docs_url
                            # Extract docs_url from task description or use a default
                            import re
                            docs_url_match = re.search(r'(http[s]?://\S+)', task_description)
                            docs_url = docs_url_match.group(1) if docs_url_match else "https://docs.crewai.com"
                            result = agent_module.run_agent(docs_url=docs_url)
                        else:
                            # Default handling for other agents
                            result = agent_module.run_agent(task_description)
                        
                        # Restore the original config function
                        model_utils.prompt_for_openrouter_config = original_prompt
                        return result
                    
                    result = run_without_prompt(task_description)
                else:
                    st.error(f"The selected agent '{selected_agent}' does not have a run_agent function.")
                    st.stop()
                
                # Store the result in session state
                st.session_state.output = result
                st.session_state.edited_output = result
                st.session_state.show_output = True
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Display output if available
if st.session_state.show_output:
    st.markdown("---")
    st.markdown("## Output")
    
    # Create tabs for different views of the output
    tab1, tab2 = st.tabs(["Rendered Markdown", "Edit Output"])
    
    with tab1:
        st.markdown(st.session_state.edited_output)
        
        # Add copy button for the rendered output
        if st.button("Copy Output", key="copy_rendered"):
            st.write('<script>navigator.clipboard.writeText(`' + st.session_state.edited_output.replace('`', '\\`') + '`);</script>', unsafe_allow_html=True)
            copy_to_clipboard()
    
    with tab2:
        # Create an editable text area with the result
        edited_text = st.text_area("Edit Output", value=st.session_state.edited_output, height=400, key="output_editor")
        
        # Update button
        if st.button("Update Output"):
            st.session_state.edited_output = edited_text
        
        # Add copy button for the editable output
        if st.button("Copy Output", key="copy_editable"):
            st.write('<script>navigator.clipboard.writeText(`' + edited_text.replace('`', '\\`') + '`);</script>', unsafe_allow_html=True)
            copy_to_clipboard()

# Instructions at the bottom
with st.expander("How to use this app"):
    st.markdown("""
    ### Instructions:
    
    1. Enter your OpenRouter API Key in the sidebar (required)
    2. Select a company and model from the sidebar dropdowns
    3. Select an agent from the dropdown menu
    4. Enter your task description in the text area
       - For the blog-writing agent, you can specify a topic using "topic: [your topic]"
       - For the trip-planner agent, you can specify a destination using "destination: [your destination]"
    5. Click "Run Agent" to start the process
    6. The output will appear below in two tabs:
       - "Rendered Markdown" shows the formatted output
       - "Edit Output" allows you to modify the output
    7. Use the "Copy Output" button to copy the result to your clipboard
    
    ### About OpenRouter:
    
    This app uses OpenRouter to access various AI models. When you provide your OpenRouter API key,
    you'll be able to use models from OpenAI, Anthropic, Cohere, and many others through a single interface.
    
    ### Running the app:
    
    ```bash
    streamlit run app.py
    ```
    
    ### Requirements:
    
    Make sure you have all the required packages installed:
    
    ```bash
    pip install -r requirements.txt
    ```
    """) 