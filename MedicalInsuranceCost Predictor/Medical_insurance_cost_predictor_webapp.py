# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:22:32 2023

@author: V SASI REHA
"""

import numpy as np
import pickle
import streamlit as st
load_model=pickle.load(open('medical_insurance_predictor.sav','rb'))


def insurance_prediction(input_data):
    
    input_data_array = np.asarray(input_data)

    #reshaping the data so that it works for only one instance at a time
    input_data_reshaped = input_data_array.reshape(1,-1)

    prediction = load_model.predict(input_data_reshaped)
    return'Predicted Medical Insurance Cost : ',str(prediction)
    
    
    
def main():
    #giving a title
    st.title('Medical Insurance Cost Prediction')
    
    #get the input data from user
   
    age=st.text_input('Age')
    sex=st.text_input('Gender:0-->Female 1-->Male')
    bmi=st.text_input('BMI value')
    children=st.text_input('Number of children')
    smoker=st.text_input('Smoker 0-->No 1-->Yes')
    region=st.text_input('Region')
    
    #code for prediction
    prediction=''
    
    #creating a button for prediction
    if st.button('Insurance Amount'):
        prediction=insurance_prediction([age,sex,bmi,children,smoker,region])
    st.success(prediction)
    
if __name__=='__main__':
    main()
    
        