from configparser import ConfigParser

cf =ConfigParser()
cf.read("setting.cfg")

keyword=input("keyword?")
if(not keyword in cf.sections()):
    cf.add_section(keyword)

for i in range(20):
    cf.set(keyword,str(i),str(i*2))

cf_open=open("setting.cfg", 'w')
cf.write(cf_open)
cf_open.close()

print("finished")



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


