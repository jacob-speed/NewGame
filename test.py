from Functions import highscore

print(highscore())

import csv

def get_high_score():
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        scores = [float(row[0]) for row in reader]
    return max(scores)

high_score = get_high_score()

print(get_high_score())