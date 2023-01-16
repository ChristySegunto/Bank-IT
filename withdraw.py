from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as TkFont
from tkinter import messagebox

# main window
withdraw = Tk()
withdraw.geometry("1100x628")
withdraw.title("Bank IT")
withdraw.iconbitmap(r'image files\logo.ico')

# window background
withdraw_background = ImageTk.PhotoImage(file=r'image files\backgroundtwo.png')
canvas1 = Canvas(withdraw, width=1100, height=628)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = withdraw_background, anchor = "nw")

# window logo
bankIT_logo = ImageTk.PhotoImage(file=r'image files\logo.png')
canvas1.create_image(80, 40, image = bankIT_logo, anchor="nw")

# window fonts
mainfont = TkFont.Font(family="Myriad Pro", size=65, weight="bold")
subfont = TkFont.   Font(family="Myriad Pro", size=11)
textboxfont = TkFont.Font(family="Myriad Pro", size=28)

# window design/layout
canvas1.create_text( 550, 160, text = "Withdraw", fill='white', font=mainfont)
canvas1.create_text( 550, 240, text = "How much do you wish to withdraw?", fill='white', font=subfont)
canvas1.create_text( 550, 260, text = "Enter your desired amount:", fill='white', font=subfont)

# window textbox
bluetextbox = Image.open(r'image files\bluetextbox.png')
bluetextbox_resize = bluetextbox.resize((370, 60))
bluetextbox_final = ImageTk.PhotoImage(bluetextbox_resize)
canvas1.create_image(370, 280, anchor=NW, image=bluetextbox_final)

textbox_string = StringVar()
bluetextbox_entry = Entry(withdraw, font=textboxfont, width=14, fg="white", bd=0, bg="#161B81", justify="center", textvariable = textbox_string)
bluetextbox_entry.pack()
bluetextbox_entry_layout = canvas1.create_window(550, 310, window=bluetextbox_entry)


# money buttons
def button1(event):
    print("1000")
button1_image = Image.open(r'image files\onethousand.png')
button1_image_resize = button1_image.resize((1100,628))
button1_image_final = ImageTk.PhotoImage(button1_image_resize)
button1_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button1_image_final)
canvas1.tag_bind(button1_image_layout, "<Button-1>", button1)

def button2(event):
    print("2000")
button2_image = Image.open(r'C:\Users\bossg\OneDrive\Desktop\My Programs\python_programs\BANK IT\Images\twothousand.png')
button2_image_resize = button2_image.resize((1100,628))
button2_image_final = ImageTk.PhotoImage(button2_image_resize)
button2_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button2_image_final)
canvas1.tag_bind(button2_image_layout, "<Button-1>", button2)

def button3(event):
    print("5000")
button3_image = Image.open(r'image files\fivethousand.png')
button3_image_resize = button3_image.resize((1100,628))
button3_image_final = ImageTk.PhotoImage(button3_image_resize)
button3_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button3_image_final)
canvas1.tag_bind(button3_image_layout, "<Button-1>", button3)

def button4(event):
    print("10000")
button4_image = Image.open(r'image files\tenthousand.png')
button4_image_resize = button4_image.resize((1100,628))
button4_image_final = ImageTk.PhotoImage(button4_image_resize)
button4_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button4_image_final)
canvas1.tag_bind(button4_image_layout, "<Button-1>", button4)

# submit button
def button5(event):
    print("submit")
submitbutton_image = Image.open(r'image files\submitbutton.png')
submitbutton_image_resize = submitbutton_image.resize((1100,628))
submitbutton_image_final = ImageTk.PhotoImage(submitbutton_image_resize)
submitbutton_image_layout = canvas1.create_image(-40, 15, anchor=NW, image=submitbutton_image_final)
canvas1.tag_bind(submitbutton_image_layout, "<Button-1>", button5)

# back button
def backbutton(event):
    print("back")
backbutton_image = Image.open(r'image files\bluebackbutton.png')
backbutton_image_resize = backbutton_image.resize((1100,628))
backbutton_image_final = ImageTk.PhotoImage(backbutton_image_resize)
backbutton_image_layout = canvas1.create_image(0, 0, anchor=NW, image=backbutton_image_final)
canvas1.tag_bind(backbutton_image_layout, "<Button-1>", backbutton)


# window end
withdraw.resizable(False, False)
withdraw.mainloop()
