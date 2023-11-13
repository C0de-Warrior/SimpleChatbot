from flask import Flask, render_template, request
import pickle
import importlib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load the vectorizer and classifier
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('classifier.pkl', 'rb') as file:
    classifier = pickle.load(file)


# Function to determine the intent and execute the corresponding action
def process_user_input(user_input, intent):
    module = importlib.import_module(intent)
    response = getattr(module, f"handle_{intent}")(user_input)
    return response


def get_intent(user_input):
    # Vectorize the user input
    user_input_vectorized = vectorizer.transform([user_input])

    # Predict the intent
    intent = classifier.predict(user_input_vectorized)[0]

    return intent


@app.route('/')
def home():
    return render_template("index.html")


chat_history = []  # Initialize an empty list to store the chat history


@app.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    userText = request.args.get('msg')
    intent = get_intent(userText)  # Determine the intent of the user's input
    response = process_user_input(userText, intent)  # Pass intent to process_user_input
    return response





if __name__ == '__main__':
    app.run()
