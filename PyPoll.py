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

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
#with open(file_to_load, 'r') as election_data:
#    for each in election_data:
#        print(each)

# To do: perform analysis.
#for each_vote in election_data:
#    print (each_vote)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

# Close the file.
election_data.close()
