# SUPERVISOR AGENT

## IMPORT DEPENDENCIES
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage

from pydantic import BaseModel


## CONSTANTS
MODEL_NAME = ""
TASK = "text-generation"
MAX_NEW_TOKENS = 512
TEMPERATURE = 0.1

## INITIALIZE LLM
llm = HuggingFaceEndpoint(
    repo_id = MODEL_NAME,
    task = TASK,
    max_new_tokens=MAX_NEW_TOKENS,
    temperature=TEMPERATURE
)

## INITIALIZE CHATMODEL
model = ChatHuggingFace(llm=llm)

## INITALIZE STATE
class AgentState(BaseModel):
    pass


## SYSTEM MESSAGE
system_message = f""" """


def supervisor_agent(state:AgentState):
    pass