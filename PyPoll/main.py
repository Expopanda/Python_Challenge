import os
import csv

candidate_list = []
vote_dic = {}

electiondata_csv = os.path.join("Resources", "election_data.csv")

with open(electiondata_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for i in csvreader:
        candidate_name = i[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            vote_dic[candidate_name] = 0
        vote_dic[candidate_name] += 1

#print(candidate_list)
#print(vote_dic)

totalvotes = sum(vote_dic[item] for item in vote_dic)
#print(totalvotes)

vote_list = [*vote_dic.values()]

ccsvoteper = (vote_list[0]) / totalvotes * 100
ddvoteper = (vote_list[1]) / totalvotes * 100
radvoteper = (vote_list[2]) / totalvotes * 100

winner = max(ccsvoteper, ddvoteper, radvoteper)
if winner == ccsvoteper:
    winner = candidate_list[0]
if winner == ddvoteper:
    winner = candidate_list[1]
if winner == radvoteper:
    winner = candidate_list[2]

output =(
f"Election Results\n"
f"----------------------------\n"
f"Total Votes: {totalvotes}\n"
f"----------------------------\n"
f"{candidate_list[0]}: ({ccsvoteper:.3f}%) {vote_list[0]}\n"
f"{candidate_list[1]}: ({ddvoteper:.3f}%) {vote_list[1]}\n"
f"{candidate_list[2]}: ({radvoteper:.3f}%) {vote_list[2]}\n"
f"----------------------------\n"
f"Winner: {winner}\n"
f"----------------------------"
)

print(output)

polldata_txt = os.path.join("analysis", "poll_analysis.txt")

with open(polldata_txt,"w") as txtfile:
    txtfile.write(output)