import os
import csv

#Path to collect Budget Data
inputfile='\\Users\\molly\\Desktop\\UCI\\Homework\\python-challenge\\PyBank\\Resources\\budget_data.csv'
outputfile='\\Users\\molly\\Desktop\\UCI\\Homework\\python-challenge\\PyBank\\Resources\\budget_output.txt'

#Create Variables, lists and trackers
totalmonths = 0
totalrevenue = 0
pastrevenue = 0
highestincrev = 0
lowestdecrev = 99999999999
revenuechange = []

#Open CSV file and skip headers
with open(inputfile,newline=' ') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    next(budget_csvreader, none)

    #Loop through file
    for row in budget_csvreader:
        #Find The total number of months and revenue included in the dataset
        totalmonths = totalmonths + 1
        totalrevenue = totalrevenue + (int(row[1]))
        #The net total amount of "Profit/Losses" over the entire period
        monthlyrevchange = int(row[1]) - pastrevenue
        pastrevenue = int(row[1])
        revenuechange.append(monthlyrevchange)
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
