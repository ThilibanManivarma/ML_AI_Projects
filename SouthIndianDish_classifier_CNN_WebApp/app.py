import streamlit as st
from keras.models import load_model
from PIL import Image
from newutil import classify

#Set title 
st.title('Sakarapongal - Vadakari classifier')

#Set header 
st.header('Please upload an image of either Sakarapongal or Vadakari')

#Upload file
file = st.file_uploader("",type=['jpeg','jpg','png'])

#Load classifier 
model = load_model('my_model.hdf5')

#load class names 
#with open('labels.txt', 'r') as f:
#    class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
#    f.close()

#print(class_names)



#display image 

if file is not None:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True) #To display an image

    #classify image
    #class_name, conf_score = classify(image, model, class_names)
    class_name_x = classify(image, model)

    #write classification

    st.write("## {}".format(class_name_x))
    #st.write("### score: {}".format(conf_score))



