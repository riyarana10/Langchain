from langchain.agents import initialize_agent, Tool
from utilities import llm
from langchain import SerpAPIWrapper

class LangChainSearchAgent:
    def __init__(self, serpapi_api_key):
        self.serpapi_wrapper = SerpAPIWrapper(serpapi_api_key=serpapi_api_key)
        
        self.tools = [
            Tool(
                name="Intermediate Answer",
                func=self.serpapi_wrapper.run,
                description='google search'
            )
        ]

        self.self_ask_agent = initialize_agent(
            tools=self.tools,
            llm=llm,
            agent="self-ask-with-search",
            verbose=True,
            max_iterations=3
        )

    def run_self_ask_agent(self, query):
        return self.self_ask_agent(query)

if __name__ == "__main__":
    serpapi_api_key = 'd86887155391f0fb55e77339443a576faf34773cb18b8a7c6631a6a9f875852a'
    search_agent = LangChainSearchAgent(serpapi_api_key)

    print(search_agent.run_self_ask_agent("who live longer, Akbar or Babar?"))
