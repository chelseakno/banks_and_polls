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

increaseDate={}
revenueIncrease=0

decreaseDate={}
revenueDecrease=0

count1 = 1

with open(csvpath,newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	next(csvreader, None)
	for row in csvreader:
		months = 1
		totalRevenue = totalRevenue + int(row[1])

		if count1 == 1:
			prevRowRev=int(row[1])
			increaseDate[row[0]]=int(row[1])
			decreaseDate[row[0]]=int(row[1])
			count1+=1
		elif int(row[1])>prevRowRev:
			if (int(row[1])> 0 and prevRowRev>0) or (int(row[1])<0 and prevRowRev<0):
				compI=abs(abs(int(row[1]))- abs(prevRowRev))
				monthChange.append(compI)
			else:
				compI=abs(abs(int(row[1]))+abs(prevRowRev))
				monthChange.append(compI)
			if compI>revenueIncrease:
				revenueIncrease=compI
				increaseDate={}
				increaseDate[row[0]]=(row[1])

		else:
			if (int(row[1])> 0 and prevRowRev>0) or (int(row[1])<0 and prevRowRev<0):
				compD=abs(abs(int(row[1]))- abs(prevRowRev))
				monthChange.append(compD)
			else:
				compD=abs(abs(int(row[1]))+abs(prevRowRev))
				monthChange.append(compD)
			if compD>revenueDecrease:
				revenueDecrease=compD
				decreaseDate={}
				decreaseDate[row[0]]=row[1]

sum1=0
for i in (monthChange):
	sum1+=float(i)
averageChange = sum1/(len(monthChange))

gtMonth=""
dcMonth=""
for u in increaseDate:
	gtMonth = u
	gtDollar=increaseDate[u]

for z in decreaseDate:
	dcMonth = z
	dcDollar=decreaseDate[z]


print("Financial Analysis")
print("----------------------------")
print("Total Months: "+ str(months))
print("Total Revenue: $"+ str(totalRevenue))

print("Average Revenue Change: $" + str(averageChange))
print("Greatest Increase in Revenue: "+ str(gtMonth)+" ($"+str(gtDollar)+")")
print("Greatest Decrease in Revenue: "+ str(dcMonth)+" ($"+str(dcDollar)+")")
print("---------------------------")


with open("pybank_analysis.txt","w") as text_file:
	text_file.write("Financial Analysis\n")
	text_file.write("----------------------------\n")
	text_file.write("Total Months: "+ str(months)+"\n")
	text_file.write("Total Revenue: $"+ str(totalRevenue)+"\n")
	text_file.write("Average Revenue Change: $" + str(averageChange)+"\n")
	text_file.write("Greatest Increase in Revenue: "+ str(gtMonth)+" ($"+str(gtDollar)+")\n")
	text_file.write("Greatest Decrease in Revenue: "+ str(dcMonth)+" ($"+str(dcDollar)+")\n")
	text_file.write("---------------------------")
