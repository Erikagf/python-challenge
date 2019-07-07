import os
import csv
budget_csv = ('budget_data.csv')

total_months = []
net_total = 0
avg_change = 0
lastamount = 0
avg_month = 0
profit = 0
loss = 0
profit_m = ""
loss_m = ""


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        net_total += int(row[1])

        if(lastamount != 0):
            avg_change = avg_change + (int(row[1]) - lastamount)
            avg_month = avg_month + 1

            if(((int(row[1]) - lastamount) > 0) & (profit < (int(row[1]) - lastamount)) ):
                profit = (int(row[1]) - lastamount)
                profit_m = row[0]


            
            if(((int(row[1]) - lastamount) < 0)  &  (loss > (int(row[1]) - lastamount)) ):
                loss  = (int(row[1]) - lastamount)
                loss_m = row[0]

        lastamount = int(row[1])
        

        if(total_months.count(row[0]) == 0):
            total_months.append(row[0])
        
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(avg_change/avg_month, 2)}")
    print(f"Greatest Increase in Profits: {profit_m} (${profit})")
    print(f"Greatest Decrease in Profits: {loss_m} (${loss})")

#r stands for carraige return and n stands for new line, its like alt-ent in excel for a cell

f = open("results.txt", "w")
f.write("Financial Analysis\r\n")
f.write("------------------\r\n")
f.write(f"Total Months: {len(total_months)}\r\n")
f.write(f"Total: ${net_total}\r\n")
f.write(f"Average Change: ${round(avg_change/avg_month, 2)}\r\n")
f.write(f"Greatest Increase in Profits: {profit_m} (${profit})\r\n")
f.write(f"Greatest Decrease in Profits: {loss_m} (${loss})\r\n")
f.close()














 



  
