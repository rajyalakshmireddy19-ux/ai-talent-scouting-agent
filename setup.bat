@echo off
echo Setting up AI Talent Scouting Agent...

echo.
echo 1. Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 2. Setup complete!
echo.
echo To run the application:
echo   python main.py
echo.
echo Then open your browser to: http://localhost:8000
echo.
echo Note: For full AI engagement features, add your OpenAI API key to .env file
echo.
pause