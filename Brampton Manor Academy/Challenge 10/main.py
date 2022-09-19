#CHALLENGE 10
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
            dictionary[home] = [0,0]
        if away not in dictionary:
            dictionary[away] = [0,0]

        if winner == "D":
            dictionary[home][0] += 1
            dictionary[away][0] += 1
        elif winner == "H":
            dictionary[home][0] += 1
        elif winner == "A":
            dictionary[away][0] += 1
        
        #goal difference also needs to be calculated
        dictionary[home][1] = dictionary[home][1] + int(homegoals) - int(awaygoals)
        #goal difference for away team here
        dictionary[away][1] = dictionary[away][1] + int(awaygoals) - int(homegoals)
        #after this is done, you'll have all of the points and goal differences for each team
    return dictionary 

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    results = process_results(file_contents)
    for key, value in sorted(results.items(), key=lambda e: e[0][1]):
        print(key, value)