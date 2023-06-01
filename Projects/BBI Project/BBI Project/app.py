# Importing the necessary libraries
import streamlit as st
import pathlib 
import platform
from fastai.vision.all import * 

# Setting up the platform-dependent functionality for file paths
plt = platform.system()
if plt == 'Windows':
    pathlib.PosixPath = pathlib.WindowsPath

# Displaying the title on the Streamlit application
st.title('BBI Classification Project')

st.warning("BBI (Bear, Bird, Insect) Classification Project identifies images as bear, bird or insect. Because the model is trained with a limited number of images, there may be some errors. The program is designed to apply the lessons learned in practice")

# Creating a file uploader component to allow users to upload an image
pic = st.file_uploader("Upload image", type=['png', 'jpg', 'jpeg', 'gif', 'svg']) 

if pic:
    # Displaying the uploaded image on the Streamlit application
    st.image(pic)   

     # Creating a PIL image object from the uploaded image data
    img = PILImage.create(pic)
    # Loading a pre-trained model from a file
    model = load_learner('bbi_model.pkl')

    # Making a prediction using the loaded model
    pred, pred_id, probs = model.predict(img)

    # Displaying the predicted label on the Streamlit application as a success message
    st.success(f'Prediction: {pred}')

    # Displaying the probability of the predicted label as an informational message
    st.info(f'Probability: {probs[pred_id]*100:.1f}%') 
