from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
date="2021-"
month=input("which month is it?")
month=int(month)
if month<10:
    month="0"+str(month)
day=input("which day is it?")
date=date+month+"-"+day
print(date)
num = input("how many torrents do you require?")
request=input("(a)all categories (b)real life videos (c)anime (d)manga (e)pictures (f)doujinshi")
ask=input("(a)download by .torrent (b)download by magnet")
url="https://sukebei.nyaa.si/?s=seeders&o=desc"
#https://sukebei.nyaa.si/?s=seeders&o=desc
num=int(num)
timee="d"

driver_path = "C:\\webdriver\\chromedriver.exe"
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=option)
driver.implicitly_wait(10)
driver.get(url)

if request=="a":
    request="all categories"
elif request=="b":
    request="Real Life - Videos"
elif request=="c":
    request="Art - Anime"
elif request=="d":
    request="Art - Manga"
elif request=="e":
    request="Art - Pictures"
elif request=="f":
    request="Art - Doujinshi"
j=1
token=0

while True:
    if token==num:
        print("mission completed")
        break
    if j==76:
        print("there arent adequate torrents on the day that you designate")
        print("i can only find "+str(token)+"torrents")
        break
    k=str(j)
    temp="//tr["+k+"]/td[5]"
    temp=driver.find_element_by_xpath(temp).text
    timee=temp[:-6]
    print(timee)
    if str(date) == str(timee):
        print("found!")
        temp="//tr["+k+"]/td[1]/a"
        cate=driver.find_element_by_xpath(temp).get_attribute("title")
        if request==cate:
            if ask=="a":
                temp="//tr["+k+"]/td[3]/a[1]"
            elif ask=="b":
                temp="//tr["+k+"]/td[3]/a[2]"
            driver.find_element_by_xpath(temp).click()
            token=token+1
        elif request=="all categories":
            if ask=="a":
                temp="//tr["+k+"]/td[3]/a[1]"
            elif ask=="b":
                temp="//tr["+k+"]/td[3]/a[2]"
            driver.find_element_by_xpath(temp).click()
            token=token+1
    j=j+1


time.sleep(10)



