# Import module  
from tkinter import *
  
# Create object  
root = Tk() 
  
# Adjust size  
root.geometry("1920x1080") 
  
# Add image file 
#bg = PhotoImage(file = "t6q9w-e403f.gif") 

# Create Canvas 
canvas1 = Canvas( root)#, width = 1920/2, height = 1080/2) 
  
canvas1.pack(fill = "both", expand = True) 
  
canvas1.create_image( 0, 0, image = PhotoImage(file = "t6q9w-e403f.gif") ,   anchor = "nw") 
root.mainloop() 
