from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()#load environment variables from .env file basically it will load the api keyfrom .env file and make it avialbale in the environement variables
llm=OpenAI(model="gpt-3.5-turbo", temperature=0.9)
result=llm.invoke("how is the prime minister of india ")
print(result )