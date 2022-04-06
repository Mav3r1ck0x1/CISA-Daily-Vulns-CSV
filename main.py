import csv
from urllib import request
import datetime
import time
import os

#URL of the .csv file from CISA
dl = ('https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv')

#Local name is the name you want to save the file as locally
local_name = 'CVE-Vulns-Today.csv'
request.urlretrieve(dl, local_name)
time.sleep(2) #Sleep to give time for download, 5 seconds is usually overkill

#Check date of file to determine if fresh CVE added
check_file_update = os.path.getctime('CVE-Vulns-Today.csv')
date_check = datetime.datetime.fromtimestamp(check_file_update).strftime('%Y-%m-%d %H:%M')
print ('Date that CISA updated file: ',  date_check)

#Check date of file against todays date
if date_check == datetime.datetime.today():
    print ('UPDATED TODAY!')
else:
    print ('NOT YET UPDATED.')



#I shouldn't have to explain this
date = datetime.datetime.now()
print ('Current date and time: ', date)
time.sleep(7)


#Opens and prints the CSV data
with open(r'C:\Users\Blake Blackwell\PycharmProjects\CISADailyCSVParser\CVE-Vulns-Today.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)
