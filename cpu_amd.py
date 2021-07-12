from bs4 import BeautifulSoup
import requests
import csv
import time

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',"Accept-Language": "en-US"}
response = requests.get('https://www.amd.com/en/products/specifications/processors',headers=header).text
website = BeautifulSoup(response, 'lxml')

table_head = website.find('thead')
table_body = website.find('tbody')

headers = []
for element in table_head.findAll('th'):
    headers.append(element.text.replace('\n' , '').replace('\xb9', '1').replace('\xb2', '2'))
headers.pop(0)

rows = []
data = []
for row in table_body.findAll('tr'):
    for element in row.findAll('td'):
        rows.append(element.text.replace('\n' , '').replace('\u200b', ''))
    rows.pop(0)
    data.append(rows)
    rows = []

with open('cpu_amd.csv', 'w') as csv_file:
     write = csv.writer(csv_file)
     write.writerow(headers)
     for i in range(len(data)):
         write.writerow(data[i])
