# 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

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

openai_api_key = "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"

llm = OpenAI(openai_api_key=openai_api_key)
chat_model = ChatOpenAI(openai_api_key=openai_api_key)


llm_prediction = llm.predict("hi!")
print("LLM Prediction:", llm_prediction)

chat_prediction = chat_model.predict("hi!")
print("Chat Model Prediction:", chat_prediction)

text = "What would be a good company name for a company that makes colorful socks?"

llm_prediction1 = llm.predict(text)
print(llm_prediction1)

chat_prediction1 = chat_model.predict(text)
print(chat_prediction1)

message = [HumanMessage(content=text)]

llm_prediction2 = llm.predict_messages(message)
print(llm_prediction2)

chat_prediction2 = chat_model.predict_messages(message)
print(chat_prediction2)