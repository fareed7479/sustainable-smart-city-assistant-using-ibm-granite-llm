import streamlit as st
import requests

API_URL = "http://localhost:8000/chat/ask"

def chat_assistant():
    st.markdown(
        """
        <style>
        .input-box {
            border-radius: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            width: 100%;
            box-sizing: border-box;
        }
        .response-box {
            border-radius: 10px;
            padding: 10px;
            background-color: #f0f2f6;
            margin-top: 10px;
            white-space: pre-wrap;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    query = st.text_area("Ask the Smart City Assistant:", height=100, key="chat_input", placeholder="Type your question here...", help="Enter your question and press Submit.")
    if st.button("Submit"):
        if query.strip():
            with st.spinner("Getting response..."):
                try:
                    response = requests.post(API_URL, json={"query": query})
                    if response.status_code == 200:
                        answer = response.json().get("response", "")
                        st.markdown(f'<div class="response-box">{answer}</div>', unsafe_allow_html=True)
                    else:
                        st.error(f"Error: {response.status_code} - {response.text}")
                except Exception as e:
                    st.error(f"Request failed: {str(e)}")
        else:
            st.warning("Please enter a question.")
