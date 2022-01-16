from email import message
from tkinter import *
from tkinter import messagebox
import requests
import webbrowser

root = Tk()
# Code to add widgets will go here...

GPSWeekStart=StringVar()
GPSWeekEnd=StringVar()

description = Label(root,text="This is a tool for downloading \n CDDIS IGS Precise Orbit Data. \n Check GPS Week here:")
GPSWeekCalendarLabel = Label(root,text="https://www.ngs.noaa.gov/CORS/Gpscal.shtml", fg="blue", cursor="hand2")
GPSWeekStartLabel = Label(root, text="GPS Week Start")
GPSWeekEndLabel = Label(root,text="GPS Week End")
GPSWeekStartEntry = Entry(root,textvariable = GPSWeekStart)
GPSWeekEndEntry = Entry(root,textvariable = GPSWeekEnd)
# Length Calculator
def length_calculator(num):
    if (num < 10):
        return 1
    return 1 + length_calculator(int(num/10))

def openLinkCallBack(event):
    webbrowser.open_new(event.widget.cget("text"))

def downloadCallBack():
    if not GPSWeekStart.get():
        messagebox.showinfo("Error","Please enter GPS Week Start")
    if not GPSWeekEnd.get():
        messagebox.showinfo("Error","Please enter GPS Week End")

    if GPSWeekStart.get() and GPSWeekEnd.get() :
        for y in range(int(GPSWeekStart.get()),int(GPSWeekEnd.get())):

            for x in range(0,7):
                #https://cddis.nasa.gov/archive/gnss/products/1617/igs16170.sp3.Z
                
                url = "https://cddis.nasa.gov/archive/gnss/products/"+ str(y) +"/igs"+ str(y)+ str(x) +".sp3.Z"

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

GPSWeekStartLabel.grid(row=0,column=0)
GPSWeekStartEntry.grid(row=0,column=1)
GPSWeekEndLabel.grid(row=1,column=0)
GPSWeekEndEntry.grid(row=1,column=1)
B.grid(row=2,column=0)
description.grid(row=3)
GPSWeekCalendarLabel.grid(row=4)
GPSWeekCalendarLabel.bind("<Button-1>", openLinkCallBack)
root.mainloop()