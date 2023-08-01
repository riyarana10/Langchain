from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

from utilities import llm


llm_prediction = llm.predict("hi!")
print("LLM Prediction:", llm_prediction)

chat_prediction = llm.predict("hi!")
print("Chat Model Prediction:", chat_prediction)

text = "What would be a good company name for a company that makes colorful socks?"

llm_prediction1 = llm.predict(text)
print(llm_prediction1)

chat_prediction1 = llm.predict(text)
print(chat_prediction1)

message = [HumanMessage(content=text)]

llm_prediction2 = llm.predict_messages(message)
print(llm_prediction2)

chat_prediction2 = llm.predict_messages(message)
print(chat_prediction2)