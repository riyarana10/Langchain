from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from utilities import llm


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(", ")


class CommaSeparatedListGenerator:
    def __init__(self):
        template = """You are a helpful assistant who generates comma separated lists.
        A user will pass in a category, and you should generate 5 objects in that category in a comma-separated list.
        ONLY return a comma-separated list, and nothing more."""

        self.system_message_prompt = SystemMessagePromptTemplate.from_template(
            template)
        self.human_template = "{text}"
        self.human_message_prompt = HumanMessagePromptTemplate.from_template(
            self.human_template)

        self.chat_prompt = ChatPromptTemplate.from_messages(
            [self.system_message_prompt, self.human_message_prompt]
        )

        self.chain = LLMChain(
            llm=llm, prompt=self.chat_prompt, output_parser=CommaSeparatedListOutputParser()
        )

    def generate_list(self, category):
        output = self.chain.run(category)
        return output


# Usage example
def main():
    generator = CommaSeparatedListGenerator()
    category = "aimals"
    result = generator.generate_list(category)
    print(result)
    
if __name__ == "__main__":
    main()
