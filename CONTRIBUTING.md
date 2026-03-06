# Contributing to SpotifyLocalPrep

Thanks for your interest in contributing! Here's how to get set up for development.

## Dev setup

```bash
git clone https://github.com/YOUR_USERNAME/spotify-local-prep.git
cd spotify-local-prep
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate.bat on Windows
pip install -r requirements.txt
python main.py
```

## Project layout

- `app/core/` — all business logic (no GUI imports allowed here)
- `app/gui/` — all CustomTkinter widgets and windows
- `app/utils/` — shared utilities (logging, validators)

## Guidelines

- Keep GUI logic out of `core/` modules
- Add a docstring to every new function/class
- Test manually with a variety of audio formats before submitting a PR
- If adding a new dependency, add it to `requirements.txt` with a comment explaining why
