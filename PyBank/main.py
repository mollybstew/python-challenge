import os
import csv

#define the path to the file 
budget_csvpath = '\\Users\\molly\\Desktop\\UCI\\Homework\\python-challenge\\PyBank\\Resources\\budget_data.csv'

#create trackers
total_months = 0
total_revenue = 0
past_revenue = 0
highest_inc_revenue = 0
revenue_change = []
lowest_dec_revenue = 0

#read csv file
with open(budget_csvpath, newline='') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    next(budget_csvreader, None)
    
    for row in budget_csvreader:
        #count total months in csv file
        total_months = total_months + 1
        #count total revenue in csv file
        total_revenue = total_revenue + (int(row[1]))
        #create a variable that will count the revenue change
        monthly_rev_change = int(row[1]) - past_revenue
        past_revenue = int(row[1])
        #add changes in new list
        revenue_change.append(monthly_rev_change)
        
        #calculate the average change in revenue
        avg_rev_change = round(sum(revenue_change)/total_months)
        
        #find the greatest increase in revenue
        if (monthly_rev_change > highest_inc_revenue):
            highest_inc_month = row[0]
            highest_inc_revenue = monthly_rev_change 
        #find the greatest decrease in revenue
        if (monthly_rev_change < lowest_dec_revenue):
            lowest_dec_month = row[0]
            lowest_dec_revenue = monthly_rev_change

#create varible to hold finanical analysis results and use f-strings for formatting
results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {total_months} \n"
f"Total Revenue: ${total_revenue} \n"
f"Average Revenue Change: ${avg_rev_change} \n"
f"Greatest Increase in Revenue: {highest_inc_month} (${highest_inc_revenue}) \n"
f"Greatest Decrease in Revenue: {lowest_dec_month} (${lowest_dec_revenue}) \n")
print(results)

#Write a text file to export results
outputfile='\\Users\\molly\\Desktop\\UCI\\Homework\\python-challenge\\PyBank\\Resources\\budget_output.txt'

with open(outputfile, 'w') as txtfile:
    txtwriter = txtfile.write(results)