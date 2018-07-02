# Import Libraries
import os
import csv

# Set File Path for Input and Output
csvpath = "Resources/election_data.csv"
file_output = "analysis/poll_results.txt"
# Declaring the Variables 
total_votes = 0
candidates = {}
candidates_percent = {}
winner_count = 0
winner = ""

# Read the File
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)
    for row in csvreader:
        # Find the total vote count
        total_votes += 1
        #Find the list of candidates a well as the number of
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        # percentages for each candidate by pulling info from items in the candidates dictionary
        # candidates dictionary: key= Name value= the number of votes
        for key, value in candidates.items():
            candidates_percent[key] = round((value/total_votes) * 100, 1)

        # Finding the winner using the candidates dictionary. 
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]


# Print tests
#print("Election Results")
#print("-------------------------------------")
#print("Total Votes: " + str(total_votes))
#print("-------------------------------------")
#for key, value in candidates.items():
#    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
#print("-------------------------------------")
#print("Winner: " + winner)
#print("-------------------------------------")


# writing the new file
with open(file_output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")
