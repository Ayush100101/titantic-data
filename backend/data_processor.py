import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv("LLAMA_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)  

# Define a prompt template for general questions
template = """Question: {question}
Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])

# Create an LLMChain for general questions using Groq
def get_groq_response(question: str):
    """
    Get a response from the Groq API for general questions.
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": question}],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,  
        stop=None,
    )
    return completion.choices[0].message.content

def process_question(question: str):
    """
    Processes the user's question and returns a response with text and/or visualization.
    """
    # Load the dataset
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    
    # Preprocess the dataset
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Handle specific questions
    if "percentage of passengers were male" in question.lower():
        male_percentage = (df['Sex'].value_counts(normalize=True)['male'] * 100).round(2)
        return {"response": f"{male_percentage}% of passengers on the Titanic were male."}

    elif "histogram of passenger ages" in question.lower():
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Age'].dropna(), bins=20, kde=True)
        plt.title("Histogram of Passenger Ages")
        plt.xlabel("Age")
        plt.ylabel("Count")
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
        plt.close()
        return {"response": "Here is the histogram of passenger ages:", "image": image_base64}

    elif "average ticket fare" in question.lower():
        avg_fare = df['Fare'].mean().round(2)
        return {"response": f"The average ticket fare on the Titanic was ${avg_fare}."}

    elif "passengers embarked from each port" in question.lower():
        embark_counts = df['Embarked'].value_counts()
        return {"response": f"Passengers embarked from each port:\n{embark_counts.to_string()}"}

    else:
        # Use Groq API for general questions
        response = get_groq_response(question)
        return {"response": response}
