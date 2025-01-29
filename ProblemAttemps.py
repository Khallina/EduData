import pandas as pd

# Load the datasets
early_data = pd.read_csv("early.csv")
late_data = pd.read_csv("late.csv")

# Combine the datasets
data = pd.concat([early_data, late_data])

# Calculate the number of unique students per ProblemID
student_counts = data.groupby('ProblemID')['SubjectID'].nunique()

# Calculate the total attempts per ProblemID
total_attempts = data.groupby('ProblemID')['Attempts'].sum()

# Calculate the average attempts per student for each ProblemID
average_attempts_per_student = total_attempts / student_counts

# Find the ProblemID with the highest average attempts per student
max_attempts_problem = average_attempts_per_student.idxmax()
max_attempts_value = average_attempts_per_student.max()

print(f"ProblemID with the highest average attempts per student: {max_attempts_problem}")
print(f"Highest average attempts per student: {max_attempts_value}")
