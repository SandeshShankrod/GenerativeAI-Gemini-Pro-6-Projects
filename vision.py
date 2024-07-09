import streamlit as st
from PIL import Image
import pathlib
import textwrap

import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyBWBMlQ-vmWaLBd4V1y4g9vpzvn5bNUwHY'

import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# function

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    
    if input != "":
         response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
      
    return response.text  

# streamlit we will initialize

st.set_page_config(page_title = 'IMAGE CREATION')

st.header('GEMINI AI IMAGE APP ANALYSIS')

input = st.text_input('Input prompt :', key = 'input')

upload_file = st.file_uploader('choose an image', type = ['jpg','jpeg','png'])

image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption='Upload Image', use_column_width = True)
    
submit = st.button('Explain breif about image')  

if submit:
    response = get_gemini_response(input, image)
    st.subheader('The response is ') 
    st.write(response)

