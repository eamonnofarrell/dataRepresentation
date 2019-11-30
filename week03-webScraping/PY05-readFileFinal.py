from bs4 import BeautifulSoup
import csv

with open("carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"',  quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
#print(rows)
for row in rows:

    cols = row.findAll("td")[0:4]  #modify code so that update and delete is not outputted
    dataList = []
    for col in cols:
        dataList.append(col.text)
        #print(dataList)
    employee_writer.writerow(dataList)
employee_file.close()
