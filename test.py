import selenium

"""
from selenium import webdriver
from os import path
from time import sleep
url="https://sukebei.nyaa.si/?s=seeders&o=desc&p=1"
option = webdriver.ChromeOptions()
option.headless = True#remember
driver = webdriver.Chrome(path.abspath('.\chromedriver.exe'), options=option)
option.add_argument('blink-settings=imagesEnabled=false')
driver.implicitly_wait(20)
driver.get(url)
sleep(2)
for i in range(60):
    url="https://sukebei.nyaa.si/?s=seeders&o=desc&p="+str(i)
    print(len(driver.find_elements_by_class_name("success"))+len(driver.find_elements_by_class_name("default")))
"""


