import requests
from API_KEY import API_KEY

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

for article in content["articles"]:
    print(article["title"])
    print("------------------------")