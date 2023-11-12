import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data from the CSV file
data = pd.read_csv('Teachers.csv')

# Extract the teacher names and departments
teacher_names = data['Lecturer Name'].tolist()
departments = data['Department'].tolist()


# Define a function to search for lecturers by role
def handle_lecturers_role(query):
    matching_indices = data[data['Role'] != 'lecturer'].index
    results = data.iloc[matching_indices]

    if not results.empty:
        response = "Lecturers in the Specified Role:<br><br>"
        for index, row in results.iterrows():
            response += f"Name: {row['Lecturer Name']}<br>"
            response += f"Contact: {row['Contact no']}<br>"
            response += f"Email: {row['Email']}<br>"
            response += f"Status: {row['Status']}<br>"
            response += f"Department: {row['Department']}<br>"
            response += f"Role: {row['Role']}<br><br>"
        return response

    return "No teachers found in the given role."
