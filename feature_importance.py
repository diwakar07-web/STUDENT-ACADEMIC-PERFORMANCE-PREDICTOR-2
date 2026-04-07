import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importance(model, feature_names, model_type='tree'):
    """
    Extracts and plots feature importance for a given model.
    """
    # 1. Extract Importance
    if model_type == 'tree':
        # For Random Forest or Decision Trees
        importances = model.feature_importances_
    else:
        # For Linear Regression (using absolute coefficients)
        importances = np.abs(model.coef_)

    # 2. Create a DataFrame for visualization
    feature_importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    })

    # 3. Sort features by importance (highest to lowest)
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    # 4. Plotting
    plt.figure(figsize=(12, 8))
    sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='viridis')
    
    plt.title('Feature Importance for Student Academic Performance Predictor', fontsize=16)
    plt.xlabel('Relative Importance Score', fontsize=12)
    plt.ylabel('Features', fontsize=12)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    return feature_importance_df

# Example usage with the best model (Random Forest)
# feature_names = X_train.columns
# plot_feature_importance(random_forest_model, feature_names, model_type='tree')
