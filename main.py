import requests
from API_KEY import API_KEY
from send_email import send_email


url = (
    f"https://newsapi.org/v2/everything?"
    f"q=tesla&"
    f"from=2026-02-08&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)
# Make a GET request to the API
response = requests.get(url)

# Get the JSON content from the response
content = response.json()

email_content = ""

for article in content["articles"]:
    email_content += (
        f"Title: {article['title']}\n"
        f"Description: {article['description']}\n"
        f"URL: {article['url']}\n\n"
    )

send_email(
    message=email_content,
    subject="Daily News Update"
)