import csv


def handle_programs_list(user_input):
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

    # Print the filtered programs
    if filtered_programs:
        print("Here is a list of available programs:")
        for program in filtered_programs:
            print(f"Program: {program['program']}")
            print(f"Description: {program['description']}")
            print(f"Level: {program['level']}")
            print()
    else:
        print("No programs found.")
