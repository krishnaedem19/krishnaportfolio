@echo off
echo Starting Edem Krishna Chaithanya Portfolio...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)
call venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
pause
