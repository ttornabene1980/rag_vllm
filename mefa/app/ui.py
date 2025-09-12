import streamlit as st
import requests

API_URL = "http://orchestrator:8000"

st.set_page_config(page_title="LLM Function Generator", layout="wide")

st.title("⚡ LLM Function Generator with LangChain & DSPy")

query = st.text_input("Describe the function you want:", "reverse a string")

col1, col2 = st.columns(2)

if st.button("Generate"):
    with col1:
        st.subheader("LangChain Result")
        try:
            res = requests.get(f"{API_URL}/langchain", params={"query": query}).json()
            st.code(res["result"], language="python")
        except Exception as e:
            st.error(str(e))

    with col2:
        st.subheader("DSPy Result")
        try:
            res = requests.get(f"{API_URL}/dspy", params={"query": query}).json()
            st.code(res["result"], language="python")
        except Exception as e:
            st.error(str(e))
