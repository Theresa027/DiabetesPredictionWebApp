import pickle
import sklearn
import numpy as np
import streamlit as st
#to display images
from PIL import Image



#loading the saved model
loaded_model = pickle.load(open(r'C:\Users\HP\Desktop\GOMYCODE\trained_model.sav', 'rb'))


#creating a function for prediction

def diabetes_prediction(input_data):

    #changing the input_data_to_numpy_array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return "The person is not diabetic"
    else:
        return "The person is diabetic"

def main():
    # display image
    img = Image.open(r"C:\Users\HP\PycharmProjects\WhatsApp Image 2024-03-17 at 15.39.23_22265810.jpg")
    new_image = img.resize((700, 200))
    st.image(new_image)
    # let's display
    # st.image(img, width=700)

    # giving a title
    st.title('Diabetes Prediction Web App')

    # getting the input data from the user


    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetespedigreeFunction = st.text_input('Diabetes pedigree Function value')
    Age = st.text_input('Age of the person')


    # code for prediction
    diagnosis = ''

    # creating a button for prediction

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetespedigreeFunction, Age])


        st.success(diagnosis)


if __name__ == '__main__':
    main()
