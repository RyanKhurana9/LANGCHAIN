from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)
prompt1=PromptTemplate(
    template="write me a report about the {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="write a summmary of the following{text}",
    input_variables=['text']
)
parser=StrOutputParser()
report_gen_chain=RunnableSequence(prompt1,model,parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)
final_chain=RunnableSequence(report_gen_chain,branch_chain)
result=final_chain.invoke({"topic":"F-35"})
print(result)