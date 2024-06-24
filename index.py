import streamlit as st
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLM
llm = LlamaCpp(
    model_path="llama-2-7b-chat.Q4_0.gguf",
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

# Create the LLM chain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit UI
st.title("Medical Code Chatbot")

question = st.text_input("Question", placeholder="Type your question here", help="Enter your medical question here.")

if st.button("Get Answer"):
    if question:
        # Run the LLM chain to get the answer
        answer = llm_chain.run(question)
        st.text_area("Answer", value=answer, placeholder="Answer will appear here", help="The answer to your question will be displayed here.", height=200)
    else:
        st.warning("Please enter a question before submitting.")
