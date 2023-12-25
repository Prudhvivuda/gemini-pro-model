# Q&A Chatbot

# Importing necessary libraries and modules
#from langchain.llms import OpenAI  # (Optional) Importing OpenAI module (commented out, not used in the code)
from dotenv import load_dotenv  # Importing the load_dotenv function from the dotenv module

load_dotenv()  # Loading environment variables from .env file

import streamlit as st  # Importing the Streamlit library
import os  # Importing the os module for interacting with the operating system
import pathlib  # Importing the pathlib module for working with file paths
import textwrap  # Importing the textwrap module for formatting text

# Importing the generative AI module from the google library
import google.generativeai as genai

# Importing display and Markdown from IPython for rendering output
from IPython.display import display
from IPython.display import Markdown

# Retrieving Google API key from environment variables (Note: This line does not have any effect unless the result is assigned to a variable or used)
os.getenv("GOOGLE_API_KEY")

# Configuring the generative AI module with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get responses
# Creating an instance of the GenerativeModel class
model = genai.GenerativeModel('gemini-pro')

# Starting a chat session with an empty history
chat = model.start_chat(history=[])

# Function to get responses from the chatbot
def get_gemini_response(question):
    
    # Sending a message to the chatbot and receiving a response
    response = chat.send_message(question, stream=True)
    return response

## Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

# Setting up the header for the Streamlit app
st.header("Gemini Application")

# Creating a text input box for user input
input = st.text_input("Input: ", key="input")

# Creating a button for submitting the question
submit = st.button("Ask the question")

# If the submit button is clicked
if submit:
    
    # Getting the response using the get_gemini_response function
    response = get_gemini_response(input)
    
    # Displaying the subheader for the response
    st.subheader("The Response is")
    
    # Printing each chunk of the response and adding a separator line
    for chunk in response:
        print(st.write(chunk.text))
        print("_" * 80)
    
    # Displaying the chat history
    st.write(chat.history)
