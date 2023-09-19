import os
import csv


month_list = []
amount_list = []
change_list = []
counter = 0

budgetdata_csv = os.path.join("Resources", "budget_data.csv")

with open(budgetdata_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    #row_count = sum(1 for row in budgetdata_csv)
    for i in csvreader:
        #print(i[0])
        month_list.append(i[0])
        amount_list.append(int(i[1]))
        if counter > 0:
            change = int(i[1]) - previous_amount
            change_list.append(change)
        counter += 1
        previous_amount = int(i[1])
        

#print(len(month_list))
#print(sum(amount_list))
average_change = round(sum(change_list)/len(change_list),2)
#print(average_change)

max_increase = max(change_list)
max_decrease = min(change_list)
#print(max_increase,max_decrease)

max_index = change_list.index(max_increase)
min_index = change_list.index(max_decrease)

max_month = month_list[max_index+1]
min_month = month_list[min_index+1]

#print(min_month,max_month)



output =(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {len(month_list)}\n"
f"Total: ${sum(amount_list)}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_month} (${max_increase})\n"
f"Greatest Decrease in Profits: {min_month} (${max_decrease})"
)

print(output)

budgetdata_txt = os.path.join("analysis", "budget_analysis.txt")

with open(budgetdata_txt,"w") as txtfile:
    txtfile.write(output)

