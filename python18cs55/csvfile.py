import csv,os
file = open('file.csv')
filereader = csv.reader(file)
data = list(filereader)
i=0
outputfile = open('output.csv','w',newline='')
outputwriter = csv.writer(outputfile,delimiter='\t',lineterminator='\n\n')
for r in data:
    i+=1
    outputwriter.writerow([i,r])


for csvfilename in os.listdir('.'):
    if not csvfilename.endswith('.csv'):
        continue
    print("removing headers from csv file",csvfilename,'......')

