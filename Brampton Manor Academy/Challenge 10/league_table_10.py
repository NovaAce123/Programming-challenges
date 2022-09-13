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

def teamls(csv_contents):
    teamls = []
    for currentrow in csv_contents:
        i = currentrow[1]
        if i not in teamls:
            teamls.append(i)
    return teamls


def win_team(currentrow):
    if currentrow[5] == "A":
        win_team = row[2]
    elif currentrow[5] == "H":
        win_team = row[1]
    else:
        win_team = "draw"
    return win_team


if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    teamls(read_csv(csv_file))