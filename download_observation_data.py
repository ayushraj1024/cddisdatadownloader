from email import message
from tkinter import *
from tkinter import messagebox
import requests
import sys

root = Tk()
# Code to add widgets will go here...

year=StringVar()
GPSDayStart=StringVar()
GPSDayEnd=StringVar()
siteID=StringVar()

description = Label(root,text="This is a tool for downloading \n CDDIS Observation Data.")
yearLabel = Label(root, text="Year")
GPSDayStartLabel = Label(root,text = "GPS Day Start")
GPSDayEndLabel = Label(root,text="GPS Day End")
siteIDLabel = Label(root,text="Site ID")
yearEntry = Entry(root,textvariable = year)
GPSDayStartEntry = Entry(root,textvariable = GPSDayStart)
GPSDayEndEntry = Entry(root,textvariable = GPSDayEnd)
siteIDEntry = Entry(root,textvariable = siteID)

# Length Calculator
def length_calculator(num):
    if (num < 10):
        return 1
    return 1 + length_calculator(int(num/10))

def downloadCallBack():
    if not year.get():
        messagebox.showinfo("Error","Please enter Year")
    if not GPSDayStart.get():
        messagebox.showinfo("Error","Please enter GPS Day Start")
    if not GPSDayEnd.get():
        messagebox.showinfo("Error","Please Enter GPS Day End")
    if not siteID.get():
        messagebox.showinfo("Error","Please enter Site ID")

    if year.get() and GPSDayStart.get() and GPSDayEnd.get() and siteID.get():
        for x in range(int(GPSDayStart.get()),int(GPSDayEnd.get())+1):
                        # Reads the URL from the command line argument
                        #https://cddis.nasa.gov/archive/gnss/data/daily/2011/007/11o/iisc0070.11o.Z
            day = "000"
            if(length_calculator(x) == 3):
                day = str(x)
            elif(length_calculator(x) == 2):
                day = "0"+str(x)
            elif(length_calculator(x) == 1):
                day = "00"+str(x)
            
            url = "https://cddis.nasa.gov/archive/gnss/data/daily/"+ year.get() +"/"+ day +"/"+ year.get()[-2:] +"o/"+siteID.get().lower()+day+"0."+year.get()[-2:]+"o.Z"

            # Assigns the local file name to the last part of the URL
            filename = url.split('/')[-1]

            # Makes request of URL, stores response in variable r
            r = requests.get(url)

            # Opens a local file of same name as remote file for writing to
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1000):
                    fd.write(chunk)

            # Closes local file
            fd.close()

B = Button(root, text = "Start Download", command = downloadCallBack)

yearLabel.grid(row=0,column=0)
yearEntry.grid(row=0,column=1)
GPSDayStartLabel.grid(row=1,column=0)
GPSDayStartEntry.grid(row=1,column=1)
GPSDayEndLabel.grid(row=2,column=0)
GPSDayEndEntry.grid(row=2,column=1)
siteIDLabel.grid(row=3,column=0)
siteIDEntry.grid(row=3,column=1)
B.grid(row=4,column=0)
description.grid(row=5)
root.mainloop()