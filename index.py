import streamlit as st

st.title("Medical Code Chatbot")
question = st.text_input("Question", key="input1", placeholder="Type your question here", help="Enter your medical question here.")
answer = st.text_input("Answer", key="input2", placeholder="Answer will appear here", help="The answer to your question will be displayed here.")
