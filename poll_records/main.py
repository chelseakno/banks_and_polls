import os
import csv

csvpath = os.path.join("/Users/chelseaknox/Desktop/creativity/data_analytics/python_homework/poll_records/election_data.csv")
print("Election Results")
print("__________________")
print()
votes = []
candidates = []

with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ',')
   csv_header = next(csvreader)

   for column in csvreader:
       votes.append(column[0])
       candidates.append(column[2])

   totalVotes = (len(votes))
   print(f"Total Votes: {totalVotes}")
   print("__________________")
   print()
   
   khan = int(candidates.count("Khan"))
   correy = int(candidates.count("Correy"))
   li = int(candidates.count("Li"))
   otooley = int(candidates.count("O'Tooley"))

   khanPercent = (khan/totalVotes) * 100
   correyPercent = (correy/totalVotes) * 100
   liPercent = (li/totalVotes) * 100
   otooleyPercent = (otooley/totalVotes) * 100

   print(f"Khan: {khanPercent}% ({khan})")
   print(f"Correy: {correyPercent}% ({correy})")
   print(f"Li: {liPercent}% ({li})")
   print(f"O'Tooley: {otooleyPercent}% ({otooley})")

   if khan > correy > li > otooley:
       winner = "Khan"
   elif correy > khan > li > otooley:
       winner = "Correy"
   elif li > khan > correy > otooley:
       winner = "Li"
   elif otooley > khan > correy > li:
       winner = "O'Tooley"
   print("__________________")
   print(f"Winner: {winner}")

outputPath = os.path.join("election_analysis.txt")
with open(outputPath, 'w', newline='') as txtfile:
   txtfile.write(f"Total Votes: {totalVotes}")
   txtfile.write("__________________")
   txtfile.write(f"Khan: {khanPercent}% ({khan})")
   txtfile.write("__________________")
   txtfile.write(f"Correy: {correyPercent}% ({correy})")
   txtfile.write("__________________")
   txtfile.write(f"Li: {liPercent}% ({li})")
   txtfile.write("__________________")
   txtfile.write(f"O'Tooley: {otooleyPercent}% ({otooley})")
   txtfile.write("__________________")
   txtfile.write(f"Winner: {winner}")
