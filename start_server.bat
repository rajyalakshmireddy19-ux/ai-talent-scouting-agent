@echo off
echo.
echo ========================================
echo   AI TALENT SCOUTING AGENT - STARTUP
echo ========================================
echo.
echo Starting web server...
echo.
echo Once started, open your browser to:
echo   http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload