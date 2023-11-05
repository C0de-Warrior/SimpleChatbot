import csv


def handle_programs_search(user_input):
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

    # Print the filtered programs
    if filtered_programs:
        print("Here is a list of available programs:")
        for program in filtered_programs:
            print(f"Program: {program['program']}")
            print(f"Description: {program['description']}")
            print(f"Level: {program['level']}")
            print()
    else:
        print(
            "The program you are searching for is not offered at the university. Please choose from the available "
            "programs:")
        for program in programs:
            print(f"Program: {program['program']}")
            print(f"Description: {program['description']}")
            print(f"Level: {program['level']}")
            print()