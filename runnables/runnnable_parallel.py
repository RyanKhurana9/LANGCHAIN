from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)
prompt1=PromptTemplate(
    template="generate a tweet about the {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="generate a linkdein post about the {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()
parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,parser),
    "linkdein":RunnableSequence(prompt2,model,parser)
}
)
result=parallel_chain.invoke({"topic":"US-Iran conflict"})
print(result['tweet'])
print(result['linkdein'])
parallel_chain.get_graph().print_ascii#explains the workflow 
