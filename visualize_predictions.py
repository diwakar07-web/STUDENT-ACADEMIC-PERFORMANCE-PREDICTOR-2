import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_predictions_vs_actual(model, X_test, y_test):
    """
    Generates predictions and plots them against actual values.
    """
    # 1. Generate predictions for the test set
    y_pred = model.predict(X_test)

    # 2. Set up the plot aesthetics
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 8))

    # 3. Create the scatter plot
    # alpha=0.6 helps visualize density where points overlap
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, color='royalblue', edgecolor='w', s=80)

    # 4. Draw the ideal diagonal reference line (Perfect Prediction Line)
    # This line represents where Predicted == Actual
    max_val = max(max(y_test), max(y_pred))
    min_val = min(min(y_test), min(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], color='crimson', lw=2, linestyle='--', label='Perfect Prediction (y=x)')

    # 5. Labeling and Title
    plt.title('Predicted vs. Actual Student Scores', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Actual Final Exam Score', fontsize=12)
    plt.ylabel('Predicted Final Exam Score', fontsize=12)
    plt.legend(loc='upper left')
    
    # Add grid for better readability
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

    return y_pred

# Example usage:
# y_pred = plot_predictions_vs_actual(random_forest_model, X_test, y_test)
