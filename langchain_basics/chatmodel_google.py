from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
result=model.invoke("write a a paragrah on Virat Kohli")
print(result.content)
# this model works on the google genai api and it is a chat model which is based on the gemini-2.5-flash-lite model. It is a very powerful model which can generate high quality responses. The result object contains the response from the model and the content attribute of the result object contains the actual response from the model.
from google.genai import Client
'''
client = Client()python -m pip list

models = client.list_models()
for m in models:
    print(m.name)
'''
