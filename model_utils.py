import os
from langchain_openai import ChatOpenAI
from collections import defaultdict
from models import get_models_by_company

def setup_openrouter(api_key=None, model_name=None):
    """Set up OpenRouter with the provided API key and model."""
    if api_key:
        os.environ["OPENROUTER_API_KEY"] = api_key
    else:
        # Check if API key exists in environment variables
        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            return None
    
    # Set OpenRouter base URL if not already set
    if not os.environ.get("OPENAI_API_BASE"):
        os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
    
    # If model is specified, create and return an LLM instance
    if model_name:
        # Prepend "openrouter/" to the model name if needed
        if not model_name.startswith("openrouter/"):
            model_name = f"openrouter/{model_name}"
        
        return ChatOpenAI(
            model=model_name,
            temperature=0.7,
            openai_api_key=api_key
        )
    return None

def prompt_for_openrouter_config():
    """Get API key and model selection from environment or prompt the user."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    selected_model = os.environ.get("SELECTED_MODEL", "openai/gpt-4o")
    
    if not api_key:
        api_key = input("Please enter your OpenRouter API key: ").strip()
        if not api_key:
            print("No API key provided. Exiting.")
            return None, None
            
        # Simple model selection if we had to prompt for API key
        print("\nAvailable models:")
        print("1. GPT-4o")
        print("2. Claude 3.5 Sonnet")
        print("3. Mistral Large")
        
        selection = input("\nSelect model (1-3): ").strip()
        if selection == "1":
            selected_model = "openai/gpt-4o"
        elif selection == "2":
            selected_model = "anthropic/claude-3.5-sonnet-20240620"
        elif selection == "3":
            selected_model = "mistralai/mistral-large"
        else:
            selected_model = "openai/gpt-4o"  # Default choice
            
    return api_key, selected_model

def get_available_models(top_n=10):
    """Return a dictionary of popular models grouped by company."""
    models_by_company = get_models_by_company()
    
    # Dictionary to store the top models from each company
    top_models = {}
    
    # Extract top models from each company
    for company, models in models_by_company.items():
        top_models[company] = models[:min(top_n, len(models))]
    
    return top_models 