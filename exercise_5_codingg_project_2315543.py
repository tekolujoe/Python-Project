# -*- coding: utf-8 -*-
"""Exercise_5_Codingg_project_2315543.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B-umk8mU5bdIcoKTO2HSj-DKZMFY7dHm
"""

import numpy as np
import pandas as pd

# Define the named data type
std_dtype = np.dtype([('Reg_no', 'int'), ('Mark_exam', 'float'), ('Mark_coursework', 'float'), ('Overall_mark', 'float'), ('Std_grade', 'U20')])

# Prompt the user for the specified input file name
specified_file_name = input("Enter the name of the input file: ")

# Read the data from the specified input file using Pandas
stud_data = pd.read_csv(specified_file_name , sep=' ', header=None, skiprows=1,
                   names=['Reg_no', 'Mark_exam', 'Mark_coursework'])

# From the input file name, extract information from the first lin
num_students, coursework_weighting = map(int, stud_data.iloc[0, :2])

# Calculate student's overall marks then round to two decimal places
stud_data['Overall_mark'] = np.round(stud_data['Mark_exam'] * (1 - coursework_weighting / 100) +
                               stud_data['Mark_coursework'] * (coursework_weighting / 100), 2)

# Based on overall marks of the students, define a function to calculate Std_grade
def calculate_grade(row):
    if any(mark < 30 for mark in [row['Mark_exam'], row['Mark_coursework']]):
        return "Fail"
    elif row['Overall_mark'] >= 70:
        return "First Class"
    elif 50 <= row['Overall_mark'] < 70:
        return "Second Class"
    elif 40 <= row['Overall_mark'] < 50:
        return "Third Class"
    else:
        return "Fail"

# Apply the calculate_grade function to create a new 'Std_grade' column
stud_data['Std_grade'] = stud_data.apply(calculate_grade, axis=1)

# Sort the DataFrame by overall mark
sorted_stud_data = stud_data.sort_values(by='Overall_mark', ascending=False)

# Output sorted_stud_data to a file
output_file_name = specified_file_name.replace(".txt", "_std_data_output.txt")
sorted_stud_data.to_csv(output_file_name, sep='\t', index=False)

# Display the number of students in each grade category
std_grade_counts = sorted_stud_data['Std_grade'].value_counts()
print("Number of students with first-class marks:", std_grade_counts.get("First Class", 0))
print("Number of students with second-class marks:", std_grade_counts.get("Second Class", 0))
print("Number of students with third-class marks:", std_grade_counts.get("Third Class", 0))
print("Number of students who have failed:", std_grade_counts.get("Fail", 0))

# Display the registration numbers of the students who have failed
failed_students = sorted_stud_data[sorted_stud_data['Std_grade'] == 'Fail']
print("Registration numbers of students who have failed:")
print(failed_students['Reg_no'].tolist())