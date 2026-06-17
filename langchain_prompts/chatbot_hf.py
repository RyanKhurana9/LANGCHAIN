from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()
pipe=pipeline(
    "text-generation",
    model='haykgrigorian/TimeCapsuleLLM-v2-llama-1.2B',
    max_new_tokens=256,
    temperature=0.7
)
model=HuggingFacePipeline(pipeline=pipe)
while(True):
    user_input=input("YOU:")
    if user_input.lower() in['exit','quit']:
        print("Exiting the Chatbot.GOODBYE!")
        break
    response=model.invoke(user_input)
    print("AI:", response.content)
