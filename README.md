# NewsAPIEmail

This project fetches recent business news from NewsAPI, asks Gemini to generate a short analysis, and emails the summary.

It also includes a separate Streamlit script that displays NASA's Astronomy Picture of the Day.

## Project Files
- `main.py`: Fetches news, generates an AI summary with Gemini, and sends it by email.
- `send_email.py`: Reusable Gmail sender utility (SMTP over SSL).
- `task.py`: Streamlit mini-app for NASA APOD.

## Requirements
- Python 3.8+
- A NewsAPI key
- A Google Gemini API key
- A Gmail account with an app password
- A NASA API key (only for `task.py`)

## Installation
1. Create and activate a virtual environment (recommended).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. If you want to run the NASA Streamlit script, install Streamlit:

```bash
pip install streamlit
```

## Environment Variables
Create a `.env` file in the project root with:

```env
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
EMAIL_ADDRESS=your_gmail_address
EMAIL_APP_EXAMPLE_PASSWORD=your_gmail_app_password
NASA_API_KEY=your_nasa_api_key
```

Notes:
- `EMAIL_APP_EXAMPLE_PASSWORD` is the exact variable name currently used by the code.
- `NASA_API_KEY` is only needed for the Streamlit script.

## Usage

### 1. Generate and email daily business summary

```bash
python main.py
```

What it does:
- Pulls English news from NewsAPI.
- Sends the article list to Gemini (`gemini-3-flash-preview`) for a two-paragraph analysis.
- Emails the generated summary using Gmail SMTP.

### 2. Run the NASA APOD Streamlit app

```bash
streamlit run task.py
```

This script fetches NASA's Astronomy Picture of the Day and displays the title, image, and explanation.

## Current Defaults in `main.py`
- Topic is hardcoded as `business`.
- The NewsAPI query uses `from=2026-02-15`.
- The email receiver defaults to `karim.bouaziz@rwth-aachen.de` in `send_email.py`.

## Troubleshooting
- If email sending fails, confirm Gmail app password setup and `.env` values.
- If Gemini fails, verify `GEMINI_API_KEY` and billing/access for the selected model.
- If NewsAPI returns no articles, check API key, quota, and query dates.