from bs4 import BeautifulSoup
import requests
import re

website_link = 'https://www.cpubenchmark.net/'
html_text = requests.get(website_link).text
website = BeautifulSoup(html_text, 'lxml')

cmps = website.find(class_ = 'search-cmps')

benchmarks = []
benchmark_names = []
for benchmark in cmps.findAll('a'):
    benchmarks.append(benchmark.get('href'))
    benchmark_names.append(benchmark.text.replace('\n',''))

benchmarks = [website_link + x for x in benchmarks]

for i in range(len(benchmarks)):
    html_text = requests.get(benchmarks[i]).text
    website = BeautifulSoup(html_text, 'lxml')

    charts = website.find(id = 'mark')

    f = open("bench_" + benchmark_names[i] + ".txt", "w")
    cpus = []
    for product in charts.find_all('li'):
        f.write(product.find(class_='prdname').text + ';')
        f.write(product.find(class_='count').text + '\n')
    f.close()
