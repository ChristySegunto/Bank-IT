import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font


deposit = Tk()
deposit.geometry("1100x628")

deposit.title("Bank IT")

deposit.iconbitmap(r"image files\logo.ico")

# login window background
lastpage = ImageTk.PhotoImage(file=r"image files\BG-8.jpg")

# Creating canvas for bg and texts
canvas1 = Canvas(deposit, width=1100,
                 height=628)

canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=lastpage,
                     anchor="nw")


# declaring the properties of font
mainfont = Font(family="Myriad Pro", size=50, weight="bold")
subfont = Font(family="Myriad Pro", size=14, weight="bold")


# creatings texts
canvas1.create_text(350, 200, text="Your transaction", fill='white', font=mainfont)
canvas1.create_text(300, 270, text="is successful!", fill='white', font=mainfont)
canvas1.create_text(200, 320, text="Thank you for using Bank IT", fill='white', font=subfont)

canvas1.create_text(900, 200, text="+63933333333", fill='white', font=subfont)
canvas1.create_text(925, 240, text="Bank-IT@bsit2-1.com", fill='white', font=subfont)
canvas1.create_text(920, 280, text="Intramuros, Manila", fill='white', font=subfont)

canvas1.create_text(228, 520, text="Contact info | Bank IT", fill='white', font=subfont)
canvas1.create_text(300, 540, text="General Luna corner Muralla Streets,", fill='white', font=subfont)
canvas1.create_text(290, 560, text="Intramuros,Manila,Philippines 1002", fill='white', font=subfont)


dep = ImageTk.PhotoImage(file=r"image files\ICONS.png")
canvas1.create_image(500, 300, image=dep,
                     anchor="nw")
deposit1_img = Image.open(r"image files\ICONS.png")
canvas1.create_image(500, 300, image=dep,
                     anchor="nw")

deposit.resizable(False, False)
deposit.mainloop()
