import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intent data from intent.json file
with open('intent.json', 'r') as file:
    data = json.load(file)

# Extract training examples and labels from intent data
X_train = []
y_train = []
for intent in data:
    for example in data[intent]:
        X_train.append(example)
        y_train.append(intent)

# Create a CountVectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train a logistic regression classifier
classifier = LogisticRegression()
classifier.fit(X_train_vectorized, y_train)

# Save the vectorizer and classifier to disk
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

with open('classifier.pkl', 'wb') as file:
    pickle.dump(classifier, file)


# Function to determine the intent and execute the corresponding action
def process_user_input(user_input):
    # Load the saved vectorizer and classifier
    with open('vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)

    with open('classifier.pkl', 'rb') as file:
        classifier = pickle.load(file)

    # Vectorize the user input
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the intent
    intent = classifier.predict(user_input_vectorized)[0]

    # Import the corresponding Python file for the intent
    module = __import__(intent)

    # Call the function for the intent and pass the user input
    getattr(module, f'handle_{intent}')(user_input)


# Example usage
while True:
    user_input = input("Enter your message (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    process_user_input(user_input)
