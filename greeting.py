import random


def handle_greeting(user_input):
    # List of possible greetings
    greetings = ["Hello!", "Hi!", "Hey there!", "Greetings!"]

    # Randomly choose a greeting
    random_greeting = random.choice(greetings)

    # Print the chosen greeting
    print(random_greeting + "I am the Acacia chat-bot how can I assist you today?, I can help you with information "
                            "about Africa University, from the Programs offered at the University to the various "
                            "sports and clubs you can join.")
