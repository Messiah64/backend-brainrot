#!/bin/bash

echo "========================================"
echo "SKIBIDI-FICATION 3000 - HACK&ROLL 2026"
echo "========================================"
echo ""

echo "[1/3] Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "[2/3] Starting backend API server..."
python backend_api.py &

sleep 3

echo ""
echo "[3/3] Opening frontend in browser..."
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:8000/frontend/app.html
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:8000/frontend/app.html
fi

echo ""
echo "========================================"
echo "System is ready! Check your browser."
echo "Backend API: http://localhost:8000"
echo "Frontend: http://localhost:8000/frontend/app.html"
echo "========================================"
