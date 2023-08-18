from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from utilities import llm
from langchain.prompts import PromptTemplate


class ConversationBot:
    def __init__(self, llm, prompt_template):
        self.llm = llm
        self.prompt_template = PromptTemplate.from_template(prompt_template)
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        self.conversation = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template,
            verbose=True,
            memory=self.memory
        )

    def respond(self, user_input):
        return self.conversation(user_input)


class ConversationBufferBot:
    def __init__(self, llm):
        self.llm = llm
        self.memory = ConversationBufferMemory()
        self.conversation_buffer = LLMChain(
            llm=self.llm,
            memory=self.memory
        )

    def converse(self, user_input):
        return self.conversation_buffer(user_input)


if __name__ == "__main__":
    prompt_template = """You are a nice chatbot having a conversation with a human.
    
    Previous conversation:
    {chat_history}
    
    New human question: {question}
    Response:"""

    conversation_bot = ConversationBot(llm=llm, prompt_template=prompt_template)
    user_input = "Can you tell me about the weather?"
    response = conversation_bot.respond(user_input)
    print("AI Response:", response)

    conversation_buffer_bot = ConversationBufferBot(llm=llm)
    conversation_buffer_bot.converse("good morning ai")
    print(conversation_buffer_bot.memory.buffer)
