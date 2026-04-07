import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_student_data(file_path):
    # 1. Load the dataset using pandas
    print("--- Loading Dataset ---")
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {file_path}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please ensure the dataset exists.")
        return

    # 2. Display basic dataset info and summary
    print("\n--- Dataset Info ---")
    print(df.info())
    
    print("\n--- Statistical Summary ---")
    print(df.describe())

    # 3. Check and handle missing values
    print("\n--- Checking for Missing Values ---")
    missing_values = df.isnull().sum()
    print(missing_values[missing_values > 0] if missing_values.any() else "No missing values found.")
    
    # If missing values were found, we would handle them here (e.g., df.fillna(df.mean()))
    if missing_values.any():
        print("Handling missing values by filling with column mean...")
        df = df.fillna(df.mean())

    # 4. Encode categorical features
    # In our dataset:
    # 'extracurricular_participation' is already 0/1 (binary)
    # 'parents_education_level' is 1, 2, 3 (ordinal)
    # If we had string categories, we would use pd.get_dummies() or LabelEncoder
    print("\n--- Encoding Categorical Features ---")
    # Example for nominal categorical data (if any existed):
    # df = pd.get_dummies(df, columns=['some_category_column'], drop_first=True)
    print("Categorical features are already in numeric format (0/1 or ordinal).")

    # 5. Separate features (X) and target variable (y)
    print("\n--- Separating Features and Target ---")
    target_column = 'final_exam_score'
    
    if target_column not in df.columns:
        print(f"Error: Target column '{target_column}' not found in dataset.")
        return

    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")

    # 6. Normalize/Standardize numerical features
    # Standardization (Mean=0, Std=1) is generally preferred for regression models like Linear Regression or SVM
    print("\n--- Standardizing Features ---")
    scaler = StandardScaler()
    
    # We fit the scaler only on the features
    X_scaled = scaler.fit_transform(X)
    
    # Convert back to DataFrame for readability (optional)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    
    print("Standardization complete.")
    print("\nFirst 5 rows of standardized features:")
    print(X_scaled_df.head())

    # 7. Split into Training and Testing sets (Bonus step for ML readiness)
    print("\n--- Splitting into Train and Test sets ---")
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}")

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Path to the dataset generated in the previous step
    dataset_path = 'public/student_performance.csv'
    preprocess_student_data(dataset_path)
