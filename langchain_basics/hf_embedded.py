from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')# the model name that we are using for embedding 

documents = [#the document that we want to embed
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
result=embedding.embed_documents(documents)#embedding the documents and storing the result in a variable called result
print(str(result))#converting the result to string and printing it out

