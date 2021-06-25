# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Add total vote counter
total_votes = 0
# Getting candidates.
candidate_options = []
# Create a candidate_votes dictionary.
candidate_votes = {}
# Winning Candidate and Winning Count Tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader) 
    # Print each row in the CSV file.
    for row in file_reader:
        # Add the total vote count.
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Counting candidate votes.
        candidate_votes[candidate_name] += 1

# Save the results fo our text file.
with open(file_to_save,"w") as txt_file:
    # After opening the file print the final vote count ot the terminal.
    election_results = (f"\nElection Results\n"f"-------------------------\n"f"Total Votes: {total_votes:,}\n"f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the termina lsave the final vote.
    txt_file.write(election_results)
    # Determine the percentage of votes for each cnadidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes)/float(total_votes)*100
        # Determine the winning vote count and candidate.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    # print out each candidates name, vote count, and percentage of votes.
    winning_candidate_summary = (f"-------------\n"f"Winner: {winning_candidate}\n"f"Winning Vote Count: {winning_count:,}\n"f"Winning Percentage: {winning_percentage:.1f}%\n"f"-----------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)




















































