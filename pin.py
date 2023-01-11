from tkinter import *
import tkinter.font as TkFont
from tkinter import messagebox

from PIL import Image, ImageTk

#pin
pin = Tk()
pin.geometry('1100x628')
pin.title("Bank IT")
pin.iconbitmap(r"C:\Users\chris\Bank IT\logo.ico")
pinbg = ImageTk.PhotoImage(file=r"C:\Users\chris\Bank IT\bglogin.png")

canvas1 = Canvas(pin, width = 1100,
                 height = 628)

canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = pinbg,
                     anchor = "nw")

logo = ImageTk.PhotoImage(file=r"C:\Users\chris\Bank IT\logo.png")
canvas1.create_image(80, 40, image = logo,
                     anchor = "nw")

mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=11)
pinfont = TkFont.Font (family = "Myriad Pro", size = 50)

canvas1.create_text( 550, 160, text = "PIN", fill='white', font=mainfont)
canvas1.create_text( 550, 250, text = "Please enter your 4-digit pin code:", fill='white', font=subfont)


def back(event):
    pin.destroy()
    #import home


backPhoto = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\backbtn.png"))
btnBack = canvas1.create_image(1000, 590, image=backPhoto)
canvas1.tag_bind(btnBack, "<Button-1>", back)

pin1Photo = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\pinbtn.png"))
entryPin1 = canvas1.create_image(298, 350, image=pin1Photo)
pin2Photo = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\pinbtn.png"))
entryPin2 = canvas1.create_image(458, 350, image=pin2Photo)
pin3Photo = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\pinbtn.png"))
entryPin3 = canvas1.create_image(618, 350, image=pin3Photo)
pin4Photo = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\pinbtn.png"))
entryPin4 = canvas1.create_image(778, 350, image=pin4Photo)


pinfont = TkFont.Font(family="Myriad Pro", size=50)
pin_value1 = StringVar()
pin_value2 = StringVar()
pin_value3 = StringVar()
pin_value4 = StringVar()
specialchar=['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/',"'","[",']',"|","\\",'.',';','{','}',':','"']

#declaring limits for pin 1
def pin1_limit(*args):
    if len(pin_value1.get()) > 0:
        pin_value1.set(pin_value1.get()[-1])
    if pin_value1.get().isalpha() == True or pin_value1.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        pin1_entry.delete(len(pin1_entry.get()) - 1)

pin_value1.trace("w", lambda *args: pin1_limit(pin_value1))

#declaring limits for pin 2
def pin2_limit(*args):
    if len(pin_value2.get()) > 0:
        pin_value2.set(pin_value2.get()[-1])
    if pin_value2.get().isalpha() == True or pin_value2.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        pin2_entry.delete(len(pin2_entry.get()) - 1)

pin_value2.trace("w", lambda *args: pin2_limit(pin_value2))

#declaring limits for pin 3
def pin3_limit(*args):
    if len(pin_value3.get()) > 0:
        pin_value3.set(pin_value3.get()[-1])
    if pin_value3.get().isalpha() == True or pin_value3.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        pin3_entry.delete(len(pin3_entry.get()) - 1)

pin_value3.trace("w", lambda *args: pin3_limit(pin_value3))


#declaring limits for pin 4
def pin4_limit(*args):
    if len(pin_value4.get()) > 0:
        pin_value4.set(pin_value4.get()[-1])
    if pin_value4.get().isalpha() == True or pin_value4.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        pin4_entry.delete(len(pin4_entry.get()) - 1)


pin_value4.trace("w", lambda *args: pin4_limit(pin_value4))


#creating text box for pin1
pin1_entry = Entry(pin,
                    font=pinfont,
                    width=2,
                    fg="white",
                    bd=0,
                    bg="#161B81",
                    justify="center",
                    textvariable = pin_value1)
pin1_entry.pack()
pin1 = canvas1.create_window(297,350, window=pin1_entry)
pin1_entry.bind('<BackSpace>', lambda *args:'break')

#creating text box for pin2
pin2_entry = Entry(pin,
                    font=pinfont,
                    width=2,
                    fg="white",
                    bd=0,
                    bg="#161B81",
                    justify="center",
                    textvariable = pin_value2)
pin2_entry.pack()
pin2 = canvas1.create_window(455,350, window=pin2_entry)
pin2_entry.bind('<BackSpace>', lambda *args:'break')

#creating text box for pin3
pin3_entry = Entry(pin,
                    font=pinfont,
                    width=2,
                    fg="white",
                    bd=0,
                    bg="#161B81",
                    justify="center",
                    textvariable = pin_value3)
pin3_entry.pack()
pin3 = canvas1.create_window(615,350, window=pin3_entry)
pin3_entry.bind('<BackSpace>', lambda *args:'break')

#creating text box for pin4
pin4_entry = Entry(pin,
                    font=pinfont,
                    width=2,
                    fg="white",
                    bd=0,
                    bg="#161B81",
                    justify="center",
                    textvariable = pin_value4)
pin4_entry.pack()
pin4 = canvas1.create_window(780,350, window=pin4_entry)
pin4_entry.bind('<BackSpace>', lambda *args:'break')

def checkpin(event):
    if pin_value1.get() == '5' and pin_value2.get() == '2' and pin_value3.get() == '4' and pin_value4.get() == '1':
        pin.withdraw()
        homewindow = Tk()
        homewindow.geometry("1100x628")

        homewindow.title("Bank IT")

    else:
        messagebox.showerror('Error', 'Wrong pin! Please try again.')

submitbtn_img = ImageTk.PhotoImage(Image.open(r"C:\Users\chris\Bank IT\submitbtn.png"))
submitbtn = canvas1.create_image(535, 490, image=submitbtn_img)


canvas1.tag_bind(submitbtn, "<Button-1>", checkpin)

timesclicked = 0

def clicked(event):
    global timesclicked

    timesclicked = timesclicked + 1
    if timesclicked <= 4 and timesclicked > 0:
        if timesclicked == 1:
            pin4_entry.focus_set()
            pin4_entry.delete(len(pin4_entry.get()) - 1)

        elif timesclicked == 2:
            pin3_entry.focus_set()
            pin3_entry.delete(len(pin3_entry.get()) - 1)

        elif timesclicked == 3:
            pin2_entry.focus_set()
            pin2_entry.delete(len(pin2_entry.get()) - 1)

        elif timesclicked == 4:
            pin1_entry.focus_set()
            pin1_entry.delete(len(pin1_entry.get()) - 1)


    if timesclicked >= 5:
        timesclicked = 0

backspace_img = Image.open(r"C:\Users\chris\Bank IT\Backspace.png")
backspace_resize = backspace_img.resize((50,50))
backspace = ImageTk.PhotoImage(backspace_resize)
backspacebtn = canvas1.create_image(920, 360, image=backspace)

canvas1.tag_bind(backspacebtn, "<Button-1>", clicked)







pin.resizable(False, False)
pin.mainloop()
