import streamlit as st
import requests
import re

API_URL = "http://localhost:8001"

st.set_page_config(page_title="VLLM Function Generator", layout="wide")
st.title("⚡ VLLM Function Generator with LangChain")
query = st.text_input("Describe the function you want:", "reverse a string")
if st.button("Generate"):
    try:
        res = requests.get(f"{API_URL}/langchain", params={"query": query}).json()
        if "result" in res:
            content= res["result"]["content"].replace("\\n", "\n").replace("\\t", "\t")
            st.text("1. Try to extract code block if present")
            code_match = re.search(r"```python(.*?)```", content, re.DOTALL)
            st.text("code_match = " + str(code_match))
            if code_match:
                code = code_match.group(1).strip()
                st.subheader("📝 Generated Python Function")
                st.code(code, language="python")
        with st.expander("🔍 Full response details"):
                st.json(res)

    except Exception as e:
        st.error(f"⚠️ API error: {e}")

st.title("⚡ VLLM Sql Agent")
query2 = st.text_input("Describe the db question you want:", "list all tables")
if st.button("GenerateSql"):
    try:
        res = requests.get(f"{API_URL}/sql-agent", params={"query": query2}).json()
        st.subheader("📝 SQL Agent Response")
        st.json(res)

    except Exception as e:
        st.error(f"⚠️ API error: {e}")
        
# if st.button("Generate"):
#     # with col1:
#         st.subheader("LangChain Result")
#         try:
#             res = requests.get(f"{API_URL}/langchain", params={"query": query}).json()
#             st.code(res["result"], language="python")
#         except Exception as e:
#             st.error(str(e))

    # with col2:
    #     st.subheader("DSPy Result")
    #     try:
    #         res = requests.get(f"{API_URL}/dspy", params={"query": query}).json()
    #         st.code(res["result"], language="python")
    #     except Exception as e:
    #         st.error(str(e))
