import csv
import os
from urllib import request
import datetime
import time

dl = ('https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv')

local_name = 'CVE-Vulns-Today.csv'
request.urlretrieve(dl, local_name)
time.sleep(5)

date = datetime.datetime.now()
print ('Current date and time: ', date)

with open(r'C:\Users\Blake Blackwell\PycharmProjects\CISADailyCSVParser\CVE-Vulns-Today.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

