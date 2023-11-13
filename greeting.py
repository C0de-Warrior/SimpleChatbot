import random


def handle_greeting(user_input):
    # List of possible greetings
    greetings = ["Hello!", "Hi!", "Hey there!", "Greetings!"]

    # Randomly choose a greeting
    random_greeting = random.choice(greetings)

    # Return the chosen greeting
    return random_greeting + (" I am the Acacia chat-bot. How can I assist you today? I can help you with information "
                              "about Africa University, from the programs offered at the university to the various "
                              "sports and clubs you can join.")
