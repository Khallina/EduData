import pandas as pd
#CSV files not uploaded for dataset confidentiality, upload the files with these names to run
# Load the dataset (change the file path accordingly)
main_table = pd.read_csv("MainTable.csv")
subjects_table = pd.read_csv("Subject.csv")

# Count unique students
unique_students_main = main_table['SubjectID'].nunique()
unique_students_subjects = subjects_table['SubjectID'].nunique()

print(f"Unique students in MainTable: {unique_students_main}")
print(f"Unique students in Subjects Table: {unique_students_subjects}")

