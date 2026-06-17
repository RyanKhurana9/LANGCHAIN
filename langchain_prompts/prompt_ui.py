from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

# Google Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

# Load prompt from JSON
template = load_prompt("template.json")#template.json is file which contains the prompt template for the model to generate the response based on the user input 

if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)




'''if st.button('Summerize'):
   st.text('Generating response....')
    clear_button = st.button("clear")
    if clear_button:
        user_input = ""
    result=model.invoke(user_input)
    st.write(result.content)
     #to run streamplit run 
     # streamlit run prompt_ui.py
     ''' 
