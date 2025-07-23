import streamlit as st
import pickle
import numpy as np

with open('loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏦 Loan Approval Prediction")
st.subheader("Enter Applicant Details")
education_input = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed_input = st.selectbox("Self Employed", ["Yes", "No"])
no_of_dependents = st.number_input("No of Dependents", min_value=0, step=1)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0.0)
luxury_assets_value = st.number_input("Luxury Asset Value", min_value=0)
commercial_assets_value = st.number_input("Commercial Asset Value", min_value=0)
residential_assets_value = st.number_input("Residential Asset Value", min_value=0)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, step=1)
loan_term = st.number_input("Loan Term (months)", min_value=1)
loan_amount = st.number_input("Loan Amount", min_value=0.0)
income_annum = st.number_input("Annual Income", min_value=0.0)

# Convert inputs
education = 1 if education_input == "Graduate" else 0
self_employed = 1 if self_employed_input == "Yes" else 0

# Prediction
if st.button("Predict Loan Approval"):
    user_input = [[
        education,
        self_employed,
        no_of_dependents,
        bank_asset_value,
        luxury_assets_value,
        commercial_assets_value,
        residential_assets_value,
        cibil_score,
        loan_term,
        loan_amount,
        income_annum
    ]]

    prediction = model.predict(user_input)
    result = "✅ Loan Approved" if prediction[0] == "Approved" else "❌ Loan Rejected"
    st.success(f"Prediction: {result}")