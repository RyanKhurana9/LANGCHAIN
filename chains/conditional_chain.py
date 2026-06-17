from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Literal

# Load API key
load_dotenv()#our env file contains the api key

# Output schema
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the feedback"
    )

# Parser
parser = PydanticOutputParser(pydantic_object=Feedback)

# Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.4
)
# in normal prompt we lack the control as Normally LLM can hallucinate 
# Prompt
prompt = PromptTemplate(# we prefer using pydantic in order to prevent the llm to hallucinate
    template="""Classify the following feedback as positive or negative. 

Feedback:
{feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Chain
classifier_chain = prompt | model | parser

# Invoke
result = classifier_chain.invoke(
    {"feedback": "this is a terrible smartphone"}
)

print(result.sentiment)  # negative