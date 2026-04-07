import csv
import random
import math

def generate_dataset(num_rows=500):
    header = [
        "previous_marks", "attendance_percentage", "study_hours_per_day", 
        "assignment_score", "internal_marks", "extracurricular_participation", 
        "internet_usage_hours", "parents_education_level", "family_income", 
        "final_exam_score"
    ]
    
    data = []
    for i in range(num_rows):
        # Independent Variables
        prev_marks = round(random.uniform(40, 95) if random.random() > 0.05 else random.uniform(0, 100), 1)
        attendance = round(random.uniform(60, 100) if random.random() > 0.1 else random.uniform(50, 100), 1)
        study_hours = round(random.gauss(5, 2), 1)
        study_hours = max(0, min(12, study_hours))
        
        assign_score = round(random.uniform(50, 100) if random.random() > 0.05 else random.uniform(0, 100), 1)
        internal_marks = round(random.uniform(20, 50) if random.random() > 0.05 else random.uniform(0, 50), 1)
        
        extracurricular = 1 if random.random() > 0.6 else 0
        internet_hours = round(random.uniform(1, 8), 1)
        parents_edu = random.choice([1, 2, 3])
        
        # Family income: 1500 to 15000 range
        family_income = round(random.gauss(5000, 2000) + (parents_edu * 1000), 2)
        family_income = max(1000, family_income)

        # Target Variable Calculation (Realistic Correlation)
        # Base score
        score = 10 
        score += 0.25 * prev_marks
        score += 0.15 * attendance
        score += 2.5 * study_hours
        score += 0.1 * assign_score
        score += 0.6 * internal_marks
        score += 1.5 * extracurricular
        
        # Internet usage effect: slight positive for low, negative for high
        if internet_hours > 5:
            score -= 0.8 * (internet_hours - 5)
        else:
            score += 0.2 * internet_hours
            
        score += 2.0 * parents_edu
        score += 0.0002 * family_income
        
        # Add non-linearity
        score += 2 * math.sin(study_hours)
        
        # Add Noise
        noise = random.gauss(0, 4)
        score += noise
        
        # Outliers (5% chance)
        if random.random() < 0.05:
            if random.random() > 0.5:
                score += 20 # High outlier
            else:
                score -= 20 # Low outlier
        
        # Clipping
        final_score = round(max(0, min(100, score)), 1)
        
        data.append([
            prev_marks, attendance, study_hours, assign_score, internal_marks,
            extracurricular, internet_hours, parents_edu, family_income, final_score
        ])
        
    return header, data

header, data = generate_dataset(500)

with open('student_performance_dataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Dataset generated successfully.")
