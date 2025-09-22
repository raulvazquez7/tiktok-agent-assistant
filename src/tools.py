"""Module for defining the tools available to the agent."""

from langchain_tavily import TavilySearch
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# 1. Web Search Tool
# This tool allows the agent to search the web for up-to-date information.
# We initialize it with k=3 to get the top 3 search results.
web_search_tool = TavilySearch(k=3, name="web_search")

web_search_tool.description = (
    "A search engine useful for searching the web for information on nutrition, "
    "content trends, and other relevant topics."
)
