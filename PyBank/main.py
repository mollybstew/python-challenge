import os
import csv

#define the path to the file 
budget_csvpath = '\\Users\\molly\\Desktop\\UCI\\python-challenge\\PyBank\\Resources\\budget_data.csv'

#create trackers
total_months = 0
total_revenue = 0
last_month_rev = 0
this_month_rev = 0
highest_inc_revenue = 0
lowest_dec_revenue = 0
revenue_changes = []
months = []

#read csv file
with open(budget_csvpath, newline='') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    next(budget_csvreader, None)
    
    for row in budget_csvreader:
        total_months = total_months + 1
        months.append(row[0])
        this_month_rev = int(row[1])
        total_revenue = total_revenue + this_month_rev
        if total_months > 1:
            rev_change = this_month_rev - last_month_rev
            revenue_changes.append(rev_change)
        last_month_rev = this_month_rev
        
        
        #find the greatest increase in revenue
        if (rev_change > highest_inc_revenue):
            highest_inc_month = row[0]
            highest_inc_revenue = rev_change 
        #find the greatest decrease in revenue
        if (rev_change < lowest_dec_revenue):
            lowest_dec_month = row[0]
            lowest_dec_revenue = rev_change
            
#calculate the average change in revenue
avg_rev_change = round(sum(revenue_changes)/(total_months-1), 2)

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
outputfile='\\Users\\molly\\Desktop\\UCI\\python-challenge\\PyBank\\Resources\\budget_output.txt'

with open(outputfile, 'w') as txtfile:
    txtwriter = txtfile.write(results)