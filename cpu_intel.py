from bs4 import BeautifulSoup
import requests
import re
import csv

#Processing the main processor list
intel_website = 'https://www.intel.com'
html_text = requests.get('https://www.intel.com/content/www/us/en/products/details/processors.html').text
website = BeautifulSoup(html_text, 'lxml')

ps_accordion_panel_0 = website.find(id = 'ps-accordion-panel-0')
ps_accordion_panel_1 = website.find(id = 'ps-accordion-panel-1')
ps_accordion_panel_2 = website.find(id = 'ps-accordion-panel-2')
ps_accordion_panel_3 = website.find(id = 'ps-accordion-panel-3')
#ps_accordion_panel_4 = website.find(id = 'ps-accordion-panel-4')   #intel doesn't have multiple types of Pentium cpus
ps_accordion_panel_5 = website.find(id = 'ps-accordion-panel-5')

cpu_type_links = []
cpu_type_links.append(ps_accordion_panel_0.find(class_ = 'group-title has-name').a['href'])
cpu_type_links.append(ps_accordion_panel_1.find(class_ = 'group-title has-name').a['href'])
cpu_type_links.append(ps_accordion_panel_2.find(class_ = 'group-title has-name').a['href'])
cpu_type_links.append(ps_accordion_panel_3.find(class_ = 'group-title has-name').a['href'])
#cpu_type_links.append(ps_accordion_panel_4.find(class_ = 'group-title has-name').a['href'])    #intel doesn't have multiple types of Pentium cpus
cpu_type_links.append(ps_accordion_panel_5.find(class_ = 'group-title has-name').a['href'])

#add intel website domain
cpu_type_links = [intel_website + x for x in cpu_type_links]

#Processing the individual Processor Type lists
links = []
for i in range(len(cpu_type_links)):
    print('checking types:', cpu_type_links[i])
    html_text = requests.get(cpu_type_links[i]).text
    website = BeautifulSoup(html_text, 'lxml')
    panels = website.find_all(id = 'ps-accordion-panel-0')
    for link in panels:
        links.append(link.find(class_ = 'panel-title').a['href'])

#add intel website domain
links = [intel_website + x for x in links]

#change to products page
for i in range(len(links)):
    links[i] = links[i].replace('.html', '/products.html')

#Processing the individual cpu types
cpu_link = []
for i in range(len(links)):
    print('checking this cpu:', links[i])
    html_text = requests.get(links[i]).text
    website = BeautifulSoup(html_text, 'lxml')
    table = website.find('table', class_ = 'table table-sorter').tbody

    for link in table.findAll('a', attrs={'href': re.compile("^/content/www/us/en/products/sku/")}):
        cpu_link.append(link.get('href'))


#add intel website domain
cpu_link = [intel_website + x for x in cpu_link]

#Processing every cpu's specs page
rows = []
for i in range(len(cpu_link)):
    html_text = requests.get(cpu_link[i]).text
    website = BeautifulSoup(html_text, 'lxml')
    print("page:",cpu_link[i])

    for record in website.find_all(class_ = 'col-xs-6 col-lg-6 tech-label'):
        rows.append(record.text.replace('\n', '') + ';')

    for record in website.find_all(class_ = 'col-xs-6 col-lg-6 tech-data'):
        rows.append(record.text.replace('\n', '') + ';')


with open('cpu_intel.csv', 'w') as csv_file:
     write = csv.writer(csv_file)
     for i in range(len(rows)):
         write.writerow(rows[i])
