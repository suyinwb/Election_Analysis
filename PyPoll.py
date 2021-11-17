#Election Results

#* Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Import the datetime class from the datetime module.
import datetime as dt
import csv
import os

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Assign a variable for the file to load and the path.
#file_to_load = 'resources/election_results.csv'
file_to_load = os.path.join("resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    #print(headers)

# Print each row in the CSV file.
    for row in file_reader:
        print(row)
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

       # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)

# 3. Print the total votes.
print(total_votes)


# To do: perform analysis.
#for each_vote in election_data:
#    print (each_vote)



# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file.
election_data.close()
