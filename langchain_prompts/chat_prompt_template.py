from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
chat_template=ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert"),
    ('Human','explain in simple terms,what is {topic}')
])
'''chat_template=ChatPromptTemplate ([
    SystemMessage(content="You are a  helful {domain} expert"),
    HumanMessage(content="Explain in simple terms,what is {topic}")
])'''
prompt=chat_template.invoke({"domain":"cricket","topic":"LBW"})
print(prompt)