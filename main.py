from selenium import webdriver
from time import sleep
from os import path
from os import mkdir
from os import listdir
from os import startfile
import os
from datetime import date
from datetime import datetime
from threading import Thread
#from pathlib import Path


import chromedriver_autoinstaller
chromedriver_autoinstaller.install()#not functioning

magnet_link='1'
if(not path.exists(".\downloads")):
    mkdir(".\downloads")
if(not path.exists(".\history")):
    mkdir(".\history")
while(not path.exists(".\chromedriver.exe")):
    print("please download latest version of chrome driver and put it in the same folder of this program(https://chromedriver.chromium.org/) ")
    sleep(5)
    
print("don't forget to update your chrome and chrome driver if it's not working properly(refer to readme.txt)")
temp=input("keyword filter ,1 for yes/2 for no(automatically search for torrent by  seeders)")
while(temp!="1" and temp!="2"):
    print("please input 1 or 2")#highlight
    temp=input("keyword filter ,1 for yes/2 for no(automatically search for torrent by  seeders)")
if(temp=="1"):
    keyword=input("please input the keyword?")
else:
    keyword="0"

file=open(".\history\\"+keyword+".txt","a+")
previous_list=file.readlines()
keyword='"'+keyword+'"'

temp=input("time filter ,1 for yes /2 for no (search for all time)?")
while(temp!="1" and temp!="2"):
    print("please input 1 or 2")#highlight
    temp=input("time filter ,1 for yes /2 for no (search for all time)?")
if(temp=="1"):
    asktime=True
    date=str(date.today().year)+"-"
    month =int(input("which month is it?"))
    while(month>12 or month<1):
        print("month should be a integer between 1~12")
        month =int(input("which month is it?"))
    if month<10:
        month="0"+str(month)
    month=str(month)
    day=int(input("which day is it?"))
    while(month>31 or month<1):
        print("date should be a integer between 1~31")
        date =int(input("which date is it?"))
    if day<10:
        day="0"+str(day)
    day=str(day)
    date=date+month+"-"+day
    print(date)
else:
    asktime=False
num = input("how many torrents do you require? ")
num=int(num)
while(num<1):
    print("please input a number which is greater than 0")
    num = input("how many torrents do you require?")
    num=int(num)

current_list=['']*num



print("which category would you prefer?")
category=input("(1)all categories (2)real life videos (3)anime (4)manga (5)pictures (6)doujinshi")
category=int(category)
while(category>6 or category<1):
    print("please input a number between 1 and 6")
    category=input("(1)all categories (2)real life videos (3)anime (4)manga (5)pictures (6)doujinshi")
    category=int(category)

torrent_or_magnet=input("(1)download by .torrent (2)download by magnet") #not complete yet
while(torrent_or_magnet!='1'and torrent_or_magnet!='2'):
    torrent_or_magnet=input("(1)download by .torrent (2)download by magnet")
download_path='1'
if(torrent_or_magnet=="1"):
    download_path=".\downloads\\"+datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    mkdir(download_path)
    print("download_path:"+download_path)
url="https://sukebei.nyaa.si/"
if keyword!="0":
    url=url+"?f=0&c=0_0&q="+keyword+"&s=seeders&o=desc"
else:
    url=url+"?s=seeders&o=desc"
url=url+"&p=1"
#timee="d"#not sure if it can be deleted
temp1=0
thread_stop=False

def animation():
    print("crawling...,please wait.",end="")
    animation = "|/-\\"
    idx=0
    while not thread_stop:
        print(animation[idx % len(animation)], end="\r")
        idx += 1
        sleep(0.1)
    print()
def badway_check():
    if(url==driver.title):
        page=7
        num=0
        return
    while not "Sukebei" in driver.title:
        driver.implicitly_wait(20)
        driver.get(url)
        sleep(2)
def maximum_check():
    if not "Sukebei" in driver.title:
        num=0#force stop crawling
        return True

Thread(target=animation).start()


option = webdriver.ChromeOptions()
#option.headless = True#remember
option.add_argument('blink-settings=imagesEnabled=false')
prefs = {"download.default_directory" : download_path}
option.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('.\chromedriver.exe', options=option)
driver.implicitly_wait(20)
driver.get(url)

tr=1
k=str(tr)
token=0
page=1#the first page
badway_check()
thread_stop=True

category=str(category)

if category=="1":
    category="all categories"
elif category=="2":
    category="Real Life - Videos"
elif category=="3":
    category="Art - Anime"
elif category=="4":
    category="Art - Manga"
elif category=="5":
    category="Art - Pictures"
elif category=="6":
    category="Art - Doujinshi"


def time_filter():
    temp="//tr["+k+"]/td[5]"
    temp=driver.find_element_by_xpath(temp).text
    timee=temp[:-6]
    if str(date) == str(timee):
        return True
    elif asktime==False:
        return True
    else:
        return False

def category_filter():
    temp="//tr["+k+"]/td[1]/a"
    temp1="//tr["+k+"]/td[1]/a"
    cate=driver.find_element_by_xpath(temp).get_attribute("title")
    if category==cate or category=="all categories":#category filter
        return True
    else:
        return False

def comment_check():
    temp="//tr["+k+"]/td[2]/a"
    if "comments" in driver.find_element_by_xpath(temp).get_attribute("title"):
        temp="//tr["+k+"]/td[2]/a[2]"
    return temp

def current_page_check():
    while(url!=driver.current_url):
        sleep(2)
        driver.back#not sure

def history_check():
    temp="//tr["+k+"]/td[3]/a[2]"
    global magnet_link
    magnet_link=driver.find_element_by_xpath(temp).get_attribute("href")
    if(magnet_link in previous_list or magnet_link in current_list ):
        return False
    else:
        return True

while True:
    if token>=num:#for badway_check compulsorily shut down
        break
    if tr== (1+(len(driver.find_elements_by_class_name("success"))+len(driver.find_elements_by_class_name("default")))):        
        tr=1
        temp=1
        temp1=page
        while temp1>=10:
            temp=temp+1
            temp1=temp1/10
        print(temp)
        url=url[:-(temp+3)]
        page=page+1   #flip the page
        url=url+"&p="+str(page)
        driver.get(url)
        badway_check()
        print(url)
        if maximum_check() and num!=-1:
            print("i can only find "+str(token)+" torrents,there are "+str(num-token)+" left")
            break
    k=str(tr)
    if(time_filter()):
        if(category_filter()):
            if(history_check()):
                if torrent_or_magnet=="1":
                    temp="//tr["+k+"]/td[3]/a[1]"
                    driver.find_element_by_xpath(temp).click()
                    current_page_check()
                elif torrent_or_magnet=="2":
                    temp="//tr["+k+"]/td[3]/a[2]"
                    startfile(magnet_link)       
                print(str(token+1)+". ",end = "")
                print(driver.find_element_by_xpath(comment_check()).get_attribute("title"))#don't modify the order of previous three line(including this one)
                current_list[token-1]=magnet_link
                
                token=token+1
    tr=tr+1
print("crawling finished")

file.writelines(current_list)
file.close()

if(torrent_or_magnet=='1'):
    thread_stop=False
    Thread(target=animation).start()#not sure
    
    for i in listdir(download_path):
        if(i.endswith('.crdownload')):
            sleep(8)
    thread_stop=True
    print("download finished!")
    startfile(download_path)
print("mission complete")
#sleep(7) #wait for the download finish completely,if your internet is fast enough you can just delete this line


