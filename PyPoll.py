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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)
