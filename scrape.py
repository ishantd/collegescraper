from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
import time
import json
import os
from pyvirtualdisplay import Display
import multiprocessing
from multiprocessing.pool import ThreadPool, Pool
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import itertools

#for server 
display = Display(visible=0, size=(800, 800))  
display.start()
#####

urls = ['https://www.shiksha.com/it-software/ai-robotics/colleges/colleges-india']

for i in range(2, 6):
    x = 'https://www.shiksha.com/it-software/ai-robotics/colleges/colleges-india-' + str(i)
    urls.append(x)

def get_college_links(page):
    page_links = []
    path = os.getcwd()
    chrome_driver = path + "/chromedriver"
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    # driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    driver.get(page)
    html = driver.page_source
    soup = bs(html,"html.parser")
    all_divs = soup.select('div.shadowCard.ctpCard')
    for a in all_divs:
        link = a.select_one('div.valueTxt a').get('href')
        link = "https://www.shiksha.com" + link 
        page_links.append(link)
    return page_links

big=[]
for url in urls:
    big.append(get_college_links(url))

ab = list(itertools.chain.from_iterable(big))

with open('all_college_links.txt', 'w') as f:
    for item in big:
        f.write("%s\n" % item)