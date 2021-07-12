from bs4 import BeautifulSoup
import requests
import re

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)',"Accept-Language": "en-US"}
response = requests.get('https://www.zotac.com/hu/product/graphics_card/all',headers=header).text
website = BeautifulSoup(response, 'lxml')


pager = website.find_all(class_ = 'pager-item')
pages = []
pages.append('/hu/product/graphics_card/all')
for pager in website.find_all(class_ = 'pager-item'):
    pages.append(pager.a['href'])

zotac_website = 'https://www.zotac.com'
pages = [zotac_website + x for x in pages]

html_text = []
links = []
for i in range(len(pages)):
    html_text = requests.get(pages[i]).text
    website = BeautifulSoup(html_text, 'lxml')
    cells = website.find_all(class_ = 'blk-pdt vertical')
    for link in cells:
        links.append(link.find(class_ = 'details').a['href'])


links = [zotac_website + x for x in links]

data = []
f = open("gpu_zotac.txt", "w")
for i in range(len(links)):
    html_text = requests.get(links[i]).text
    website = BeautifulSoup(html_text, 'lxml')
    table = website.find(class_ = 'table-spec')
    for record in table.find_all(class_ = 'col-left'):

        f.write(record.text + ';')

    f.write('\n')

    for record in table.find_all(class_ = 'col-right'):
        f.write(record.text.replace('\r', '|') + ';')

    f.write('\n')
