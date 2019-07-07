import os
import csv
election_csv = ('election_data.csv')

polls = []
names = []
total = 0
winner = 0
winner_name = ""
current_count = 0

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if(names.count(row[2]) == 0):
            names.append(row[2])
        
        polls.append(row[2])





print("Election Results")
print("------------------")
for name in names:
    current_count = polls.count(name)
    total = total + current_count
    if winner < current_count:
        winner = current_count
        winner_name = name
print(f"Total Votes: {total}")
print("------------------")
for name in names:
    print(f"{name}: {round(((polls.count(name)/total)*100), 3)}% ({polls.count(name)})")

print("------------------")
print(f"Winner: {winner_name}")
print("------------------")

f = open("resultsPoll.txt", "w")
f.write("Election Results\r\n")
f.write("------------------\r\n")
f.write(f"Total Votes: {total}\r\n")
f.write("------------------\r\n")
f.write(f"{name}: {round(((polls.count(name)/total)*100), 3)}% ({polls.count(name)})\r\n")
f.write("------------------\r\n")
f.write(f"Winner: {winner_name}\r\n")
f.write("------------------\r\n")
f.close()
