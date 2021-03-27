import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
  
    date=[]
    PL=[]
    net_PL=0
    change=[]
    G_Inc=0
    G_Inc_D=0
    G_Dec=0
    G_Dec_D=0
    
    for row in csvreader:
        date.append(row[0])
        PL.append(row[1])
        net_PL+=int(row[1])
        
    for month in range(1,len(date)):
        change.append(int(PL[month])-int(PL[month-1]))
        
    for month in range(len(date)):
        if int(PL[month]) > int(G_Inc):
            G_Inc=PL[month]
            G_Inc_D=date[month]
        elif int(PL[month]) < int(G_Dec):
            G_Dec=PL[month]
            G_Dec_D=date[month]
       
    
    avg=(sum(change)/len(change))
    avg=round(avg,2)
    
    months=len(date)
    def analysis():
        print(
            f'Financial Analysis\n----------------------------\nTotal Months: {months}\nTotal: ${net_PL} \nAverage Change: ${avg}\nGreatest Increase in Profits: {G_Inc_D} ${G_Inc}\nGreatest Decrease in Profits: {G_Dec_D} ${G_Dec}')      
    analysis()

    output_path = os.path.join("Analysis", "Analysis.txt")
   
    with open(output_path, 'w', newline='') as newfile:

            newfile.write('Financial Analysis\n')
            newfile.write('Total Months: ' + str(months)+'\n')
            newfile.write('Total: $'+str(net_PL)+ '\n')
            newfile.write('Average Change: $'+str(avg)+'\n')
            newfile.write('Greatest Increase in Profits: '+str(G_Inc_D)+' $'+str(G_Inc)+'\n')
            newfile.write('Greatest Decrease in Profits: '+str(G_Dec_D)+' $'+str(G_Dec))
    