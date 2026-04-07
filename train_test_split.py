from sklearn.model_selection import train_test_split

# Assuming X (features) and y (target) are already defined from the preprocessing step
# X = features_dataframe
# y = target_series

# Perform the Train-Test Split
# test_size=0.2 means 20% of the data will be used for testing, and 80% for training
# random_state=42 ensures that the split is reproducible (you get the same split every time)
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=42
)

# Verify the split sizes
print(f"Total samples: {len(X)}")
print(f"Training samples: {len(X_train)} (80%)")
print(f"Testing samples: {len(X_test)} (20%)")

# Now X_train and y_train are used to 'teach' the model
# X_test and y_test are used to 'evaluate' how well it learned
