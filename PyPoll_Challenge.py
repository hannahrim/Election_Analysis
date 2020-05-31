# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#county list and dictionary
county_list=[]
counties_dict={}


#empty string
largest_turnout=""
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
        
         #getting county names from each row
        county_name=row[1]
         #county does not match any existing in list
        if county_name not in county_list:
                county_list.append(county_name)
                counties_dict[county_name]=0
        counties_dict[county_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
     
     
    print(f"\n County Votes:\n")
    txt_file.write("\nCounty Votes:\n")

    current_max=0
    
    for county in counties_dict:
        #retrieve county vote percentage
        county_votes=counties_dict[county]
        county_percentage= int(county_votes)/int(total_votes)*100
        county_results= (
          
            f"{county}: {county_percentage:.1f}% ({county_votes:,})\n")

        if county_votes>current_max:
            current_max=county_votes
            largest_turnout=county

        print(county_results)
        txt_file.write(county_results)

    print(f"\n-------------------------") 
    txt_file.write("\n-------------------------")

    
    largest_countyresults= (
        f"\n Largest County Turnout: {largest_turnout}"
        "\n-------------------------\n")
    print(largest_countyresults)
    txt_file.write(largest_countyresults)

    



    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)