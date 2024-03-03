import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("Easy OCR - Extract Text from Images")

#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` -  hosted on 🤗 Spaces")

st.markdown("Used Github Actions to automatically build the app on any updates on [this github repo link](https://github.com/deepanshu2207/imgtotext)")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_resource
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 


reader = load_model() #load model


if image is not None:
    print('1. Image Added')
    input_image = Image.open(image) #read image
    print('2. Image Opened')
    st.image(input_image) #display image
    print('3. Image Showed')

    with st.spinner("🤖 AI is at Work! "):
        print(np.array(input_image))
        result = reader.readtext(np.array(input_image))
        print('4. Image Text Read')

        result_text = [] #empty list for results

        print(result)
        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @deepanshu2207. Credits to 🤗 Spaces for Hosting this ")