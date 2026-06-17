from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.7  
)
chat_history=[]
while(True):
    user_input=input("You: ")
    if user_input.lower() in['exit','quit']:
        print("Exiting the Chatbot.GOODBYE!")
        break
    response=model.invoke(user_input)
    chat_history.append(response.content)
    print("AI:", response.content)
print(chat_history)

     