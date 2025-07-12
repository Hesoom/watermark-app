# Watermark App

A simple Python app to add a PNG logo watermark to an image using CustomTkinter and Pillow.

## Features
- Load an image
- Add a transparent logo (PNG)
- Save the watermarked image

## How to Run
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate on Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
## Requirements
Python 3.10+
Pillow
customtkinter

## Notes
Only transparent .png logos are supported.
Final image can be saved as .jpg or .png.
