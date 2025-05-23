from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Returns the list of tools to be used within chatbot
    """
    tools = [TavilySearchResults(max_results= 3)]
    
    return tools

def create_tool_node(tools):
    """
    create and returns a tool node for the graph
    """
    return ToolNode(tools = tools)