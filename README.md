<img src="https://static.bc-edx.com/data/dl-1-2/m3/lms/img/banner.jpg" alt="lesson banner" />

### Background

It's time to put away the Excel sheet and enter the world of programming with Python. In this assignment, you'll use the concepts you've learned to complete **two** Python challenges, PyBank and PyPoll. Both tasks present a real-world situation where your newly developed Python scripting skills come in handy.

### Before You Begin

Before starting the assignment, be sure to complete the following steps:

* Create a new repository for this project called `python-challenge`. **Do not add this homework assignment to an existing repository**.

* Clone the new repository to your computer.

* Inside your local Git repository, create a folder for each Python assignment and name them `PyBank` and `PyPoll`.

* In each folder that you just created, add the following content:

  * A new file called `main.py`. This will be the main script to run for each analysis.

  * A `Resources` folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.

  * An `analysis` folder that contains your text file that has the results from your analysis.

* Push these changes to GitHub or GitLab.

### Files

Download the following files to help you get started:

[Module 3 Challenge files](https://static.bc-edx.com/data/dl-1-2/m3/lms/starter/Starter_Code.zip)

### PyBank Instructions

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called `budget_data.csv`. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

```text
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

Your analysis should align with the following results:

```text
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

In addition, your final script should both print the analysis to the terminal and export a text file with the results.

### Hints and Considerations

* Consider what you've learned so far. You've learned how to import modules like `csv`. You’ve learned how to read and write files in various formats. You’ve learned how to store content in variables, lists, and dictionaries. You’ve learned how to iterate through basic data structures. And you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.

* The datasets for these Challenges are quite large. This was done purposefully to showcase one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more powerful options for handling big data.

* Write one script for each of the provided datasets. Run each script separately to make sure that the code works for its respective dataset.

* Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed `README.md` file.

### Requirements

#### Correctly Reads in the CSV (10 points)

* Reads in the CSVs for both PyBank and PyPoll using Python (5 points)

* Successfully stores the header row (5 points)

#### Results Printed out to correctly to terminal (40 points)

* Results correctly display for PyBank:

  * Total Months (5 points)

  * Total (5 points)

  * Average Change (5 points)

  * Greatest Increase (5 points)

  * Greatest Decrease (5 points)

* Results correctly display for PyPoll:

  * Total Votes (5 points)

  * Each candidate’s total votes and percent of votes (5 points)

  * Winner (5 points)

#### Code Runs Error Free (10 points)

* Error Free (5 points)

* Producing consistent results (5 points)

#### Exports results to text file (30 points)

* The text file contains for PyBank:

  * Total Months (2.5 points)

  * Total (2.5 points)

  * Average Change (5 points)

  * Greatest Increase (5 points)

  * Greatest Decrease (5 points)

* The text file contains for Pypoll:

  * Total Votes (2.5 points)

  * Each candidate’s total votes and percent of votes (2.5 points)

  * Winner (5 points)

#### Code is cleaned and commented (10 points)

* Has additional tests and debugging removed (5 points)

* Commented (5 points)

### Grading

This assignment will be evaluated against the requirements and assigned a grade according to the following table:

| Grade | Points |
| --- | --- |
| A (+/-) | 90+ |
| B (+/-) | 80&ndash;89 |
| C (+/-) | 70&ndash;79 |
| D (+/-) | 60&ndash;69 |
| F (+/-) | < 60 |

### Submission

To submit your Challenge assignment, click Submit, and then provide the URL of your GitHub repository for grading.

> **Note** You are allowed to miss up to two Challenge assignments and still earn your certificate. If you complete all Challenge assignments, your lowest two grades will be dropped. If you wish to skip this assignment, click Next, and move on to the next module.

Comments are disabled for graded submissions in Bootcamp Spot. If you have questions about your feedback, please notify your instructional staff or your Student Success Manager. If you would like to resubmit your work for an additional review, you can use the Resubmit Assignment button to upload new links. You may resubmit up to three times for a total of four submissions.

### References

Data for this dataset was generated by edX Boot Camps LLC, and is intended for educational purposes only.
