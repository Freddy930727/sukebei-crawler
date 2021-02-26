"""
from selenium import webdriver
import time
import os
from datetime import date
url="https://sukebei.nyaa.si/?s=seeders&o=desc&p=1"
driver_path = os.path.abspath('.\chromedriver.exe')
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)
driver.get(url)

while driver.title !="Browse :: Sukebei":
    driver.get(url)
    time.sleep(3)
temp="/html/body/div/div[1]/table/tbody/tr[12]/td[2]/a"
print(driver.find_element_by_xpath(temp).get_attribute("title")+" a")
temp="/html/body/div/div[1]/table/tbody/tr[12]/td[2]/a[1]"
print(driver.find_element_by_xpath(temp).get_attribute("title")+" 1")
temp="/html/body/div/div[1]/table/tbody/tr[12]/td[2]/a[2]"
print(driver.find_element_by_xpath(temp).get_attribute("title")+" 2")
temp="/html/body/div/div[1]/table/tbody/tr[13]/td[2]/a"
print(driver.find_element_by_xpath(temp).get_attribute("title")+" a")
temp="/html/body/div/div[1]/table/tbody/tr[13]/td[2]/a[1]"
print(driver.find_element_by_xpath(temp).get_attribute("title")+" 1")
temp="/html/body/div/div[1]/table/tbody/tr[13]/td[2]/a[2]"
#print(driver.find_element_by_xpath(temp).get_attribute("title")+"@6")
"""
from time import sleep
from threading import Thread
thread_stop=False

def animation():
    print("crawling...,please wait.",end='')
    animation = "|/-\\"
    idx=0
    while not thread_stop:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        sleep(0.1)
Thread(target=animation).start()
sleep(5)
print(35)
thread_stop=True
sleep(10)


