from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4")
result=model.invoke("what is the capital of INDIA")
print(result.content)#content is the attribute of the response object which contains the actual respose of the model. 