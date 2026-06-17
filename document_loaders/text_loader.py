from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
model = ChatGoogleGenerativeAI( model="gemini-2.5-flash-lite", temperature=0.7)
prompt1=PromptTemplate(
    template="write a summary for the following poem{poem}",
    input_variables=['poem']
)
parser=StrOutputParser()



from langchain_community.document_loaders import TextLoader
loader=TextLoader('cricket.txt',encoding='utf-8')# create the loader object
docs=loader.load()
chain=prompt1|model|parser
result=chain.invoke({"poem":docs[0].page_content})
print(result)