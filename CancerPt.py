

import streamlit as st
import joblib
import pandas as pd
#from prediction import predict

st.write("# Breast Cancer Diagnosis")

col1, col2, col3 = st.columns(3)

# getting user input
radius_mean	= col1.number_input("Enter the radius_mean")
texture_mean	= col1.number_input("Enter the texture_mean")
perimeter_mean	= col1.number_input("Enter the perimeter_mean")
area_mean = col1.number_input("Enter the area_mean")	
smoothness_mean	= col1.number_input("Enter the smoothness_mean")
compactness_mean = col1.number_input("Enter compactness_mean")
concavity_mean = col1.number_input("Enter the concavity_mean") 
concave_points_mean	= col1.number_input("Enter the concave points_mean")
symmetry_mean	= col1.number_input("Enter the symmetry_mean")
fractal_dimension_mean = col1.number_input("Enter the fractal_dimension_mean")
radius_se = col2.number_input("Enter the radius_se")
texture_se = col2.number_input("Enter the texture_se")
perimeter_se = col2.number_input("Enter the perimeter_se")
area_se = col2.number_input("Enter the area_se")
smoothness_se = col2.number_input("Enter the smoothness_se")
compactness_se = col2.number_input("Enter the compactness_se")
concavity_se = col2.number_input("Enter the concavity_se")
concave_points_se = col2.number_input("Enter the concave points_se")
symmetry_se = col2.number_input("Enter the symmetry_se")
fractal_dimension_se = col2.number_input("Enter the fractal_dimension_se")
radius_worst = col3.number_input("Enter the radius_worst")
texture_worst = col3.number_input("Enter the texture_worst")
perimeter_worst = col3.number_input("Enter the perimeter_worst")
area_worst = col3.number_input("Enter the area_worst")
smoothness_worst = col3.number_input("Enter the smoothness_worst")
compactness_worst = col3.number_input("Enter the compactness_worst")
concavity_worst = col3.number_input("Enter the concavity_worst")
concave_points_worst = col3.number_input("Enter the concave points_worst")
symmetry_worst = col3.number_input("Enter the symmetry_worst")
fractal_dimension_worst = col3.number_input("Enter the fractal_dimension_worst")


df_pred = pd.DataFrame([[radius_mean, texture_mean, perimeter_mean,
       area_mean, smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]],

columns= ['radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave_points_mean', 'symmetry_mean', 'fractal_dimension_mean',
       'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se',
       'fractal_dimension_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave_points_worst',
       'symmetry_worst', 'fractal_dimension_worst'])

if st.button('Predict'):
    if sum(df_pred.iloc[0])==0:
            st.write('<p class="big-font">Please, fill the above form with your test results.</p>',unsafe_allow_html=True)
  
    else:    
      xg_boost = joblib.load('breastCancer_xgb_model.pkl')
      prediction = xg_boost.predict(df_pred)

      if(prediction[0]==0):
            st.write('<p class="big-font">The cancer is Benign.</p>',unsafe_allow_html=True)

      else:
            st.write('<p class="big-font">The cancer is Malignant.</p>',unsafe_allow_html=True)        
