from tavily import TavilyClient
from marko import convert

api_key = "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"
tavily_client = TavilyClient(api_key)

response = tavily_client.search(query="hey how to kserve for llama4.1")

web_text = ""
for result in response["results"]:
    for key, value in result.items():
        web_text += f"### {key}\n {value}\n\n"
    web_text += "----\n"

print(convert(web_text))