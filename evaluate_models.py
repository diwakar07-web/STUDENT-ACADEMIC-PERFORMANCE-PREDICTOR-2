import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_models(models, X_test, y_test):
    """
    Evaluates a dictionary of models and returns a comparison table.
    """
    results = []
    
    for name, model in models.items():
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        results.append({
            'Model': name,
            'MAE': round(mae, 4),
            'MSE': round(mse, 4),
            'RMSE': round(rmse, 4),
            'R2 Score': round(r2, 4)
        })
    
    # Create comparison table
    comparison_df = pd.DataFrame(results)
    return comparison_df

# Assuming models are already trained and stored in a dictionary
# models = {
#     'Linear Regression': linear_reg_model,
#     'Decision Tree': decision_tree_model,
#     'Random Forest': random_forest_model
# }

# comparison_table = evaluate_models(models, X_test, y_test)
# print(comparison_table)
