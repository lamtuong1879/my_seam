import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import os
from carved import seam_carve
# from seam1 import resize_image
import base64
import cv2

st.title('RESIZE IMAGE')

# get file to downloda
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    col1, col2 = st.beta_columns(2)
    with col1:
      file_details = {"FileName":image_file.name,"FileType":image_file.type, "FileSize":image_file.size}
      st.write(image_file.name)
      # st.write(image_file.size)
      img = Image.open(image_file)
      
      st.image(img)
      st.write(img.size)
      with open(os.path.join("tempDir",'input.jpeg'),"wb") as f: 
        f.write(image_file.getbuffer())         
    # st.success("Saved File")
    genre = st.radio("Choose:", ('Horizontal', 'Vertical', 'Both'))
    img = cv2.imread('tempDir/input.jpeg').astype(np.float64)
    print(img)
    numSeams = st.slider('', -10, 10, 0)
    print(numSeams)
    if genre == 'Horizontal':
      seam_carve(img, numSeams, 0,  None, False)
    elif genre == 'Vertical':
      seam_carve(img, 0, numSeams, None, False)
    else:
      seam_carve(img, numSeams, numSeams,  None, False)

    carved_img = Image.open('./tempDir/carved.jpeg')
    if carved_img:
      with col2:
        if numSeams > 0 or numSeams < 0:
          carved_img = Image.open('./tempDir/carved.jpeg')
          st.write("Carved image")
          st.image(carved_img.convert('RGB'), width=None)
          st.write(carved_img.size)
      st.markdown(get_binary_file_downloader_html('./tempDir/carved.jpeg', 'Carved Image'), unsafe_allow_html=True)
