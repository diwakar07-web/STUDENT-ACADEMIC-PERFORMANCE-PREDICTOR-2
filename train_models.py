from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Assuming X_train, y_train are already defined and preprocessed
# X_train = training_features
# y_train = training_target

# 1. Linear Regression Model
# Best for capturing linear relationships between features and target
linear_reg_model = LinearRegression()
linear_reg_model.fit(X_train, y_train)
print("Linear Regression model trained successfully.")

# 2. Decision Tree Regressor Model
# Captures non-linear relationships and interactions between features
# random_state=42 ensures reproducibility of the tree structure
decision_tree_model = DecisionTreeRegressor(random_state=42)
decision_tree_model.fit(X_train, y_train)
print("Decision Tree Regressor model trained successfully.")

# 3. Random Forest Regressor Model
# An ensemble method that combines multiple decision trees for better accuracy and stability
# n_estimators=100 is a standard starting point for the number of trees
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest_model.fit(X_train, y_train)
print("Random Forest Regressor model trained successfully.")

# All models are now trained and stored in their respective variables
# Ready for evaluation in the next step
