from langchain import Wikipedia
from langchain.agents.react.base import DocstoreExplorer
from langchain.agents import Tool
from utilities import llm
from langchain.agents import initialize_agent
from langchain.callbacks import get_openai_callback

class LangChainDocstoreAgent:
    def __init__(self):
        self.docstore = DocstoreExplorer(Wikipedia())
        self.tools = [
            Tool(
                name="Search",
                func=self.docstore.search,
                description='search wikipedia'
            ),
            Tool(
                name="Lookup",
                func=self.docstore.lookup,
                description='lookup a term in wikipedia'
            )
        ]

        self.docstore_agent = initialize_agent(
            tools=self.tools,
            llm=llm,
            agent="react-docstore",
            verbose=True,
            max_iterations=1000
        )

    def run_docstore_agent(self, query):
        return self.docstore_agent(query)

if __name__ == "__main__":
    docstore_search_agent = LangChainDocstoreAgent()

    print(docstore_search_agent.run_docstore_agent("what was the first theorem given by Albert Einstein?"))
