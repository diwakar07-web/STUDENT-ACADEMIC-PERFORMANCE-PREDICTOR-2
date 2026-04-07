import joblib
import numpy as np

# 1. Save the trained model
# We use joblib as it is more efficient than pickle for models with large numpy arrays (like Random Forest)
model_filename = 'student_performance_model.pkl'
joblib.dump(best_model, model_filename)
print(f"Model saved successfully as {model_filename}")

# 2. Load the saved model back into Python
# This allows us to use the model in a different script or after restarting the environment
loaded_model = joblib.load(model_filename)
print("Model loaded successfully.")

# 3. Demonstrate prediction on new, unseen data
# Data format: [previous_marks, attendance, study_hours, assignment, internal, extra, internet, parents_edu, income]
# Example: A student with 85 marks, 90% attendance, 8 hours study, 88 assignment, 45 internal, 1 extra, 2h internet, level 3 edu, 8000 income
new_student_data = np.array([[85.0, 90.0, 8.0, 88.0, 45.0, 1, 2.0, 3, 8000.0]])

# Note: If the model was trained on scaled data, the new data must be scaled using the SAME scaler
# Assuming 'scaler' was the StandardScaler used during preprocessing:
# new_student_scaled = scaler.transform(new_student_data)
# prediction = loaded_model.predict(new_student_scaled)

# For this demonstration, we assume the model handles the input directly or scaling is handled
prediction = loaded_model.predict(new_student_data)

print(f"\nPredicted Final Exam Score for the new student: {prediction[0]:.2f}")
