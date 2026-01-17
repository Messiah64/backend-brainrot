@echo off
echo ========================================
echo SKIBIDI-FICATION 3000 - HACK&ROLL 2026
echo ========================================
echo.

echo [1/3] Installing dependencies...
pip install -r requirements.txt

echo.
echo [2/3] Starting backend API server...
start cmd /k "python backend_api.py"

timeout /t 3 /nobreak >nul

echo.
echo [3/3] Opening frontend in browser...
start http://localhost:8000/frontend/app.html

echo.
echo ========================================
echo System is ready! Check your browser.
echo Backend API: http://localhost:8000
echo Frontend: http://localhost:8000/frontend/app.html
echo ========================================
pause
