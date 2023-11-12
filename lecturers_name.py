import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

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
def extract_name_from_input(user_input):
    # Use regular expression to extract the name from the user input
    pattern1 = r"I am searching for the contact details of (.*?) lecturer"
    pattern2 = r"I want to search for a lecturers contact (.*?)"
    match1 = re.search(pattern1, user_input)
    match2 = re.search(pattern2, user_input)

    if match1:
        name = match1.group(1).lower()  # Extracted name in lowercase
        return name
    elif match2:
        name = match2.group(1).lower()  # Extracted name in lowercase
        return name

    # Handle cases where only the first name or last name is provided
    names = user_input.split(" ")[-2:]  # Extract last two words (first name, last name)
    if len(names) == 2:
        name = " ".join(names).lower()# Extracted name in lowercase
        print(name)
        return name

    return "Please provide the name of the lecturer you are searching for in one of the following formats:\n" \
           "- I am searching for the contact details of [Lecturer Name] lecturer\n" \
           "- I want to search for a lecturer's contact [Lecturer Name]"


def handle_lecturers_name(query):
    name = extract_name_from_input(query)  # Call the extract_name_from_input function
    print(name)
    if isinstance(name, str):
        return name  # Return error message if name extraction failed

    query_vector = name_vectorizer.transform([name])
    similarity_scores = cosine_similarity(query_vector, name_vectors).flatten()
    top_indices = similarity_scores.argsort()[::-1]  # Sort in descending order

    results = data.iloc[top_indices]
    exact_match = results[results['Lecturer Name'].str.lower() == name.lower()]

    if not exact_match.empty:
        # If an exact match is found, return the result
        return exact_match[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(
            index=False)
    elif not results.empty:
        # If no exact match is found but there are matching results, return those results with similarity score >= 0.8
        high_similarity = results[similarity_scores >= 0.8]
        if not high_similarity.empty:
            return high_similarity[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(
                index=False)

    return "No exact match found. Here are the closest matches:\n" + results[
        ['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)


# Define a function to search for lecturers by department
def search_lecturers_by_department(query):
    query_vector = department_vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, department_vectors).flatten()
    matching_indices = [index for index, score in enumerate(similarity_scores) if score >= 0.8]
    results = data.iloc[matching_indices]

    if not results.empty:
        return results[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)

    return "No lecturers found in the given department."


# Define a function to search for lecturers by role
def search_lecturers_by_role(query):
    matching_indices = data[data['Role'] != 'lecturer'].index
    results = data.iloc[matching_indices]

    if not results.empty:
        return results[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)

    return "No teachers found in the given role."

# Function to determine the intent and executethe corresponding action.