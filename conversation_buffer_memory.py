from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from utilities import llm

# memory = ConversationBufferMemory()
# memory.save_context({"input": "hi"}, {"output": "whats up"})
# print(memory.load_memory_variables({}))


# memory = ConversationBufferMemory(return_messages=True)
# memory.save_context({"input": "hi"}, {"output": "whats up"})

# print("load memory varialble")
# print(memory.load_memory_variables({}))

# print("\n")

conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=ConversationBufferMemory()
)

print(conversation.predict(input="Hi there!"))
print(conversation.predict(input="I'm doing well! Just having a conversation with an AI."))
print(conversation.predict(input="Tell me about yourself."))
