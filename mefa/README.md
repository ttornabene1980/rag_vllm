# rag_vllm

cd mefa
python3  -m venv .mefaenv 
source .env/bin/activate
pip install uv
uv pip install  -r pyproject.toml

cd /Users/tindarotornabene/develop/sorgente/rag_vllm
export PYTHONPATH=$(pwd)
streamlit run mefa/dashboard/app.py

streamlit run  dashboard/app.py