from tkinter import *
from tkinter import messagebox

import tk as tk
from PIL import ImageTk, Image
import tkinter.font as TkFont
import sqlite3

current_balance = 10000

window = Tk()
window.geometry("1100x628")

window.title("Bank IT")

window.iconbitmap(r"image files/logo.ico")

#login window background
loginbg = ImageTk.PhotoImage(file=r"image files/BG-1.jpg")

#Creating canvas for bg and texts
canvas1 = Canvas(window, width = 1100,
                 height = 628)

canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = loginbg,
                     anchor = "nw")

#logo of bank it
logo = ImageTk.PhotoImage(file=r"image files/logo.png")
canvas1.create_image( 80, 40, image = logo,
                     anchor = "nw")


#declaring the properties of font
mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=14)
smallfont = TkFont.Font(family="Myriad Pro", size=8)
#creatings texts
canvas1.create_text( 240, 280, text = "Bank", fill='white', font=mainfont)
canvas1.create_text( 420, 280, text = "IT", fill='#f6008d', font=mainfont)

canvas1.create_text( 270, 340, text = "Automated Teller Machine System", fill='white', font=subfont)


#login acc
USERNAME = StringVar()
PASSWORD = StringVar()

#Username section
canvas1.create_text( 670, 210, text = "USERNAME", fill='white', font=smallfont)

txtbox_img= Image.open(r"image files/textbox.png")
txtbox_resize = txtbox_img.resize((450,140))
txtbox=ImageTk.PhotoImage(txtbox_resize)
canvas1.create_image(570,175,anchor=NW,image=txtbox)

un_entry = Entry(canvas1,
    bd=0,
    bg="#050519",
    fg="#fff",
    highlightthickness=0,
    font=("Myriad pro", 16 * -1),
    insertbackground="#fff",
    textvariable=USERNAME)

un_entry.pack()
username=canvas1.create_window(750,245, window=un_entry)

#Password Section
canvas1.create_text( 670, 300, text = "PASSWORD", fill='white', font=smallfont)
txtbox2=ImageTk.PhotoImage(txtbox_resize)
canvas1.create_image(570,265,anchor=NW,image=txtbox2)
pass_entry = Entry(canvas1,
    bd=0,
    bg="#050519",
    fg="#fff",
    highlightthickness=0,
    font=("Myriad pro", 16 * -1),
    insertbackground="#fff",
    show='*',
    textvariable=PASSWORD)
pass_entry.pack()
password = canvas1.create_window(750,334, window=pass_entry)

#login btn
def checkacc(event):
    if USERNAME.get() == 'Christysegunto' and PASSWORD.get() == '12345':
        window.withdraw()
        menuwindow = Tk()
        menuwindow.geometry("1100x628")
        menuwindow.title("Bank IT")
    else:
        messagebox.showerror('Wrong credentials', 'Wrong credentials! Please try again.')

#declaring image as btn
btn_img = ImageTk.PhotoImage(Image.open(r"image files/loginbtn.png"))
loginbtn = canvas1.create_image(785, 450, image=btn_img)

canvas1.tag_bind(loginbtn, "<Button-1>", checkacc)

window.resizable(False, False)
window.mainloop()