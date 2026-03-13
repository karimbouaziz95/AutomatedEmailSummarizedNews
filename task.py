import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

# Make a GET request to the NASA API
nasa_response = requests.get(url)

# Get the JSON content from the response
nasa_content = nasa_response.json()
title = nasa_content["title"]
url = nasa_content["url"]
explanation = nasa_content["explanation"]

# Download the image from the URL and save it locally
image_file_path = "nasa_image.jpg"
image_response = requests.get(url)
with open(image_file_path, "wb") as file:
    file.write(image_response.content)

# Display the title, image, and explanation using Streamlit
st.title(title)
st.image(image_file_path, caption=title)
st.write(explanation)