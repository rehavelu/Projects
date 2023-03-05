# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:13:12 2023

@author: V SASI REHA
"""
import numpy as np
import pickle

load_model=pickle.load(open('C:/Users/V SASI REHA/Downloads/Medical Insurance Cost Prediction-Streamlit/medical_insurance_cost_predictor.sav','rb'))
input_data = (19,0,27.9,0,1,3)
input_data_array = np.asarray(input_data)

#reshaping the data so that it works for only one instance at a time
input_data_reshaped = input_data_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
print('Predicted Medical Insurance Cost : ',str(prediction))
