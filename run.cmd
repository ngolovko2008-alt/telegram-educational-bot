@echo off
rem run.cmd — activate virtualenv (venv or .venv) and run the bot
rem Usage: double-click or run from cmd in project root

cd /d "%~dp0"

if exist "venv\Scripts\activate.bat" (
    call "venv\Scripts\activate.bat"
) else if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
) else (
    echo No virtual environment found in venv\ or .venv\
    echo Create one with: python -m venv venv
    pause
    exit /b 1
)

echo Using Python: "%~dp0"
python -u src\bot.py

echo Bot process ended. Press any key to close this window.
pause
