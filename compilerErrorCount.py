import pandas as pd

# Load the dataset (change the file path accordingly)
main_table = pd.read_csv("MainTable.csv")

# Filter the MainTable for rows with compiler errors (assuming 'Compile.Result' indicates error state)
compiler_errors = main_table[main_table['Compile.Result'] == 'Error']

# Second interpretation: Total number of compiler errors per problem
total_errors_per_problem = compiler_errors.groupby('ProblemID').size()

# Find the problem with the most compiler errors (maximum total errors)
problem_with_most_errors = total_errors_per_problem.idxmax()
max_errors = total_errors_per_problem.max()

# First interpretation: Average number of compiler errors per problem
# We calculate the average by dividing the total number of errors by the number of unique students per problem
errors_per_problem = compiler_errors.groupby('ProblemID').size()
students_per_problem = main_table.groupby('ProblemID')['SubjectID'].nunique()
average_errors_per_problem = errors_per_problem / students_per_problem

# Find the problem with the highest average compiler errors
problem_with_highest_avg_errors = average_errors_per_problem.idxmax()
max_avg_errors = average_errors_per_problem.max()

# Print the results clearly
print("\nSecond Interpretation (Total Errors):")
print(f"Problem with the most compiler errors: ProblemID {problem_with_most_errors}")
print(f"Total number of compiler errors: {max_errors}")

print("\nFirst Interpretation (Average Errors):")
print(f"Problem with the highest average compiler errors: ProblemID {problem_with_highest_avg_errors}")
print(f"Average number of compiler errors: {max_avg_errors:.2f}")
