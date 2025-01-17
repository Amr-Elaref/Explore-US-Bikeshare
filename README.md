# Explore-US-Bikeshare
Python Script to Explore US Bikeshare Data
________________________________________________________________________________________________________________

This Python script is written for Project 1 of Udacity's Professional Data Analyst Nanodegree (DAND) and is used to explore data related to bike share systems for Chicago, New York City, and Washington. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

How to run the script

You can run the script using a Python integrated development environment (IDE) such as Visual Studio Code. This script is written in Python 3.8, so you will need the Python 3.x version of the installer.

Datasets

The datasets used for this script contain bike share data for the first six months of 2017. Some data wrangling has been performed by Udacity's staff before being provided to the students of DAND. Under the permission of Udacity, I have uploaded a copy of the datasets here. The file sizes are too big to be uploaded on GitHub, so they were uploaded on Google Drive instead. After downloading the datasets, place them in the same folder with this Python script.

The data is provided by Motivate, which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
•	Start Time
•	End Time
•	Trip Duration (in seconds)
•	Start Station
•	End Station
•	User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
•	Gender
•	Birth Year

Questions explored

The script answers the following questions about the bike share data:
•	What is the most popular month for start time?
•	What is the most popular day of week (Monday, Tuesday, etc.) for start time?
•	What is the most popular hour of day for start time?
•	What is the total trip duration and average trip duration?
•	What is the most popular start station and most popular end station?
•	What is the most popular trip (from start station to end station)?
•	What are the counts of each user type?
•	What are the counts of gender? (not available for Washington)
•	What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years? (not available for Washington)
•	Raw data is displayed upon request by the user at last.
