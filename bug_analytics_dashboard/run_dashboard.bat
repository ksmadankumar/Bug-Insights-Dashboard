
@echo off
echo Installing requirements...
pip install -r requirements.txt

echo Starting dashboard...
streamlit run dashboard/app.py

pause
