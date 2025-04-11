from tavily import TavilyClient

def search(query):
    """
    Search for a query using the Tavily API.

    Args:
        query (str): The query string to search for.

    Returns:
        dict: The response from the Tavily API.
    """

    api_key = "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"
    tavily_client = TavilyClient(api_key)

    response = tavily_client.search(query=query)

    return response

