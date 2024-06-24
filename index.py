import streamlit as st
import base64

# Add custom CSS to change the background color to black
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stTextInput>div>div>input {
        color: white;
        background-color: #333;
    }
    .stTextArea>div>div>textarea {
        color: white;
        background-color: #333;
    }
    .stTextInput>div>div>label, .stTextArea>div>div>label {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Medical Code Chatbot")
question = st.text_input("Question", key="input1", placeholder="Type your question here", help="Enter your medical question here.")
answer = st.text_input("Answer", key="input2", placeholder="Answer will appear here", help="The answer to your question will be displayed here.")

if st.button("Get Answer"):
    if question:
        # Here you would call your model to get the answer (placeholder for now)
        # Replace the following line with your LLM code to get the answer
        answer = "This is a placeholder answer."  
        st.text_area("Answer", value=answer, placeholder="Answer will appear here", help="The answer to your question will be displayed here.", height=200)
    else:
        st.warning("Please enter a question before submitting.")
