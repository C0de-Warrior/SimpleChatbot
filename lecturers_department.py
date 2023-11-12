import re

import pandas as pd
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the data from the CSV file
data = pd.read_csv('Teachers.csv')

# Extract the teacher names and departments
teacher_names = data['Lecturer Name'].tolist()
departments = data['Department'].tolist()

# Create a TF-IDF vectorizer for names
name_vectorizer = TfidfVectorizer()
name_vectors = name_vectorizer.fit_transform(teacher_names)

# Create a TF-IDF vectorizer for departments
department_vectorizer = TfidfVectorizer()
department_vectors = department_vectorizer.fit_transform(departments)


# Define a function to search for lecturers by name
def extract_department_from_input(user_input):
    # Use regular expression to extract the department from the user input
    pattern1 = r"I am searching for the contact details of .*? lecturers in the (\w+) department"
    pattern2 = r"I want to search for the lecturers contact details in the (\w+) department"
    match1 = re.search(pattern1, user_input)
    match2 = re.search(pattern2, user_input)

    if match1:
        department = match1.group(1).lower()  # Extracted department in lowercase
        return department
    elif match2:
        department = match2.group(1).lower()  # Extracted department in lowercase
        return department

    return "Please provide the department you are searching for in one of the following formats:\n" \
           "- I am searching for the contact details of Africa University lecturers in the [Department] department\n" \
           "- I want to search for the lecturers contact details in the [Department] department"


def handle_lecturers_department(query):
    department = extract_department_from_input(query)

    if department:
        close_matches = []

        for index, row in data.iterrows():
            row_department = str(row['department'])
            if pd.notnull(row_department):
                similarity = fuzz.token_set_ratio(department, row_department)
                if similarity >= 85:
                    close_matches.append(row)

        if close_matches:
            response = "Lecturers in the Specified Department: <br><br>"
            for match in close_matches:
                response += f"Title: {match['title']}<br>"
                response += f"Name: {match['name']}<br>"
                response += f"Contact: {match['contact']}<br>"
                response += f"Email: {match['email']}<br>"
                response += f"Status: {match['status']}<br>"
                response += f"Department: {match['department']}<br>"
                response += f"Role: {match['role']}<br>"
                return response
            else:
                return "No lecturers found in the given department."


# Define a function to search for lecturers by role
def search_lecturers_by_role(query):
    matching_indices = data[data['Role'] != 'lecturer'].index
    results = data.iloc[matching_indices]

    if not results.empty:
        return results[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)

    return "No teachers found in the given role."

# Function to determine the intent and executethe corresponding action.
