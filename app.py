from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load the vectorizer and classifier
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)

# Function to determine the intent and execute the corresponding action
def process_user_input(user_input):
    # Vectorize the user input
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the intent
    intent = classifier.predict(user_input_vectorized)[0]

    # Import the corresponding Python file for the intent
    module = __import__(intent)

    # Call the function for the intent and pass the user input
    response = getattr(module, f'handle_{intent}')(user_input)
    return response


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = process_user_input(userText)
    # Wrap the response in a <p> tag
    response_html = f'<p>{response}</p>'
    # Return the response to display on the website
    return response_html


if __name__ == '__main__':
    app.run()