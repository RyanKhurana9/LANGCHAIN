from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.7
)
#here we invoke the model by 
chat_history=[SystemMessage("You are a helpful AI assistant")]
while(True):
    user_input=input("You:")
    if(user_input=="exit"):
        break
    chat_history.append(HumanMessage(content=user_input))
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
print("Chat HISTORY")
print("="*1000)
print(chat_history)
