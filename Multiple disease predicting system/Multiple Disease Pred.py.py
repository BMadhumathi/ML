# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:40:56 2023

@author: bmadh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('C:/Users/bmadh/OneDrive/Desktop/Multiple disease predicting system/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/bmadh/OneDrive/Desktop/Multiple disease predicting system/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/bmadh/OneDrive/Desktop/Multiple disease predicting system/saved models/parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
