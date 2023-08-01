from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


class PromptTemplate:
    def __init__(self, input_variables, template):
        self.input_variables = input_variables
        self.template = template

    def format(self, **kwargs):
        return self.template.format(**kwargs)


def main():
    # Example prompts
    no_input_prompt = PromptTemplate(
        input_variables=[], template="Tell me a joke.")
    one_input_prompt = PromptTemplate(
        input_variables=["adjective"], template="Tell me a {adjective} joke.")
    multiple_input_prompt = PromptTemplate(
        input_variables=["adjective", "content"],
        template="Tell me a {adjective} joke about {content}."
    )

    # Output examples
    output1 = no_input_prompt.format()
    output2 = one_input_prompt.format(adjective="funny")
    output3 = multiple_input_prompt.format(
        adjective="funny", content="chickens")

    # Print the outputs
    print(output1)
    print(output2)
    print(output3)
    
    template = "You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    formatted_chat_prompt = chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")
    
    for message in formatted_chat_prompt:
        print(message.content)
