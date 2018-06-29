import os
import csv

file_input = "raw_data/budget_data_1.csv"

file_output = "analysis/budget_analysis_1.txt"

#Default variable for what we are looking for
total_months = 0
total_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
biggest_decr = ['', 99999999999]
biggest_incr = ['', 0]

with open(file_input) as revenue_data:  
    reader = csv.DictReader(revenue_data)
    
    for row in reader:

        #Count the total of months
        total_months += 1
        #Calculate the total revenue over the entire period
        total_revenue += int(row['Revenue'])

        #Calulate the average change in revenue between months over the entire period
        rev_change = int(row["Revenue"])- prev_revenue
        prev_revenue = int(row["Revenue"])
        revenue_change_list = revenue_change_list + [rev_change]
        month_of_change = month_of_change + [row["Date"]]
        #The greatest increase in revenue (date and amount) over the entire period
        if rev_change>biggest_incr[1]:
            biggest_incr[1]= rev_change
            biggest_incr[0] = row['Date']
        #The greatest decrease in revenue (date and amount) over the entire period
        if rev_change<biggest_decr[1]:
            biggest_decr[1]= rev_change
            biggest_decr[0] = row['Date']


#print(rev_change_list)
rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print('Average Change in Revenue: $ ' + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(total_revenue))
print(biggest_incr)
print(biggest_decr)



with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (biggest_incr[0], biggest_incr[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (biggest_decr[0], biggest_decr[1]))