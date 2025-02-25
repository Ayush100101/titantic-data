import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get backend URL and port from environment variables, with a default fallback
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1")
BACKEND_PORT = os.getenv("BACKEND_PORT", "10000")  # Default port is 10000
API_ENDPOINT = f"{BACKEND_URL}:{BACKEND_PORT}/ask/"

st.title("Titanic Dataset Chatbot")

user_input = st.text_input("Ask me anything about the Titanic dataset:")

if user_input:
    response = requests.post(API_ENDPOINT, json={"question": user_input})
    
    if response.status_code == 200:
        result = response.json()
        st.write(result["response"])
        
        if "image" in result:
            image_data = base64.b64decode(result["image"])
            image = Image.open(BytesIO(image_data))
            st.image(image, caption="Visualization", use_column_width=True)
    else:
        st.error("Failed to get response from the server.")
