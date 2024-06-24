import streamlit as st
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LlamaCpp model
llm = LlamaCpp(
    model_path="downloads/llama-2-7b-chat.Q4_0.gguf",
    n_gpu_layers=40,
    n_batch=512,
    verbose=False
)

# Define the prompt template
template = """
Question: {question}

Answer:
"""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create an LLM chain with the prompt and the LLM
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit application
st.title("Medical Code Chatbot")

# Input for the user's question
question = st.text_input("Question", key="input1", placeholder="Type your question here", help="Enter your medical question here.")

# Display the answer when the question is submitted
if question:
    answer = llm_chain.run(question)
    st.text_area("Answer", value=answer, key="input2", placeholder="Answer will appear here", help="The answer to your question will be displayed here.", height=200)
