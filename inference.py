import joblib
import pandas as pd

def predict_student_score():
    # 1. Load the saved model
    model_path = 'student_performance_model.pkl'
    try:
        model = joblib.load(model_path)
        print(f"Model '{model_path}' loaded successfully.")
    except FileNotFoundError:
        print(f"Error: {model_path} not found. Please ensure the model is saved in the correct directory.")
        return

    # 2. Define the input features in the exact order used during training
    # It's best to use a dictionary to ensure clarity and easy conversion to DataFrame
    new_student_data = {
        'previous_marks': 78.5,
        'attendance_percentage': 85.0,
        'study_hours_per_day': 6.5,
        'assignment_score': 82.0,
        'internal_marks': 42.0,
        'extracurricular_participation': 1,  # 1 for Yes, 0 for No
        'internet_usage_hours': 3.0,
        'parents_education_level': 2,        # 1=Low, 2=Medium, 3=High
        'family_income': 5500.0
    }

    # 3. Convert the input into a pandas DataFrame
    # Models trained with scikit-learn often expect a 2D array or DataFrame
    input_df = pd.DataFrame([new_student_data])

    # 4. Perform the prediction
    # Note: If the model was trained on standardized data, you would need to 
    # load the saved 'scaler.pkl' and apply scaler.transform(input_df) here.
    try:
        predicted_score = model.predict(input_df)
        
        # 5. Print the result clearly
        print("\n" + "="*30)
        print(" STUDENT PERFORMANCE PREDICTION ")
        print("="*30)
        for feature, value in new_student_data.items():
            print(f"{feature.replace('_', ' ').title()}: {value}")
        print("-" * 30)
        print(f"PREDICTED FINAL EXAM SCORE: {predicted_score[0]:.2f} / 100")
        print("="*30)
        
    except Exception as e:
        print(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    predict_student_score()
