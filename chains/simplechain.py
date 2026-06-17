from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
)
prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)


parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'Nuclear missile'})
chain.get_graph().print_ascii()#help to show pipeline
'''
python3 -m pip install grandalf use this to use get_graph

'''

