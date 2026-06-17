from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader('dl-curriculum.pdf')
docs=loader.load()
print(len(docs))# number of pages
print(docs[0].metadata)
print(docs[0].page_content)