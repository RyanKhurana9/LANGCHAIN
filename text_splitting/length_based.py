from langchain_text_splitters import CharacterTextSplitter
text="""LangChain is a framework designed to help developers build applications powered by large language models.
It provides modular components for document loading, text splitting, embeddings, vector stores, and chains.

Text splitting is a critical preprocessing step.
Large documents such as PDFs, research papers, and books must be divided into smaller chunks so that
language models can process them efficiently without exceeding context limits.

Length-based splitting divides text purely based on size.
Semantic splitting, on the other hand, attempts to preserve meaning by splitting on sentences or topics.

Choosing the right chunk size and overlap is important.
Too small, and you lose context.
Too large, and you risk token overflow."""
splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=0,separator='')
result=splitter.split_text(text)
print(result)