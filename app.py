import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Load the saved model
@st.cache_resource
def load_model():
    return joblib.load('student_performance_model.pkl')

model = load_model()

# 2. App Title and Description
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")
st.title("🎓 Student Academic Performance Predictor")
st.markdown("""
This app uses a Machine Learning model to predict a student's final exam score based on their behavioral, academic, and socio-economic factors.
""")

# 3. Sidebar for Input Features
st.sidebar.header("Input Student Details")

def user_input_features():
    # Academic Factors
    st.sidebar.subheader("Academic Factors")
    previous_marks = st.sidebar.slider("Previous Marks (0-100)", 0.0, 100.0, 75.0)
    attendance_percentage = st.sidebar.slider("Attendance %", 50.0, 100.0, 85.0)
    internal_marks = st.sidebar.slider("Internal Marks (0-50)", 0.0, 50.0, 35.0)
    assignment_score = st.sidebar.slider("Assignment Score (0-100)", 0.0, 100.0, 80.0)
    
    # Behavioral Factors
    st.sidebar.subheader("Behavioral Factors")
    study_hours_per_day = st.sidebar.number_input("Study Hours per Day", 0.0, 12.0, 5.0)
    internet_usage_hours = st.sidebar.number_input("Internet Usage Hours", 0.0, 10.0, 3.0)
    extracurricular_participation = st.sidebar.selectbox("Extracurricular Participation", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    
    # Socio-Economic Factors
    st.sidebar.subheader("Socio-Economic Factors")
    parents_education_level = st.sidebar.selectbox("Parents Education Level", options=[1, 2, 3], format_func=lambda x: ["Low", "Medium", "High"][x-1])
    family_income = st.sidebar.number_input("Monthly Family Income", min_value=0.0, value=5000.0)

    # Create a dictionary for the features
    data = {
        'previous_marks': previous_marks,
        'attendance_percentage': attendance_percentage,
        'study_hours_per_day': study_hours_per_day,
        'assignment_score': assignment_score,
        'internal_marks': internal_marks,
        'extracurricular_participation': extracurricular_participation,
        'internet_usage_hours': internet_usage_hours,
        'parents_education_level': parents_education_level,
        'family_income': family_income
    }
    
    # Convert to DataFrame
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# 4. Main Page Display
st.subheader("Student Profile Summary")
st.write(input_df)

# 5. Prediction Logic
if st.button("Predict Final Exam Score"):
    try:
        # Perform prediction
        prediction = model.predict(input_df)
        
        # Display results
        st.success(f"### Predicted Final Exam Score: {prediction[0]:.2f} / 100")
        
        # Visual feedback
        st.progress(min(100, int(prediction[0])))
        
        # Additional Context
        if prediction[0] >= 75:
            st.balloons()
            st.info("Performance Outlook: Excellent! The student is on track for a high grade.")
        elif prediction[0] >= 50:
            st.warning("Performance Outlook: Average. There is room for improvement in study habits.")
        else:
            st.error("Performance Outlook: At Risk. Immediate intervention recommended.")
            
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.info("Ensure the model file 'student_performance_model.pkl' is present and matches the input features.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit • Machine Learning Regression Project")
