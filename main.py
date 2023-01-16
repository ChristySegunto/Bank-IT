from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import Font

# main deposit
deposit = Tk()
deposit.geometry("1100x628")
deposit.title("Bank IT")
deposit.iconbitmap(r"C:\Users\mando\PycharmProjects\pythonProject1\image\logo.ico")

# deposit background
dep = ImageTk.PhotoImage(file=r"C:\Users\mando\PycharmProjects\pythonProject1\image\bglogin.png")
# Creating canvas for bg and texts
canvas1 = Canvas(deposit, width=1100,
                 height=628)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=dep,
                     anchor="nw")

# logo of bank it
logo = ImageTk.PhotoImage(file=r"C:\Users\mando\PycharmProjects\pythonProject1\image\logo.png")
canvas1.create_image(80, 40, image=logo,
                     anchor="nw")

# deposit font
mainfont = Font(family="Myriad Pro", size=75, weight="bold")
subfont = Font(family="Myriad Pro", size=14)
depositfont = Font(family="Myriad Pro", size=40)

# creatings texts
canvas1.create_text(550, 160, text="Deposit", fill='white', font=mainfont)
canvas1.create_text(550, 240, text="How much do you wish to deposit?", fill='white', font=subfont)
canvas1.create_text(550, 260, text="Enter your desired amount:", fill='white', font=subfont)



deposit_value1 = StringVar()
deposit1_image = Image.open(r"C:\Users\mando\PycharmProjects\pythonProject1\image\PHP.png")
deposit1_resize = deposit1_image.resize((1100, 628))
deposit1 = ImageTk.PhotoImage(deposit1_resize)
canvas1.create_image(550, 300, anchor="nw", image=deposit1)


def entrybox(event):
    deposit.deposit()
entrybox_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\PHP.png')
entrybox_image_resize = entrybox_image.resize((1000, 600))
entrybox_image_final = ImageTk.PhotoImage(entrybox_image_resize)
entrybox_image_layout = canvas1.create_image(50, 37, anchor=NW, image=entrybox_image_final)


# declaring limits for pin 1
def deposit1_limit(*args):
    if len(deposit_value1.get()) > 0:
        deposit_value1.set(deposit_value1.get())
    if not deposit_value1.get().isnumeric():
        messagebox.showerror('Error!', 'You must input a number')
        deposit1_entry.delete(len(deposit1_entry.get()) - 1)


deposit_value1.trace("w", lambda *args: deposit1_limit())

# creating text box for pin1
deposit1_entry = Entry(deposit,
                       font=depositfont,
                       width=6,
                       fg="white",
                       bd=0,
                       bg="#161B81",
                       justify="center",
                       textvariable=deposit_value1)
deposit1_entry.pack()
deposit1 = canvas1.create_window(617, 320, window=deposit1_entry)
deposit1_entry.bind('<BackSpace>', lambda *args: 'break')

# deposit buttons
def button1(event):
    deposit.deposit()
button1_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\onek.png')
button1_image_resize = button1_image.resize((1100,628))
button1_image_final = ImageTk.PhotoImage(button1_image_resize)
button1_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button1_image_final)
canvas1.tag_bind(button1_image_layout, "<Button-1>", button1)

def button2(event):
    deposit.deposit()
button2_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\twok.png')
button2_image_resize = button2_image.resize((1100,628))
button2_image_final = ImageTk.PhotoImage(button2_image_resize)
button2_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button2_image_final)
canvas1.tag_bind(button2_image_layout, "<Button-1>", button2)

def button3(event):
    deposit.deposit()
button3_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\fivek.png')
button3_image_resize = button3_image.resize((1100,628))
button3_image_final = ImageTk.PhotoImage(button3_image_resize)
button3_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button3_image_final)
canvas1.tag_bind(button3_image_layout, "<Button-1>", button3)

def button4(event):
    deposit.deposit()
button4_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\tenk.png')
button4_image_resize = button4_image.resize((1100,628))
button4_image_final = ImageTk.PhotoImage(button4_image_resize)
button4_image_layout = canvas1.create_image(0, 20, anchor=NW, image=button4_image_final)
canvas1.tag_bind(button4_image_layout, "<Button-1>", button4)

# submit button
def submit(event):
    deposit.deposit()
submitbutton_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\Submit.png')
submitbutton_image_resize = submitbutton_image.resize((1100,628))
submitbutton_image_final = ImageTk.PhotoImage(submitbutton_image_resize)
submitbutton_image_layout = canvas1.create_image(-40, 15, anchor=NW, image=submitbutton_image_final)
canvas1.tag_bind(submitbutton_image_layout, "<Button-1>", submit)

# back button
def back(event):
    deposit.deposit()
backbutton_image = Image.open(r'C:\Users\mando\PycharmProjects\pythonProject1\image\Back Button.png')
backbutton_image_resize = backbutton_image.resize((1100,628))
backbutton_image_final = ImageTk.PhotoImage(backbutton_image_resize)
backbutton_image_layout = canvas1.create_image(0, 0, anchor=NW, image=backbutton_image_final)
canvas1.tag_bind(backbutton_image_layout, "<Button-1>", back)

def back(event):
    deposit.destroy()
    # import home

deposit.resizable(False, False)
deposit.mainloop()
