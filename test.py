import csv

with open('help.csv', 'r') as file:
    reader = csv.DictReader(file)
    sports = list(reader)

print("Number of sports:", len(sports))
print(sports)
