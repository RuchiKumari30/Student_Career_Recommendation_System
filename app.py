import streamlit as st
import pickle
import numpy as np

# Load the trained model and label encoders
model = pickle.load(open("career_model.pkl", "rb"))
le_degree = pickle.load(open("le_degree.pkl", "rb"))
le_major = pickle.load(open("le_major.pkl", "rb"))
le_career = pickle.load(open("le_career.pkl", "rb"))

# App Title
st.title("Student Career Recommendation System")
st.markdown("Get personalized career suggestions based on your academic background.")

# Input Fields
degree = st.selectbox("Select Your Degree", le_degree.classes_)
major = st.selectbox("Select Your Major Field", le_major.classes_)
result = st.slider("Enter Your Academic Result (%)", 0.0, 100.0, 70.0)

# Recommend Button
if st.button("Recommend Career"):
    # Encode inputs
    encoded_degree = le_degree.transform([degree])[0]
    encoded_major = le_major.transform([major])[0]

    # Create input array
    input_data = np.array([[encoded_degree, encoded_major, result]])

    # Predict career
    predicted_encoded_career = model.predict(input_data)[0]

    # Decode to get career label
    recommended_career = le_career.inverse_transform([predicted_encoded_career])[0]

    # Output
    st.success(f" Recommended Career Path: **{recommended_career}**")
