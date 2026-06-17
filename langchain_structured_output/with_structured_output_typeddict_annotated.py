from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict,Annotated
model=ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-lite',
    temperature=0.7
)
class Review(TypedDict):
    summary:Annotated[str,"Generate a small summary"]
    sentiment:Annotated[str,'return the sentiment of the review posstive,negative or neutral']
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""The smartphone delivers a strong all-round performance, making it a reliable choice for everyday use. Its sleek and modern design feels comfortable in hand, with a solid build quality that gives a premium impression even at a moderate price point""")
print(result['summary'])
print(result['sentiment'])