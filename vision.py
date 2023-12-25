# Q&A Chatbot

# Importing necessary libraries and modules
#from langchain.llms import OpenAI  # (Optional) Importing OpenAI module (commented out, not used in the code)
from dotenv import load_dotenv  # Importing the load_dotenv function from the dotenv module

load_dotenv()  # Loading environment variables from .env file

import streamlit as st  # Importing the Streamlit library
import os  # Importing the os module for interacting with the operating system
import pathlib  # Importing the pathlib module for working with file paths
import textwrap  # Importing the textwrap module for formatting text
from PIL import Image  # Importing the Image module from the Pillow library for working with images

# Importing the generative AI module from the google library
import google.generativeai as genai

# Retrieving Google API key from environment variables (Note: This line does not have any effect unless the result is assigned to a variable or used)
os.getenv("GOOGLE_API_KEY")

# Configuring the generative AI module with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get responses
def get_gemini_response(input, image):
    # Creating an instance of the GenerativeModel class
    model = genai.GenerativeModel('gemini-pro-vision')
    
    # Checking if the input is not an empty string
    if input != "":
        # Generating content based on both input text and image
        response = model.generate_content([input, image])
    else:
        # Generating content based only on the image
        response = model.generate_content(image)
    
    # Returning the generated response
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

# Setting up the header for the Streamlit app
st.header("Gemini Application")

# Creating a text input box for the input prompt
input = st.text_input("Input Prompt: ", key="input")

# Creating a file uploader for choosing an image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""  # Initializing an empty string for the image variable

# If an image is uploaded
if uploaded_file is not None:
    # Opening the uploaded image file using the Image module
    image = Image.open(uploaded_file)
    # Displaying the uploaded image
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Creating a button for submitting the request to the chatbot
submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    # Getting the response using the get_gemini_response function
    response = get_gemini_response(input, image)
    # Displaying the subheader for the response
    st.subheader("The Response is")
    # Displaying the generated response
    st.write(response)
