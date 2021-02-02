from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
date="2021-"
print("注意，下載完成前請不要任意關閉cmd或chrome")
month=input("現在是幾月(請輸入阿拉伯數字)?")
month=int(month)
if month<10:
    month="0"+str(month)
day=input("今天幾號(請輸入阿拉伯數字)?")
date=date+month+"-"+day
print(date)
num = input("你想下載幾個bt?")
request=input("有限定要哪個category嗎(a)我全都要 (b)porn (c)anime (d)manga (e)pictures (f)同人誌")
ask=input("(a)下載.torrent (b)下載magnet")
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
        print("下載完成，功德圓滿")
        break
    if j==76:
        print("第一頁沒有足夠的torrent")
        print("我只能找到"+str(token)+"個torrent")
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



