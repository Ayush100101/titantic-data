# Titanic Dataset Chatbot

This project is a chatbot that analyzes the Titanic dataset. Users can ask questions in natural language and receive text responses along with visualizations.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/titanic_chatbot.git
   cd titanic_chatbot
   ```

2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

3. Set up the frontend:
   ```bash
   cd ../frontend
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```

## Usage
- Open the Streamlit app in your browser.
- Ask questions about the Titanic dataset.