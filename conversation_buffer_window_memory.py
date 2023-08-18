from langchain.memory import ConversationBufferWindowMemory
from utilities import llm
from langchain.chains import ConversationChain


memory = ConversationBufferWindowMemory( k=1)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
print(memory.load_memory_variables({}))

memory = ConversationBufferWindowMemory( k=1, return_messages=True)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})
print(memory.load_memory_variables({}))

conversation_with_summary = ConversationChain(
    llm = llm,
    # We set a low k=2, to only keep the last 2 interactions in memory
    memory=ConversationBufferWindowMemory(k=4), 
    verbose=True
)

print(conversation_with_summary.predict(input="Hi, what's up?"))
print(conversation_with_summary.predict(input="What's their issues?"))
print(conversation_with_summary.predict(input="Is it going well?"))
print(conversation_with_summary.predict(input="What's the solution?"))




