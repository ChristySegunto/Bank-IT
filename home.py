from tkinter import *
import tkinter.font as TkFont
from PIL import Image, ImageTk
from tkinter import messagebox

#home
home = Tk()
home.geometry('1100x628')
home.title("Bank IT")
home.iconbitmap(r"image files\logo.ico")
homebg = ImageTk.PhotoImage(file = r"image files\BG-3.png")

canvas1 = Canvas(home, width = 1100,
                 height = 628)

canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = homebg,
                     anchor = "nw")

logo = ImageTk.PhotoImage(file=r"image files\logo.png")
canvas1.create_image(80, 40, image = logo,
                     anchor = "nw")

mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=11)
canvas1.create_text( 550, 180, text = "Hello,", fill='white', font=mainfont)
canvas1.create_text( 550, 270, text = "How can we help you today?", fill='white', font=subfont)

def withdraw(event):
    home.destroy()
    import pin

withdrawPhoto = ImageTk.PhotoImage(Image.open(r"image files\withdrawbtn.png"))
btnWithdraw = canvas1.create_image(550, 360, image=withdrawPhoto)
canvas1.tag_bind(btnWithdraw, "<Button-1>", withdraw)

def balinq(event):
    home.destroy()
    import pin
balinqPhoto = ImageTk.PhotoImage(Image.open(r"image files\binquirybtn.png"))
btnBInquiry = canvas1.create_image(550, 420, image=balinqPhoto)
canvas1.tag_bind(btnBInquiry, "<Button-1>", balinq)

def deposit(event):
    home.destroy()
    import pin
depositPhoto = ImageTk.PhotoImage(Image.open(r"image files\depositbtn.png"))
btnDeposit = canvas1.create_image(550, 480, image=depositPhoto)
canvas1.tag_bind(btnDeposit, "<Button-1>", deposit)

home.resizable(False, False)
home.mainloop()

