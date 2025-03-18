#!/usr/bin/env python3
"""
Code Documentation Module

This module provides the run_agent function to interact with code documentation.
All Streamlit functionality has been removed and moved to app.py.
"""

from crewai_tools import CodeDocsSearchTool

def run_agent(docs_url=None):
    """
    Processes the docs_url and returns a confirmation string.
    This function is intended to be called from app.py.
    """
    if docs_url:
        tool = CodeDocsSearchTool(docs_url=docs_url)
        return f"Documentation from {docs_url} was successfully indexed. You can ask questions about it through the interface."
    else:
        return "Please provide a documentation URL to index."
