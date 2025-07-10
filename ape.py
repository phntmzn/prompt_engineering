from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4", temperature=0)

prompt = PromptTemplate(
    input_variables=["description"],
    template="""
You are a software engineer. Generate a Python CLI tool given this description:

{description}

Include:
- argparse setup
- docstrings
- one example function
- a basic main() method
""")

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("A CLI that parses a CSV file and computes column averages.")
print(response)

from langchain.chains import SimpleSequentialChain

test_prompt = PromptTemplate(
    input_variables=["code"],
    template="""
Write pytest unit tests for the following Python code:

{code}
"""
)

test_chain = LLMChain(llm=llm, prompt=test_prompt)

multi_chain = SimpleSequentialChain(chains=[chain, test_chain], verbose=True)
multi_chain.run("A script that fetches weather data from an API and prints it.")
