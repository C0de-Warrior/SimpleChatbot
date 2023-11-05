import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
def search_lecturers_by_name(query):
    query_vector = name_vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, name_vectors).flatten()
    top_indices = similarity_scores.argsort()[::-1]  # Sort in descending order

    results = data.iloc[top_indices]
    exact_match = results[results['Lecturer Name'].str.lower() == query.lower()]

    if not exact_match.empty:
        # If an exact match is found, return the result
        return exact_match[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)
    elif not results.empty:
        # If no exact match is found but there are matching results, return those results with similarity score >= 0.8
        high_similarity = results[similarity_scores >= 0.8]
        if not high_similarity.empty:
            return high_similarity[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)

    return "No exact match found. Here are the closest matches:\n" + results[['Lecturer Name', 'Contact no', 'Email', 'Status', 'Department', 'Role']].to_string(index=False)


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


# Function to determine the intent and execute the corresponding action
def handle_lecturers(action_input):
    action_input = input(
        "Please enter a number that represents your required action:\n1. Lecturer Search\n2. Department Search\n3. "
        "H.O.D List\n")

    if action_input == '1':
        lecturer_name = input("Enter the name of the lecturer: ")
        search_result = search_lecturers_by_name(lecturer_name)
        print(search_result)
    elif action_input == '2':
        department_name = input("Enter the name of the department: ")
        search_result = search_lecturers_by_department(department_name)
        print(search_result)
    elif action_input == '3':
        search_result = search_lecturers_by_role('Head of Department')
        print(search_result)
    else:
        print('Invalid Input')


