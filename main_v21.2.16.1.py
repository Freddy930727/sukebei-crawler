from selenium import webdriver
from time import sleep
from os import path
from datetime import date
from threading import Thread
#import chromedriver_autoinstaller
#chromedriver_autoinstaller.install()#not functioning
temp=input("keyword filter ,1 for yes/2 for no(automatically search for maximum seeders torrent)")
while(temp!="1" and temp!="2"):
    print("please input 1 or 2")#highlight
    temp=input("keyword filter ,1 for yes/2 for no(automatically search for maximum seeders torrent)")

if(temp=="1"):
    keyword='"'+input("please input the keyword?")+'"'
else:
    keyword=0
temp=input("time filter ,1 for yes /2 for no (search for all time)?")
while(temp!="1" and temp!="2"):
    print("please input 1 or 2")#highlight
    temp=input("time filter ,1 for yes /2 for no (search for all time)?")
if(temp=="1"):
    asktime=True
    date=str(date.today().year)+"-"
    month =int(input("which month is it?"))
    if month<10:
        month="0"+str(month)
    month=str(month)
    day=int(input("which day is it?"))
    if day<10:
        day="0"+str(day)
    day=str(day)
    date=date+month+"-"+day
    print(date)
else:
    asktime=False
num = input("how many torrents do you require? if you don't have any idea please input -1,and it will crwal until you close the program manually")
num=int(num)
while(num==0 or num<-1):
    print("please input a number which is greater than 0 or just input -1")
print("which category would you prefer?")
category=input("(1)all categories (2)real life videos (3)anime (4)manga (5)pictures (6)doujinshi")
category=int(category)
while(category>6 or category<1):
    print("please input a number between 1 and 6")
    category=input("(1)all categories (2)real life videos (3)anime (4)manga (5)pictures (6)doujinshi")
    
#magnet_ask=input("(1)download by .torrent (2)download by magnet") #not complete yet
magnet_ask="1"
url="https://sukebei.nyaa.si/"
if keyword!=0:
    url=url+"?f=0&c=0_0&q="+keyword+"&s=seeders&o=desc"
else:
    url=url+"?s=seeders&o=desc"
url=url+"&p=1"
timee="d"#not sure if it can be deleted
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
        x=7
        num=1
        return
    while not "Sukebei" in driver.title:
        sleep(2)
        driver.get(url)
        sleep(3)
def maximum_check():
    if not "Sukebei" in driver.title:
        num=1#forcefully stop crawling
        return True
Thread(target=animation).start()


driver_path = path.abspath('.\chromedriver.exe')
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=option)
option.add_argument("-headless")#not sure
driver.implicitly_wait(10)
driver.get(url)

j=1
k=str(j)
token=0
x=1#the page you are crawling #remember
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
    if "comments" in driver.find_element_by_xpath(temp).get_attribute("title"):#not sure
        #print("found comment,its j is",end='')
        print(str(j),end="")
        temp="//tr["+k+"]/td[2]/a[2]"
    print(driver.find_element_by_xpath(temp).get_attribute("title"))

while True:
    if token==num:
        print("mission completed")
        break
    if j==76:        
        j=1
        temp=1
        temp1=x
        while temp1>=10:
            temp=temp+1
            temp1=temp1/10
            
        print(temp)
        url=url[:-(temp+3)]
        x=x+1   #flip the page #remember
        url=url+"&p="+str(x)
        driver.get(url)
        badway_check()
        print(url)
        if maximum_check() and num!=-1:        #the number can be edit,if you are more patient,you can change it into 15~30
            print("i can only find "+str(token)+" torrents,there are "+str(num-token)+" left")
            break
    k=str(j)
    if(time_filter()):
        if(category_filter()):
            if magnet_ask=="1":
                temp="//tr["+k+"]/td[3]/a[1]"
            elif magnet_ask=="2":
                temp="//tr["+k+"]/td[3]/a[2]"
            driver.find_element_by_xpath(temp).click()
            print(str(token+1)+". ",end = "")
            comment_check()
            token=token+1
    j=j+1
driver.get("chrome://downloads/")
sleep(7) #wait for the download finish completely,if your internet is fast enough you can just delete this line


