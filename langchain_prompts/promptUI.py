from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt, PromptTemplate
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7,
)
st.header("RESARCH TOOL")
paper_input = st.selectbox(
    "Select Reseach Paper Name",
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
length_input=st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)
prompt = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
You are an expert research assistant.

Explain the research paper titled "{paper_input}" in a {style_input} style.

The explanation should be {length_input}.

Make it clear, structured, and accurate.
"""
)
if st.button("Summarize"):
    chain=prompt|model
    result=chain.invoke({
        "paper_input":paper_input,
        "style_input":style_input,
        "length_input":length_input
    })
    
    st.write(result.content)
