from selenium import webdriver
from time import sleep
from os.path import abspath
from os import mkdir
from os import listdir
from os import startfile
from os import getcwd
from datetime import date as Date
from datetime import datetime 
from threading import Thread
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
#import chromedriver_autoinstaller
#chromedriver_autoinstaller.install()#not functioning



def crawling(keyword,asktime,month,day,num,category,torrent_or_magnet):
    if(asktime==True):
        date=str(Date.today().year)+"-"
        if month<10:
            month="0"+str(month)
        month=str(month)
    
        if day<10:
            day="0"+str(day)
        day=str(day)
        date=date+month+"-"+day

    if(torrent_or_magnet=="1"):
        """
        download_path=str(path.join(Path.home(), "Downloads"))
        temp=1
        download_path=download_path+"\downloads_of_sukebei-crawler"+" ("+str(temp)+")"

        while(path.exists(download_path)):
            temp2=str(temp)
            temp1=1
            while(temp>=10):
                temp1=temp1+1
                temp=temp/10
            temp=int(temp2)+1
            download_path=download_path[:-(temp1+1)]
            download_path=download_path+str(temp)+")"
        print("download path="+download_path)
        mkdir(download_path)
        """#if you want to download in the "downloads" file ,but it's not recommended
        download_path=abspath(getcwd())+"\\downloads\\"+datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        mkdir(download_path)
        bulletin_text.insert("end","download_path:"+download_path+"\n")
    else:
        download_path="none"

    url="https://sukebei.nyaa.si/"
    if keyword!=0:
        url=url+"?f=0&c=0_0&q="+keyword+"&s=seeders&o=desc"
    else:
        url=url+"?s=seeders&o=desc"
    url=url+"&p=1"
    #timee="d"#not sure if it can be deleted
    temp1=0
    thread_stop=False

    def animation():
        bulletin_text.insert("end","crawling...,please wait.")
        idx=0
        while not thread_stop:
            bulletin_text.insert("end","...")
            idx += 1
            sleep(0.1)
    def badway_check():
        if(url==driver.title):
            page=7
            num=1
            return
        while not "Sukebei" in driver.title:
            driver.implicitly_wait(20)
            driver.get(url)
            sleep(3)
    def maximum_check():
        if not "Sukebei" in driver.title:
            num=1#force stop crawling
            return True

    Thread(target=animation).start()

    #sleep(20)#remember
    option = webdriver.ChromeOptions()
    #option.headless = True#remember
    option.add_argument('blink-settings=imagesEnabled=false')
    if(download_path!="none"):
        prefs = {"download.default_directory" : download_path}
        option.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(abspath('.\chromedriver.exe'), options=option)
    driver.implicitly_wait(20)
    driver.get(url)

    tr=1
    k=str(tr)
    token=0
    page=1#the first page
    badway_check()
    thread_stop=True


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
            #print("found comment,its tr is",end='')
            #print(str(tr),end="")#not sure
            temp="//tr["+k+"]/td[2]/a[2]"
        return temp
    def current_page_check():
        while(url!=driver.current_url):
            sleep(2)
            driver.back#not sure

    while True:
        if token==num:
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
                if torrent_or_magnet=="1":
                    temp="//tr["+k+"]/td[3]/a[1]"
                    driver.find_element_by_xpath(temp).click()
                    current_page_check()
                elif torrent_or_magnet=="2":
                    temp="//tr["+k+"]/td[3]/a[2]"
                    startfile(driver.find_element_by_xpath(temp).get_attribute("href"))       
                print(str(token+1)+". ",end = "")
                #comment_check()
                #temp="//tr["+k+"]/td[2]/a"
                print(driver.find_element_by_xpath(comment_check()).get_attribute("title"))#don't modify the order of previous three line(including this one)
                token=token+1
        tr=tr+1
    print("crawling finished")
    if(torrent_or_magnet=='1'):
        thread_stop=False
        Thread(target=animation).start()#not sure
        for i in listdir(download_path):
            if(i.endswith('.crdownload')):
                sleep(4)
        thread_stop=True
        print("download finished!")
        startfile(abspath(download_path))
    print("mission complete")
    #sleep(7) #wait for the download finish completely,if your internet is fast enough you can just delete this line

window=tk.Tk()
window.title("sukebei_crawler")
window.geometry("960x540")
#window.attributes('-fullscreen', True)  
window.configure(background='white')
bulletin_text=scrolledtext.ScrolledText(window)

def submit_button_fc():
    """
    bulletin_text.insert("end",keyword_entry.get()+" ")
    bulletin_text.insert("end",month_entry.get()+" ")
    bulletin_text.insert("end",day_entry.get()+" ")
    bulletin_text.insert("end",torrents_entry.get()+" ")
    bulletin_text.insert("end",str(category_var.get())+" ")
    bulletin_text.insert("end",str(torrent_or_magnet.get())+" ")
    """
    if((len(month_entry.get())==0)or(int(month_entry.get())<13 and int(month_entry.get())>0)):
        if(int(day_entry.get())<32 and int(day_entry.get())>0):
            if(int(torrents_entry.get())==-1 or int(torrents_entry.get())>0):
                submit_button["state"]="disabled"
                if(len(keyword_entry.get())==0):
                    temp=0
                else:
                    temp=keyword_entry.get()
                if(len(month_entry.get())==0):
                    temp1=False
                    temp2=1
                    temp3=1
                else:
                    temp1=True
                    temp2=int(month_entry.get())
                    temp3=int(day_entry.get())
                crawling(temp,temp1,temp2,temp3,torrents_entry.get(),str(category_var.get()),str(torrent_or_magnet.get()))
                bulletin_text.insert("end","all finished"+" ")
                window.quit()
                sleep(10)
               #crawling(keyword,asktime,month,day,num,category,torrent_or_magnet)
            else:
                messagebox.showwarning("warning","please input a number which is greater than 0 or just input -1 in the torrents number label")
        messagebox.showwarning("warning","please input a number between 1~12 in the day label")
    else:
        messagebox.showwarning("warning","please input a number between 1~12 in the month label")
        
        
    
torrent_or_magnet=tk.IntVar()


category_var=tk.IntVar()

keyword_label=tk.Label(window,text="keyword filter,(optional,if you leave it blank ,this program will crawl the most trending torrent)",bg="white",width=70,height=1)
keyword_entry=tk.Entry(window)
time_label=tk.Label(window,text="time filter",bg="white",width=15,height=1)
month_entry=tk.Entry(window)
day_entry=tk.Entry(window)
torrents_label=tk.Label(window,text="quantity of torrents",bg="white",width=15,height=1)
torrents_entry=tk.Entry(window)
category_label=tk.Label(window,text="category:",bg="white",width=15,height=1)
category_radiobutton1=tk.Radiobutton(window,text="all categories",variable=category_var,value=1)
category_radiobutton2=tk.Radiobutton(window,text="real life videos",variable=category_var,value=2)
category_radiobutton3=tk.Radiobutton(window,text="anime",variable=category_var,value=3)
category_radiobutton4=tk.Radiobutton(window,text="manga",variable=category_var,value=4)
category_radiobutton5=tk.Radiobutton(window,text="pictures",variable=category_var,value=5)
category_radiobutton6=tk.Radiobutton(window,text="doujinshi",variable=category_var,value=6)

torrent_or_magnet_label=tk.Label(window,text="which way are you going to download torrent",bg="white",width=40,height=1)
torrent_or_magnet_radiobutton1=tk.Radiobutton(window,text="download torrent",variable=torrent_or_magnet,value=1)#CheckButton
torrent_or_magnet_radiobutton2=tk.Radiobutton(window,text="magnet link",variable=torrent_or_magnet,value=2)#CheckButton
submit_button=tk.Button(window,text="submit button",command=submit_button_fc)
#pack()
keyword_label.pack()
keyword_entry.pack()
time_label.pack()
month_entry.pack()
day_entry.pack()
torrents_label.pack()
torrents_entry.pack()
category_label.pack()
category_radiobutton1.pack()
category_radiobutton2.pack()
category_radiobutton3.pack()
category_radiobutton4.pack()
category_radiobutton5.pack()
category_radiobutton6.pack()
torrent_or_magnet_label.pack()
torrent_or_magnet_radiobutton1.pack()
torrent_or_magnet_radiobutton2.pack()
torrents_label.pack()
torrents_entry.pack()
submit_button.pack()
bulletin_text.pack()

window.mainloop()

