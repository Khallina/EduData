import pandas as pd
#CSV files not uploaded for dataset confidentiality, upload the files with these names to run
# Load the datasets
early_data = pd.read_csv("early.csv")
late_data = pd.read_csv("late.csv")

# Combine early and late datasets
combined_data = pd.concat([early_data, late_data])

# Group by ProblemID and calculate the average number of attempts
average_attempts_per_problem = combined_data.groupby("ProblemID")["Attempts"].mean()

# Find the ProblemID with the highest average attempts
highest_avg_attempts = average_attempts_per_problem.idxmax()
highest_avg_attempts_value = average_attempts_per_problem.max()

# Display the result
print(f"Problem with the highest average attempts: {highest_avg_attempts}")
print(f"Average attempts for this problem: {highest_avg_attempts_value}")
