import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('public/student_performance.csv')

# Set aesthetic style for plots
sns.set_theme(style="whitegrid", palette="muted")

# 1. Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Student Performance Features', fontsize=16)
plt.show()

# Insight: Identify which features have the strongest positive or negative correlation with 'final_exam_score'.

# 2. Distribution of Key Numerical Features
features_to_plot = ['study_hours_per_day', 'attendance_percentage', 'final_exam_score']
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, feature in enumerate(features_to_plot):
    sns.histplot(df[feature], kde=True, ax=axes[i], color='teal')
    axes[i].set_title(f'Distribution of {feature.replace("_", " ").title()}')

plt.tight_layout()
plt.show()

# Insight: Check for normality, skewness, and potential outliers in the target and primary predictors.

# 3. Relationship Plots (Target vs. Predictors)
# We select the most meaningful features based on expected correlation
top_features = ['study_hours_per_day', 'previous_marks', 'internal_marks']

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

for i, feature in enumerate(top_features):
    sns.regplot(x=feature, y='final_exam_score', data=df, ax=axes[i], 
                scatter_kws={'alpha':0.5, 'color':'royalblue'}, line_kws={'color':'crimson'})
    axes[i].set_title(f'{feature.replace("_", " ").title()} vs Final Exam Score')

plt.tight_layout()
plt.show()

# Insight: Visualize the linearity of relationships and the spread of data points around the regression line.

# 4. Categorical Impact: Parents Education Level vs Final Score
plt.figure(figsize=(10, 6))
sns.boxplot(x='parents_education_level', y='final_exam_score', data=df, palette='Set2')
plt.title('Impact of Parents Education Level on Final Exam Score', fontsize=14)
plt.xlabel('Education Level (1=Low, 2=Medium, 3=High)')
plt.ylabel('Final Exam Score')
plt.show()

# Insight: Determine if there is a significant variance in scores across different education levels.
