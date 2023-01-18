from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import Font

# main deposit
deposit = Tk()
deposit.geometry("1100x628")
deposit.title("Bank IT")
deposit.iconbitmap(r"image files\logo.ico")

# deposit background
depositbg = ImageTk.PhotoImage(file=r"image files\BG-1.png")
# Creating canvas for bg and texts
depositcanvas = Canvas(deposit, width=1100,
                 height=628)
depositcanvas.pack(fill="both", expand=True)
depositcanvas.create_image(0, 0, image=depositbg,
                     anchor="nw")

# logo of bank it
logo = ImageTk.PhotoImage(file=r"image files\logo.png")
depositcanvas.create_image(80, 40, image=logo,
                     anchor="nw")

# deposit font
deposit_mainfont = Font(family="Myriad Pro", size=75, weight="bold")
deposit_subfont = Font(family="Myriad Pro", size=11)
depositfont = Font(family="Myriad Pro", size=30)

depositcanvas.create_text(550, 160, text="Deposit", fill='white', font=deposit_mainfont)
depositcanvas.create_text(550, 240, text="How much do you wish to deposit?", fill='white', font=deposit_subfont)
depositcanvas.create_text(550, 260, text="Enter your desired amount:", fill='white', font=deposit_subfont)

deposit_value1 = StringVar()
deposit_image = Image.open(r"image files\php_txtbox.png")
deposit_resize = deposit_image.resize((330, 60))
deposit_img = ImageTk.PhotoImage(deposit_resize)
depositcanvas.create_image(385, 300, anchor="nw", image=deposit_img)

specialchar=['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/',"'","[",']',"|","\\",'.',';','{','}',':','"']

def deposit_limit(*args):
    if int(deposit_entry.get()) > 50000:
        messagebox.showerror('Error!', 'You have reached the amount limit')
        deposit_entry.delete(0, END)
    elif deposit_entry.get().isalpha() == True or deposit_entry.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        deposit_entry.delete(0, END)


deposit_value1.trace("w", lambda *args: deposit_limit(deposit_value1))

# creating text box for pin1
deposit_entry = Entry(deposit,
                      font=depositfont,
                      width=8,
                      fg="white",
                      bd=0,
                      bg="#161B81",
                      justify="right",
                      textvariable=deposit_value1)
deposit_entry.pack()
depositbox = depositcanvas.create_window(605, 329, window=deposit_entry)
deposit_entry.bind('<BackSpace>', lambda *args: 'break')



# button for one thousand
def onethou(event):
    value1 = 1000
    if len(deposit_entry.get()) != 0:
        deposit_entry.delete(0, END)
        deposit_entry.insert(0, value1)

    elif len(deposit_entry.get()) == 0:
        deposit_entry.insert(0, value1)


onethou_image = Image.open(r'image files\1k.png')
onethou_resize = onethou_image.resize((150,50))
onethou_final = ImageTk.PhotoImage(onethou_resize)
onethou_layout = depositcanvas.create_image(220, 400, anchor=NW, image=onethou_final)
depositcanvas.tag_bind(onethou_layout, "<Button-1>", onethou)

# button for two thousand
def twothou(event):
    value1 = 2000
    if len(deposit_entry.get()) != 0:
        deposit_entry.delete(0, END)
        deposit_entry.insert(0, value1)

    elif len(deposit_entry.get()) == 0:
        deposit_entry.insert(0, value1)


twothou_image = Image.open(r'image files\2k.png')
twothou_resize = twothou_image.resize((150,53))
twothou_final = ImageTk.PhotoImage(twothou_resize)
twothou_layout = depositcanvas.create_image(390, 400, anchor=NW, image=twothou_final)
depositcanvas.tag_bind(twothou_layout, "<Button-1>", twothou)

# button for five thousand
def fivethou(event):
    value1 = 5000
    if len(deposit_entry.get()) != 0:
        deposit_entry.delete(0, END)
        deposit_entry.insert(0, value1)

    elif len(deposit_entry.get()) == 0:
        deposit_entry.insert(0, value1)


fivethou_image = Image.open(r'image files\5k.png')
fivethou_resize = fivethou_image.resize((150,50))
fivethou_final = ImageTk.PhotoImage(fivethou_resize)
fivethou_layout = depositcanvas.create_image(560, 400, anchor=NW, image=fivethou_final)
depositcanvas.tag_bind(fivethou_layout, "<Button-1>", fivethou)


# button for ten thousand
def tenthou(event):
    value1 = 10000
    if len(deposit_entry.get()) != 0:
        deposit_entry.delete(0, END)
        deposit_entry.insert(0, value1)

    elif len(deposit_entry.get()) == 0:
        deposit_entry.insert(0, value1)

tenthou_image = Image.open(r'image files\10k.png')
tenthou_resize = tenthou_image.resize((150,50))
tenthou_final = ImageTk.PhotoImage(tenthou_resize)
tenthou_layout = depositcanvas.create_image(730, 400, anchor=NW, image=tenthou_final)
depositcanvas.tag_bind(tenthou_layout, "<Button-1>", tenthou)

# button for deleting
def clicked(event):
    deposit_entry.delete(0,END)



backspace_img = Image.open(r"image files/Backspace.png")
backspace_resize = backspace_img.resize((50,50))
backspace = ImageTk.PhotoImage(backspace_resize)
backspacebtn = depositcanvas.create_image(750, 330, image=backspace)
depositcanvas.tag_bind(backspacebtn, "<Button-1>", clicked)


deposit.resizable(False, False)
deposit.mainloop()
