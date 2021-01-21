import os
import csv

csvpath = os.path.join("/Users/chelseaknox/Desktop/creativity/data_analytics/python_homework/bank_records/budget_data.csv")

totalRevenue = 0
months = 0

comp=0
compI =0
compD=0

monthChange = []

prevRowRevenue=0
prevRowDate=""
#need a dictionary and variable to keep track of greatest increase date and revenue
greatest_inc={}
greatI=0

#need a dictionary and variable to keep track of greatest decrease date and revenue
greatest_dec={}
greatD=0
#setting a variable to insure that the first row of information is stored into initial variables
count1 = 1
#print(count1)

with open(csvpath,newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
#skipping the first row of headers in csv file
	next(csvreader, None)
	#for comparison, setting first row of data as initialization
	for row in csvreader:
		months = 1
		#print(row[1])
		totalRevenue = totalRevenue + int(row[1])

		if count1 == 1:
			prev_row_rev=int(row[1])
			greatest_inc[row[0]]=int(row[1])
			greatest_dec[row[0]]=int(row[1])
			count1+=1
			#print(count1)
		elif int(row[1])>prev_row_rev:
			if (int(row[1])> 0 and prev_row_rev>0) or (int(row[1])<0 and prev_row_rev<0):
				compI=abs(abs(int(row[1]))- abs(prev_row_rev))
				monthChange.append(compI)
			else:
				compI=abs(abs(int(row[1]))+abs(prev_row_rev))
				monthChange.append(compI)
			if compI>greatI:
				greatI=compI
				greatest_inc={}
				greatest_inc[row[0]]=(row[1])

		else:
			if (int(row[1])> 0 and prev_row_rev>0) or (int(row[1])<0 and prev_row_rev<0):
				compD=abs(abs(int(row[1]))- abs(prev_row_rev))
				monthChange.append(compD)
			else:
				compD=abs(abs(int(row[1]))+abs(prev_row_rev))
				monthChange.append(compD)
			if compD>greatD:
				greatD=compD
				greatest_dec={}
				greatest_dec[row[0]]=row[1]

#print(change)

#Average change we should now be able to take the change list, sum all values and divide by length
#	to obtain the average change between the months
sum1=0
for i in (monthChange):
	sum1+=float(i)
avg_change = sum1/(len(monthChange))

gt_month=""
dc_month=""
for u in greatest_inc:
	gt_month = u
	gt_dollar=greatest_inc[u]

for z in greatest_dec:
	dc_month = z
	dc_dollar=greatest_dec[z]


print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(months))
print("Total Revenue: $"+ str(totalRevenue))

print("Average Revenue Change: $" + str(avg_change))
print("Greatest Increase in Revenue: "+ str(gt_month)+" ($"+str(gt_dollar)+")")
print("Greatest Decrease in Revenue: "+ str(dc_month)+" ($"+str(dc_dollar)+")")
print("---------------------------")


with open("pybank_analysis.txt","w") as text_file:
	text_file.write("Financial Analysis\n")
	text_file.write("----------------------------\n")
	text_file.write("Total Months: "+ str(months)+"\n")
	text_file.write("Total Revenue: $"+ str(totalRevenue)+"\n")
	text_file.write("Average Revenue Change: $" + str(avg_change)+"\n")
	text_file.write("Greatest Increase in Revenue: "+ str(gt_month)+" ($"+str(gt_dollar)+")\n")
	text_file.write("Greatest Decrease in Revenue: "+ str(dc_month)+" ($"+str(dc_dollar)+")\n")
	text_file.write("---------------------------")
