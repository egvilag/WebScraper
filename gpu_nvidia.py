from bs4 import BeautifulSoup
import requests
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',"Accept-Language": "en-US"}
response = requests.get('https://developer.nvidia.com/cuda-gpus',headers=header).text
website = BeautifulSoup(response, 'lxml')


accordion = website.find(id = 'accordion')
gpu_link = []
for link in accordion.findAll('a', attrs={'href': re.compile(".html")}):
    gpu_link.append(link.get('href'))

print (gpu_link)
