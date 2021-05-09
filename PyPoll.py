#Data we need to retrieve
#total number of votes cast
#A complete list of candidates who received votes
# The percentage of votes each candidate won
# Total number of votes each candidate won
# The winner of the election based on the popular votes
import os
import csv


'''Assign a variable for the file to load and the path.'''
file_to_load = os.path.join("Resources", "election_results.csv")
'''Open the election results and read the file'''
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total_votes = 0
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)



    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Winning Candidate Summary
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # print(winning_candidate_summary)
