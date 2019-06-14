import os
import csv

#Path to collect Election Data
csvpath='\\Users\\molly\\Desktop\\UCI\\python-challenge\\PyPoll\\Resources\\election_data.csv'

# Set the Varibales and define the lists
total_votes = 0
candidate_list = []
candidate_name = []
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

# define the path to the file that contains the results of the election
with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader, None)

     # loop through entire file to count total votes, add names to the candidate_name list, and votes per candidate
    for row in csv_reader:
        total_votes += 1
        candidate_list.append(str(row[2]))
        
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1

    # Calculate the percentage of the total votes for each candidate
    candidate_vote_percent[0] = round((candidate_vote[0] / total_votes) * 100, 2)
    candidate_vote_percent[1] = round((candidate_vote[1] / total_votes) * 100, 2)
    candidate_vote_percent[2] = round((candidate_vote[2] / total_votes) * 100, 2)
    candidate_vote_percent[3] = round((candidate_vote[3] / total_votes) * 100, 2)

    # Determine who the winner is
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[3]

# print the report to the terminal screen
results = (
f"Election Results \n"
f"----------------------------- \n"
f"Total Votes: {total_votes} \n"
f"----------------------------- \n"
f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]}) \n"
f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]}) \n"
f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]}) \n"
f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]}) \n"
f"----------------------------- \n"
f"Winner: {candidate_winner}")
print(results)

#Write a text file to export results
outputfile='\\Users\\molly\\Desktop\\UCI\\python-challenge\\PyPoll\\Resources\\election_output.txt'

with open(outputfile, 'w') as txtfile:
    txtwrite = txtfile.write(results)