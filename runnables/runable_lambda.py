from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
from dotenv import load_dotenv
load_dotenv()
def word_count(text):
    return len(text.split())
runnable_word_count=RunnableLambda(word_count)
parser=StrOutputParser()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)
prompt1=PromptTemplate(
    template="write me a joke about the(single short joke and make everyone laugh ROFL) {topic}",
    input_variables=['topic']
)
joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),# we do it bcz we want the joke to be also printed as the Runnable pass through just print the input as the output
    "word_count":runnable_word_count
}
)
finalchain=RunnableSequence(joke_gen_chain,parallel_chain)
result=finalchain.invoke({"topic":"us navyseals"})
print(result)