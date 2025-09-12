from fastapi import FastAPI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
# import dspy
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
# from guardrails import Guard
from langchain.agents import initialize_agent,AgentType

# FastAPI app
app = FastAPI()

db = SQLDatabase.from_uri("postgresql+psycopg2://sorgente:sorgente@192.168.1.98:5432/sorgente")
 
 # Define a simple Guardrail schema
rail_spec = """
# Output must be JSON with:
{
  "function_name": "str",
  "code": "str"
}
"""

# LangChain -> vLLM via OpenAI API
llm = ChatOpenAI(
    model="deepseek-coder-1.3b-instruct",
    openai_api_base="http://192.168.1.98:8000/v1",
    openai_api_key="EMPTY"  # vllm ignores this
)
# llm = VLLM(model="TheBloke/Llama-2-7b-chat-hf", trust_remote_code=True)

# guard = Guard.from_rail_string(rail_spec, llm=llm)

# class FunctionWriter(dspy.Signature):
#     task = dspy.InputField()
#     code = dspy.OutputField()

# def generate_code(task: str) -> str:
#     response = guard(task)
#     return response["code"]

# generator = dspy.ChainOfThought(FunctionWriter, fn=generate_code)
# print(generator(task="reverse a string").code)


sql_agent_executor = create_sql_agent(llm=llm, db=db, agent_type="openai-tools"  , verbose=True)
# //crawl_web
tools = [sql_agent_executor]
# agent = initialize_agent(
#     tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
# )

@tool("crawl_web")
def crawl_web(url: str) -> str:
    """Fetch and extract text from a web page"""
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.get_text()[:2000]  # limit for token safety


@app.get("/langchain")
def use_langchain(query: str):
    prompt = PromptTemplate(template="Write a Python function that {task}", input_variables=["task"])
    chain = prompt | llm
    return {"result": chain.invoke({"task": query})}

# # DSPy -> same vLLM endpoint
# dspy.settings.configure(
#     lm=dspy.LM("openai/deepseek-coder-1.3b",
#                api_base="http://vllm-deepseek:8000/v1",
#                api_key="EMPTY")
# )

# @app.geresult": response }

# @app.get("/dspy")
# def use_dspy(query: str):
#     class FunctionWriter(dspy.Signature):
#         """Write a Python function."""
#         task = dspy.InputField()
#         code = dspy.OutputField()
#     generator = dspy.ChainOfThought(FunctionWriter)
#     return {"result": generator(task=query).code}
