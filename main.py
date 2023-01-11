from tkinter import *
from tkinter import messagebox

import tk as tk
from PIL import ImageTk, Image
import tkinter.font as TkFont
import sqlite3

current_balance = 10000

main = Tk()
main.geometry("1100x628")

main.title("Bank IT")

main.iconbitmap(r"image files/logo.ico")

#login window background
mainbg = ImageTk.PhotoImage(file=r"image files/BG-1.jpg")

#Creating canvas for bg and texts
canvas1 = Canvas(main, width = 1100,
                 height = 628)

canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = mainbg,
                     anchor = "nw")

#declaring the properties of font
mainfont = TkFont.Font(family="Myriad Pro", size=100, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=14)
smallfont = TkFont.Font(family="Myriad Pro", size=8)
#creatings texts
canvas1.create_text( 490, 280, text = "Bank", fill='white', font=mainfont)
canvas1.create_text( 715, 280, text = "IT", fill='#f6008d', font=mainfont)

canvas1.create_text( 550, 360, text = "Automated Teller Machine System", fill='white', font=subfont)

def start(event):
    main.destroy()

startbtn_img = ImageTk.PhotoImage(Image.open(r"image files/startbtn.png"))
startbtn = canvas1.create_image(550, 430, image=startbtn_img)
canvas1.tag_bind(startbtn, "<Button-1>", start)

main.resizable(False, False)
main.mainloop()