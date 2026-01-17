"""
Skibidi-fication 3000 - TURBO MODE
Hack&Roll 2026 Demo Script

Uses GPT-5-nano for blazing fast brainrot translation.
Perfect for real-time PDF processing during your demo!
"""

import os

# IMPORTANT: Set API keys BEFORE importing
os.environ["OPENAI_API_KEY"] = "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"

os.environ["ELEVENLABS_API_KEY"] = "sk_d8a8306ae597845eafb1155a962a2311111ab229dce8453e"

# Now import after setting env vars
from brainrot_turbo import generate_brainrot_turbo

# Generate brainrot video using TURBO MODE (GPT-5-nano)
generate_brainrot_turbo("document.pdf")
