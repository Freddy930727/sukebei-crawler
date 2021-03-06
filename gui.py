import tkinter as tk

window=tk.Tk()
window.title("sukebei_crawler")
window.geometry("960x540")
#window.attributes('-fullscreen', True)  
window.configure(background='white')
bulletin_text=tk.Text(window)

def submit_button_fc():
    """
    bulletin_text.insert("end",keyword_entry.get()+" ")
    bulletin_text.insert("end",month_entry.get()+" ")
    bulletin_text.insert("end",day_entry.get()+" ")
    bulletin_text.insert("end",torrents_entry.get()+" ")
    bulletin_text.insert("end",str(category_var.get())+" ")
    """
    if((len(month_entry.get())==0)or(int(month_entry.get())<13 and int(month_entry.get())<0)):
        if(day_entry.get()<32 and day_entry.get()>0):
            if(int(torrents_entry.get())==-1 or int(torrents_entry.get())>0):
                if(len(keyword_entry.get())==0):
                    temp=0
                else:
                    temp=keyword_entry.get()
                if(len(month_entry)==0):
                    temp1=False
                    temp2=1
                    temp3=1
                else:
                    temp1=True
                    temp2=int(month_entry.get())
                    temp3=int(day_entry.get())
                
                crwaling(temp,temp1,temp2,temp3,str(category_var.get()),torrent_or_magnet)
                print("all finished")
                window.quit()
                sleep(10)
               #crawling(keyword,asktime,month,day,num,category,torrent_or_magnet)
            else:
                print()#message box"please input a number which is greater than 0 or just input -1"
        print()
                #message box"please input a number between 1~12 in the day label"
    else:
        print()
            #message box"please input a number between 1~12 in the month label"
        
        
    
torrent_or_magnet="1"
def torrent_or_magnet_fc():
    torrent_or_magnet="2"

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
torrent_or_magnet_checkbutton=tk.Button(window,text="torrent_or_magnet",command=torrent_or_magnet_fc)#CheckButton
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
torrent_or_magnet_checkbutton.pack()
torrents_label.pack()
torrents_entry.pack()
submit_button.pack()
bulletin_text.pack()

window.mainloop()
