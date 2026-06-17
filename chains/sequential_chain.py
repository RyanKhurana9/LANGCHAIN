from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
)
prompt1=PromptTemplate(
    template="write  a detailed report{topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="write a 5 point  summary on the provided\n{text}",
    input_variables=['text']
)
parser=StrOutputParser()
chain=prompt1|model|parser|prompt2|model|parser  
result=chain.invoke({'topic':"WW2"})
print(result)
chain.get_graph().print_ascii() 