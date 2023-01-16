from tkinter import *
from tkinter import messagebox

import tk as tk
from PIL import ImageTk, Image
import tkinter.font as TkFont
import sqlite3

lastpage = Tk()
lastpage.geometry("1100x628")

lastpage.title("Bank IT")

lastpage.iconbitmap(r"image files\logo.ico")

# login window background
lastpagebg = ImageTk.PhotoImage(file=r"image files\BG-8.png")

# Creating canvas for bg and texts
canvas1 = Canvas(lastpage, width=1100,
                 height=628)

canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=lastpagebg,
                     anchor="nw")

# declaring the properties of font
mainfont = TkFont.Font(family="Myriad Pro", size=50, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=12)
contactfont = TkFont.Font(family="Myriad Pro", size=13)
footerfont1 = TkFont.Font(family="Myriad Pro", size=12, weight = "bold")
footerfont2 = TkFont.Font(family="Myriad Pro", size=12)

# creatings texts
canvas1.create_text(350, 200, text="Your transaction", fill='white', font=mainfont)
canvas1.create_text(300, 270, text="is successful!", fill='white', font=mainfont)
canvas1.create_text(210, 340, text="Thank you for using Bank IT.", fill='white', font=subfont)

canvas1.create_text(899, 200, text="+63933333333", fill='white', font=contactfont)
canvas1.create_text(920, 260, text="Bank-IT@bsit2-1.com", fill='white', font=contactfont)
canvas1.create_text(911, 320, text="Intramuros, Manila", fill='white', font=contactfont)

canvas1.create_text(176, 530, text="Contact info | Bank IT", fill='white', font=footerfont1)
canvas1.create_text(220, 565, text="General Luna corner Muralla Streets,", fill='white', font=footerfont2)
canvas1.create_text(218, 585, text="Intramuros,Manila,Philippines 1002", fill='white', font=footerfont2)


def contactus(event):
    lastpage.destroy()
    withdraw = Toplevel()
    withdraw.geometry("1100x628")
    withdraw.title ("Bank IT")
    withdraw.iconbitmap (r"image files/logo.ico")
    withdrawbg = ImageTk.PhotoImage(file=r"image files\BG-8.png")

contact_img = Image.open(r"image files/CONTACT-US.png")
contact_resize = contact_img.resize((130,45))
contact = ImageTk.PhotoImage(contact_resize)
contactbtn = canvas1.create_image(170, 420, image=contact)
canvas1.tag_bind(contactbtn, "<Button-1>", contactus)

num_img = Image.open(r"image files/numicon.png")
num_resize = num_img.resize((50,39))
numPhoto = ImageTk.PhotoImage(num_resize)
numIcon = canvas1.create_image(814, 200, image=numPhoto)

email_img = Image.open(r"image files/emailicon.png")
email_resize = email_img.resize((50,39))
emailPhoto = ImageTk.PhotoImage(email_resize)
emailIcon = canvas1.create_image(814, 260, image=emailPhoto)

location_img = Image.open(r"image files/locationicon.png")
location_resize = location_img.resize((50,39))
locationPhoto = ImageTk.PhotoImage(location_resize)
locationIcon = canvas1.create_image(814, 320, image=locationPhoto)

lastpage.resizable(False, False)
lastpage.mainloop()