from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import re
import time

#
html_text = requests.get('https://www.cpu-monkey.com/en/benchmarks').text
website = BeautifulSoup(html_text, 'lxml')

benchmark = website.find(class_ = 'full_col frame')

benchmark_links = []
benchmark_names = []
for record in benchmark.findAll('li'):
    benchmark_names.append(record.text)
    benchmark_links.append(record.a['href'])

cpu_monkey_website = "https://www.cpu-monkey.com/en/"
benchmark_links = [cpu_monkey_website + x for x in benchmark_links]

for i in range(len(benchmark_links)):
    #headless
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    PATH = ''
    #headless
    #driver = webdriver.Chrome(PATH, options=chrome_options)
    driver = webdriver.Chrome(PATH)

    driver.get(benchmark_links[i])

    #clickity-click
    #search = driver.find_element_by_id("load_benchmarks")

    try:
        search = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "load_benchmarks"))
        )
        search.send_keys(Keys.RETURN)
    except:
        continue

    time.sleep(1)

    table = driver.find_element_by_class_name("data")
    table2 = driver.find_element_by_id("benchmark_data")

    data = table.text.split("\n")
    data2 = table2.text.split("\n")

    k = 3
    del data[k-2::k]
    del data2[k-2::k]

    data = [data + ";" for data in data]
    data2 = [data2 + ";" for data2 in data2]

    data = data + data2

    data = ''.join(data)
    data = re.sub('(;[^;]*);', r'\1\n', data)

    f = open("bench_" + benchmark_names[i] + ".txt", "w")
    f.write(data)
    f.close()

    driver.quit()
