from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
#ChatPromptTemplate=>class lets us define structured prompt with systen messages,human messages,AI
#MessagePlaceholder=>dynamcially insert previous chat history or conversation context
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),#placeholder for previous chat history for context 
    ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)