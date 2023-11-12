import csv


def handle_programs_search(user_input):
    response = ""

    # Read the programs.csv file
    with open('programs.csv', 'r') as file:
        reader = csv.DictReader(file)
        programs = list(reader)

    # Break down user input into individual words
    user_words = user_input.lower().split()

    # Filter programs based on user's specified level
    level = ''
    if 'masters' in user_words:
        level = 'masters'
    elif 'bachelors' in user_words:
        level = 'bachelors'

    # Filter programs based on user input words and level
    filtered_programs = []
    for program in programs:
        program_words = program['program'].lower().split()
        if level == program['level'].lower():
            filtered_programs.append(program)
        elif level == '' and any(word in program_words for word in user_words):
            filtered_programs.append(program)

    # Prepare the response
    if filtered_programs:
        response += "Here is a list of available programs:<br>"
        for program in filtered_programs:
            response += f"Program: {program['program']}<br>"
            response += f"Description: {program['description']}<br>"
            response += f"Level: {program['level']}<br><br>"
    else:
        response += ("The program you are searching for is not offered at the university. Please choose from the "
                     "available programs:<br>")
        for program in programs:
            response += f"Program: {program['program']}<br>"
            response += f"Description: {program['description']}<br>"
            response += f"Level: {program['level']}<br><br>"

    return response
