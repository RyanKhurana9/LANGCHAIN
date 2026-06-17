from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)
prompt=PromptTemplate(
    template='write me  a joke about the {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="explain me the joke in the following {text}",
    input_variables=['text']
)

parser=StrOutputParser()
chain=prompt|model|parser|prompt2|model|parser
result=chain.invoke({'topic':'Aerospace engineering'})
print(result)