import numpy as np
import joblib
import streamlit as st
import joblib
import pandas as pd


# Load your encoder and model
loaded_model = joblib.load('C:/salman/ML/Heart Disease Prediction/model.joblb')

# Creating a function for prediction
def heart_disease_prediction(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The person is not likely to have heart disease'
    else:
        return 'The person is likely to have heart disease'

def main():
    # Giving a title
    st.title('Heart Disease Prediction Web App')

    # Getting the input data from the user
    age = st.text_input('Age')
    sex = st.selectbox('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
    trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    chol = st.text_input('Serum Cholesterol (mg/dl)')
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.text_input('Maximum Heart Rate Achieved')
    exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.text_input('ST Depression Induced by Exercise Relative to Rest')
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (0-3)')
    thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

    # Code for prediction
    diagnosis = ''

    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        input_params = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        input_params=pd.DataFrame(input_params,columns=(['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']))
        input_params.replace({'sex': {'Male':1, 'Female':0}}, inplace=True)
        input_params.replace({'fbs': {'Yes':1, 'No':0}}, inplace=True)
        input_params.replace({'exang': {'Yes':1, 'No':0}}, inplace=True)

        diagnosis = heart_disease_prediction(input_params)

    st.success(diagnosis)

if __name__ == '__main__':
    main()
