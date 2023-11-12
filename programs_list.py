import csv


def handle_programs_list(user_input):
    response = ""

    # Read the programs.csv file
    with open('programs.csv', 'r') as file:
        reader = csv.DictReader(file)
        programs = list(reader)

    # Filter programs based on user's specified level
    level = ''
    user_input = user_input.lower()

    if 'masters' in user_input:
        level = 'masters'
    elif 'bachelors' in user_input:
        level = 'bachelors'

    filtered_programs = []
    for program in programs:
        if level == '' or program['level'].lower() == level:
            filtered_programs.append(program)

    # Prepare the response
    if filtered_programs:
        response += "Here is a list of available programs:<br>"
        for program in filtered_programs:
            response += f"Program: {program['program']}<br>"
            response += f"Description: {program['description']}<br>"
            response += f"Level: {program['level']}<br><br>"
    else:
        response += "No programs found."

    return response
