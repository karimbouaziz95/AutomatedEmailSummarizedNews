import requests
import os
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

from send_email import send_email

load_dotenv()

# Load API keys from environment variables
API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

topic = "business"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={topic}&"
    f"from=2026-02-15&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}&"
    f"language=en"
)
# Make a GET request to the API
request = requests.get(url)

# Get the JSON content from the response
content = request.json()

# Extract the articles from the content
articles = content["articles"]

# Initialize the Gemini model
model = init_chat_model(
    model="gemini-3-flash-preview", 
    model_provider="google-genai",
    api_key = GEMINI_API_KEY
)

prompt = f"""
You are a news summarizer. 
Write a short paragraph analyzing those news.
And add another second paragraph to tell me how they affect 
the stock market.
Here are news articles:
{articles}
"""

# Invoke the model with the prompt and get the response
response = model.invoke(prompt)
response_str = response.content[0]["text"]

# Send the response via email
send_email(
    message=response_str,
    subject=f"Daily {topic.capitalize()} News Update"
)