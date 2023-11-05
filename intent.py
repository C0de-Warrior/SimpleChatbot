import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load intent data from intent.txt file
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