from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as TkFont
from tkinter import messagebox

# main window
balance = Tk()
balance.geometry("1100x628")
balance.title("Bank IT")
balance.iconbitmap(r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\logo.ico')

# window background/canvas
balance_background = ImageTk.PhotoImage(file=r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\backgroundtwo.png')
canvas1 = Canvas(balance, width=1100, height=628)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = balance_background, anchor = "nw")

# window logo
bankIT_logo = ImageTk.PhotoImage(file=r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\logo.png')
canvas1.create_image(80, 40, image = bankIT_logo, anchor="nw")

# window fonts
mainfont = TkFont.Font(family="Myriad Pro", size=65, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=11)
phptextbox_font = TkFont.Font(family="Myriad Pro", size=24, weight="bold")

# window design/layout
canvas1.create_text( 550, 160, text = "Balance", fill='white', font=mainfont)
canvas1.create_text( 550, 250, text = "Account Balance (Checking)", fill='#F6008d', font=subfont)
canvas1.create_text( 550, 400, text = "Account Balance (Savings)", fill='#F6008d', font=subfont)

phptextbox1_string1 = StringVar()
phptextbox2_string2 = StringVar()
specialchar=['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/',"'","[",']',"|","\\",'.',';','{','}',':','"']


# limits for php textbox1
def phptextbox1_limit(*args):
    if len(phptextbox1_string1.get()) > 0:
        phptextbox1_string1.set(phptextbox1_string1.get()[7])
    if phptextbox1_string1.get().isalpha() == True or phptextbox1_string1.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number.')
        phptextbox1_string1.delete(len(phptextbox1_string1.get()) - 1)
phptextbox1_string1.trace("w", lambda *args: phptextbox1_limit(phptextbox1_string1))

# limits for php textbox2
def phptextbox2_limit(*args):
    if len(phptextbox2_string2.get()) > 0:
        phptextbox2_string2.set(phptextbox2_string2.get()[7])
    if phptextbox2_string2.get().isalpha() == True or phptextbox2_string2.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number.')
        phptextbox2_string2.delete(len(phptextbox1_string1.get()) - 1)
phptextbox2_string2.trace("w", lambda *args: phptextbox2_limit(phptextbox2_string2))


# php textbox image1
phptextbox1 = Image.open(r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\phptextboxone.png')
phptextbox1_resize = phptextbox1.resize((1100,628))
phptextbox1_final = ImageTk.PhotoImage(phptextbox1_resize)
canvas1.create_image(0, 30, anchor=NW, image=phptextbox1_final)

# php actual textbox1
phptextbox1_entry = Entry(balance, font=phptextbox_font, width=8, fg="white", bd=0, bg="#161B81", justify="center", textvariable = phptextbox1_string1)
phptextbox1_entry.pack()
phptextbox1_entry_layout = canvas1.create_window(605, 326, window=phptextbox1_entry)

# php textbox image2
phptextbox2 = Image.open(r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\phptextboxone.png')
phptextbox2_resize = phptextbox2.resize((1100,628))
phptextbox2_final = ImageTk.PhotoImage(phptextbox2_resize)
canvas1.create_image(0, 180, anchor=NW, image=phptextbox2_final)

# php actual textbox2
phptextbox2_entry = Entry(balance, font=phptextbox_font, width=8, fg="white", bd=0, bg="#161B81", justify="center", textvariable = phptextbox2_string2)
phptextbox2_entry.pack()
phptextbox2_entry_layout = canvas1.create_window(605, 476, window=phptextbox2_entry)


# back button
def backbutton(event):
    balance.withdraw()
backbutton_image = Image.open(r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\bluebackbutton.png')
backbutton_image_resize = backbutton_image.resize((1100,628))
backbutton_image_final = ImageTk.PhotoImage(backbutton_image_resize)
backbutton_image_layout = canvas1.create_image(0, 0, anchor=NW, image=backbutton_image_final)
canvas1.tag_bind(backbutton_image_layout, "<Button-1>", backbutton)


# window end
balance.resizable(False, False)
balance.mainloop()