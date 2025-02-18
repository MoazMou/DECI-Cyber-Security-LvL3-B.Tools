import os
import schedule
import subprocess
import pandas as pd
import tkinter as tk
from tkinter import *
from email import encoders
from tkinter import messagebox
import win32com.client as win32
from tkinter.filedialog import *

root = Tk()
root.title("Mail Supporter v2.1")
root.geometry('415x300')
root.iconbitmap(r'send.ico')

#DATAS
email_list = pd.read_excel("List.xlsx")
emails = email_list['To']
subjects = email_list['Subject']
messages = email_list['Message']
attachments = email_list['Attachment']  
times = email_list['Time']

#FRAMES
background1 = PhotoImage(file="background.png")
label_background = Label(root, image=background1, width=600,  height=230).pack(side=TOP)

labelb = tk.Label(root, width=80, height=4, border=3, relief=tk.GROOVE,bg="white")
labelb.pack(side=tk.TOP)

#FUNCTIONS
def jop2():
    pass

def jop():
    try:
        for i in range(len(emails)):
            emails1 = emails[i]
            subject = subjects[i]
            message = messages[i]
            attachment1 = attachments[i]
        
            message1 = message

            outlook = win32.Dispatch('outlook.application')
            mail = outlook.CreateItem(0)
            mail.To = emails1
            mail.Subject = subject
            mail.Body = message1

            mail.Attachments.Add(os.path.join(os.getcwd(), attachment1))
            mail.Send()
            
        messagebox.showinfo(title="Mail Supporter", message="Your email has sent!")
        root.destroy()

    except:
        messagebox.showinfo(title="Mail Supporter", message="Something went wrong. Check the list file again!")
        root.destroy()

def tap():
    for i in range(len(emails)):
        emails1 = emails[i]
        time1 = times[i]

    schedule.every().day.at(str(time1)).do(jop)

    while True:
        schedule.run_pending()

def tap2():
    root = Tk()
    root.title("Help")
    root.iconbitmap(r'send.ico')
    root.geometry('460x350')

    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill= Y)

    text1 = Text(root, width=260, height=50, bd=5, font=("arial",11,"bold"),yscrollcommand= scroll.set)

    scroll.config(command=text1.yview)
    text1.pack(expand=1, fill=BOTH)

    text1.insert(INSERT, """
@This application has created by (Moaaz Mourad Mohamed)
------------------------------------------------------

@Weclome to Mail Supporter:
---------------------------

   Mail Supporter is here to help you automate your mail life. 
This is version 2.1 of the application. Our Application has 
an Exel list that you have to enter your data (Emails, 
Attachments, Subjects, and Time). Save the file and then run 
Mail Supporter enter the time that you want to send 
your emails and click (Send). You will find our 
application sent to all your emails with attachments 
at one time and he will tell you to stop when he finishes. 

@How to use Mail Supporter?
---------------------------
To use Mail Supporter without any problems follow 
these steps:
------------

1- Open the MS Excel list and enter your data

2- Save the list and run Mail Supporter

3- Enter the timer in the list file like this
from (24:00:00) to (00:00:00) without typing AM or PM

4- Press the (Send) button
                 
@Note:
--------
Mail Supporter sends emails by Outlook, so you 
have to make sure that you're logged in.
    """)
    root.mainloop()

def tap3():
    subprocess.run("start List.xlsx",shell=True)

sendbtn = Button(root, text="Send", width=11, height=1, bd=3, font=("arila",12,"bold"), command=tap).place(x=10,y=250)       
listbtn = Button(root, text="Edit list", width=12, height=1, bd=3, font=("arila",12,"bold"), command=tap3).place(x=140,y=250)       
helpbtn = Button(root, text="Help", width=11, height=1, bd=3, font=("arila",12,"bold"), command=tap2).place(x=280,y=250)
root.mainloop()