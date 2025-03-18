# Code Documentation Chat Agent

A Streamlit application that allows you to chat with code documentation using semantic search. This agent uses CrewAI's CodeDocsSearchTool to perform intelligent searches within the documentation you provide.

## Features

- **Documentation Chat**: Ask questions about any code documentation and get relevant answers
- **Custom URL Input**: Specify any documentation URL you want to chat with
- **Persisted Chat History**: Chat history is maintained during your session
- **Friendly UI**: Clean, intuitive user interface with message styling

## Installation

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:

```bash
streamlit run app.py
```

2. In the sidebar, enter the URL of the documentation you want to chat with (e.g., `https://docs.crewai.com`)

3. Wait for the documentation to be indexed. This may take a moment depending on the size of the documentation.

4. Start asking questions in the chat input field at the bottom.

5. To switch to a different documentation source, simply enter a new URL in the sidebar.

## Example Questions

Once you've connected to a documentation URL (e.g., CrewAI docs), you can ask questions like:

- "How do I create a new agent in CrewAI?"
- "What are the required parameters for the process method?"
- "Explain how tools work in CrewAI"
- "What is the difference between a crew and an agent?"

## Notes

- First-time indexing of documentation may take some time
- The quality of responses depends on the content and structure of the documentation
- For best results, use documentation websites with good semantic structure 