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


# Retrieving Google API key from environment variables
os.getenv("GOOGLE_API_KEY")

# Configuring the generative AI module with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and get responses
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')  # Creating an instance of the GenerativeModel class
    response = model.generate_content(question)  # Generating content based on the input question
    return response.text  # Returning the generated response

# Initializing the Streamlit app
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
    
    # Displaying the generated response
    st.write(response)
