# Read data into Python from CSV file
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join( 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #Create empty lists
    vote = []
    candidate = []

    # Read each row of data after the header 
    #iterating over each row and append values to empty list
    for col in csvreader:
        vote.append(col[0])
        candidate.append(col[2])
    #print(set(candidate))    
    #output{'Diana DeGette', 'Raymon Anthony Doane', 'Charles Casper Stockham'}

    #count total number of votes of each candidate:
    Vote_CCS = candidate.count('Charles Casper Stockham')
    Vote_DD = candidate.count('Diana DeGette')
    Vote_RAD = candidate.count('Raymon Anthony Doane')

    #calc precentage of votes each candidate won
    Prec_CCS = round(Vote_CCS/len(vote)*100,3)
    Prec_DD = round(Vote_DD/len(vote)*100,3)
    Prec_RAD = round(Vote_RAD/len(vote)*100,3)
    
    #Find the winner
    #Dictionay with all election results:
    Election_result = {"Diana DeGette":Vote_DD, 'Raymon Anthony Doane':Vote_RAD, 'Charles Casper Stockham':Vote_CCS }
    winner = max(Election_result, key=Election_result.get)

    #print list
    print("Election Results")
    print("-------------------------------------")
    print("Total Votes:", len(vote)) 
    print("-------------------------------------")
    print("Charles Casper Stockham:",Prec_CCS,"%","(", str(Vote_CCS), ")")
    print("Diana DeGette:",Prec_DD,"%","(", str(Vote_DD), ")")
    print("Raymon Anthony Doane:",Prec_RAD,"%","(", str(Vote_RAD), ")")
    print("-------------------------------------")
    print("Winner:", winner)
    print("-------------------------------------")