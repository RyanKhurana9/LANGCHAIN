from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)
document=['who is the president of the united states?',"who is the prime minister of India?","who is the president of France?"]
result=embedding.embed_documents(document)#embed_query is for a single query
#embed_documents is for a list of documents

print(str(result))