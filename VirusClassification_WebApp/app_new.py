import streamlit as st 

from PIL import Image

import numpy as np 
import pandas as pd 
import joblib

model = joblib.load('knnmodel.joblib')

st.title('Predictor finds whether a given data of virus is H or HN')

#Now we implement the piece of code to give the values of feature

aa_length = st.text_input('Input AA length',700)
pi = st.text_input('value of pi',-0.5)
mol_wt = st.text_input('Value of mol weight',500)
hydropathy = st.text_input('Hydropathy value',-0.5)
helix = st.text_input('Input helix percentage',100)
loop = st.text_input('Inpu',100)
strand  = st.text_input('Input AA length',100)

E = st.text_input('Amino acid E count',40)
T = st.text_input('Amino acid T count',40)
Q = st.text_input('Amino acid Q count',40)
G = st.text_input('Amino acid G count',100)

columns = ['AA LENGTH', 'Pi ', 'Mol.Wt(KD)', 'Hydropathy', 'Helix (%)', 'Loop ','Strand ', 'E(%)', 'T', 'Q', 'G']

"""
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image 

uploadFile = st.file_uploader(label="virus.jpeg", type=['jpg', 'png'])

if uploadFile is not None:
    # Perform your Manupilations (In my Case applying Filters)
    img = load_image(uploadFile)
    st.image(img)
    st.write("Image Uploaded Successfully")
else:
    st.write("Make sure you image is in JPG/PNG Format.")

"""

def predict():
    row = np.array([aa_length,pi,mol_wt,hydropathy,helix,loop,strand,E,T,Q,G])
    X = pd.DataFrame([row], columns = columns)
    prediction = model.predict(X)

    if prediction[0] == 'YES':
        st.success('this virus is using H as a receptor')

    else:
        st.success('this virus is using HN as a receptor')

trigger = st.button('Predict', on_click=predict)

#prediction_1 = model.predict(X)


#row = np.array([aa_length,pi,mol_wt,hydropathy,helix,loop,strand,E,T,Q,G])
#XX = pd.DataFrame([row], columns = columns)

#print(XX)