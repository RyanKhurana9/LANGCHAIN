from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=GoogleGenerativeAIEmbeddings(model='models/text-embedding-3-large', dimensions=32)
result=embedding.embed_query("who is the president of the united states?")
print(str(result))