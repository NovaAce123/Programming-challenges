# CHALLENGE 10
import csv
from pathlib import Path

csv_file = Path("Premier 16-17.csv")


def check_file_exists(csv_file):
    return csv_file.is_file()


def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents


def process_results(rows):
    dictionary = {}
    for row in rows:
        home, away, homegoals, awaygoals, winner = row[1], row[2], row[3], row[4], row[5]

        if home not in dictionary:
            dictionary[home] = [0, 0, 0, 0, 0]
        if away not in dictionary:
            dictionary[away] = [0, 0, 0, 0, 0]

        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
            dictionary[home][3] += 1
            dictionary[away][3] += 1
        elif winner == "H":
            dictionary[home][0] += 3
            dictionary[home][2] += 1
            dictionary[away][4] += 1
        elif winner == "A":
            dictionary[away][0] += 3
            dictionary[home][4] += 1
            dictionary[away][2] += 1

        # goal difference also needs to be calculated
        dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)
        # goal difference for away team here
        dictionary[away][1] = dictionary[away][1] + int(awaygoals) - int(homegoals)
        # after this is done, you'll have all of the points and goal differences for each team
    return dictionary

file_contents = read_csv(csv_file)
sortedPoints = {k: v for k, v in sorted(process_results(file_contents).items(), key=lambda v: v[1][1] and v[1], reverse=True)}

def club_keys(sortedPoints):
    names = list(sortedPoints.keys())
    return names[i]

def points(sortedPoints):
    names = list(sortedPoints.keys())
    val = names[i]
    return sortedPoints[val][0]

def goal_diff(sortedPoints):
    names = list(sortedPoints.keys())
    val = names[i]
    return sortedPoints[val][1]

def wins(sortedPoints):
    names = list(sortedPoints.keys())
    val = names[i]
    return sortedPoints[val][2]

def draws(sortedPoints):
    names = list(sortedPoints.keys())
    val = names[i]
    return sortedPoints[val][3]

def losses(sortedPoints):
    names = list(sortedPoints.keys())
    val = names[i]
    return sortedPoints[val][4]


if __name__ == "__main__":
    results = process_results(file_contents)
    names = list(sortedPoints.keys())
    print(f"{'Clubs':<30} {'P':<5} {'GD':<5} {'W':<5} {'D':<5} {'L':<5}")
    print("_________________________________________________________")
    for i in range (0,len(names)):
        print(f"{club_keys(sortedPoints):<30} {points(sortedPoints):<5} {goal_diff(sortedPoints):<5} {wins(sortedPoints):<5} {draws(sortedPoints):<5} {losses(sortedPoints):<5}")
    #for key, value in sorted(results.items(), key=lambda e: e[0][1] and e[0][2]):
     #   print(key, value)
