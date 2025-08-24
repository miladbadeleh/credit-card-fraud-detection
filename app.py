import streamlit as st
import pickle
import numpy as np

# Load your trained best model (save it first using pickle/joblib)
# model = pickle.load(open('best_model_rf.pkl', 'rb'))

st.title('Credit Card Fraud Detection Prototype')
st.write("This is a simple demo of the ML model. Enter the transaction details.")

# Create input fields for key features (simplified for demo)
v1 = st.number_input('V1')
v2 = st.number_input('V2')
amount = st.number_input('Scaled Amount')

if st.button('Predict'):
    # Build a feature array from inputs
    input_data = np.array([[v1, v2, ..., amount]]) # You need to map all 30 features correctly
    prediction = model.predict(input_data)[0]
    prediction_proba = model.predict_proba(input_data)[0]

    if prediction == 1:
        st.error(f'Warning: Transaction predicted as FRAUDulent with {prediction_proba[1]:.2%} confidence.')
    else:
        st.success(f'Transaction predicted as LEGITIMATE with {prediction_proba[0]:.2%} confidence.')
