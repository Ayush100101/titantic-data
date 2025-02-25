import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.title("Titanic Dataset Chatbot")

user_input = st.text_input("Ask me anything about the Titanic dataset:")

if user_input:
    response = requests.post("https://titantic-data.onrender.com/ask/", json={"question": user_input})
    if response.status_code == 200:
        result = response.json()
        st.write(result["response"])
        if "image" in result:
            image_data = base64.b64decode(result["image"])
            image = Image.open(BytesIO(image_data))
            st.image(image, caption="Visualization", use_column_width=True)
    else:
        st.error("Failed to get response from the server.")
