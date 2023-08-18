from utilities import llm
from langchain.chains import LLMMathChain
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.agents import Tool
from langchain.agents import initialize_agent

class LangChainAgent:
    def __init__(self):
        self.llm = llm

        self.llm_math = LLMMathChain(llm=self.llm)

        self.prompt = PromptTemplate(
            input_variables=["query"],
            template="{query}"
        )

        self.memory = ConversationBufferMemory(memory_key='chat_history')

        self.llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)

        self.tools = []
        self.tools.append(
            Tool(
                name='Calculator',
                func=self.llm_math.run,
                description='useful for when you need to answer questions about math'
            )
        )
        self.tools.append(
            Tool(
                name='Language Model',
                func=self.llm_chain.run,
                description="use this tool for general purpose queries and logic"
            )
        )

        self.zero_shot_agent = initialize_agent(
            agent="zero-shot-react-description",
            tools=self.tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3
        )

        self.conversational_agent = initialize_agent(
            agent='conversational-react-description',
            tools=self.tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3,
            memory=self.memory
        )

    def run_zero_shot_agent(self, query):
        return self.zero_shot_agent(query)

    def run_conversational_agent(self, query):
        return self.conversational_agent(query)

if __name__ == "__main__":
    langchain_agent = LangChainAgent()

    print(langchain_agent.run_zero_shot_agent("what is (4.5*2.1)^2.2 ?"))
    print(langchain_agent.run_zero_shot_agent("what is the capital of India?"))
