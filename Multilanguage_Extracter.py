from dotenv import load_dotenv

load_dotenv () # load all env files

import streamlit as st 

import os
from PIL import Image
import  google.generativeai as genai

# Configure generative AI with Google API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load Gemini Pro Vision

model=genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read the files into bytes
        bytes_data=uploaded_file.getvalue()
        
        image_parts= [
            {
                "mime_type":uploaded_file.type, # get the mime type of the uploaded file
                "data":bytes_data
                   
            }   
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploded")
    

# initialize our streamlit app

st.title("Welcome to MultiLanguage Invoice Extractor")

st.header("MultiLanguage Invoice Extractor")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose an image of the invoice...",type=['jpg','png','jpeg'])

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)
    
    submit=st.button("Tell me about the invoice")
    
    input_prompt="""
    you are expert in understanding invoices. we will upload a image as invoice
    and you will have to answer any questions based on the uploaded invoice image
    """
    
    # if submit button is clicked
    if submit:
        image_data=input_image_details(uploaded_file)
        response = get_gemini_response(input_prompt,image_data,input)
        st.subheader("The Response is")
        st.write(response)
        
