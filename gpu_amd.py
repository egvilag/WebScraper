from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',"Accept-Language": "en-US"}
response = requests.get('https://www.amd.com/en/products/specifications/graphics',headers=header).text
website = BeautifulSoup(response, 'lxml')

table_header = []
for record in website.findAll('th'):
    table_header.append(record.text.replace('\n\n', '') + ';')

table_data = []
for record in website.findAll('td'):
   table_data.append(record.text.replace('\n\n', '') + ';' + '\n')

f = open("gpu_amd.txt", "wb")

for element in table_header:
    f.write(element.encode('utf-8'))

for i in range(len(table_data)):
    table_data[i] = table_data[i].replace('\n', '')

new_line = '\n'
f.write(new_line.encode('utf-8'))

for element in table_data:
    f.write(element.encode('utf-8'))

f.close()
