from langchain.prompts import PromptTemplate
from langchain.prompts.chat import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
formatted_prompt = prompt.format(product = "colorful socks")

print(formatted_prompt)

template = "You are a helpful assistant that translates {input_language} to {output_language}."
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_messsage_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.format_messages([system_message_prompt,human_messsage_prompt])
formatted_chat_promot = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

for mssg in formatted_chat_promot:
    print(mssg.content)


