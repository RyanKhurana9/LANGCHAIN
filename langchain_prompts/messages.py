from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chathistory=[
    SystemMessage("You are helpful AI assistant"),

]
model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.7  
)
messages=[
    SystemMessage(content="you are a helpfull assistant"),
    HumanMessage("How to invoke langchain model")
]
response=model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages )


 