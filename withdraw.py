from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.font import Font


withdraw = Tk()
withdraw.geometry("1100x628")
withdraw.title("Bank IT")
withdraw.iconbitmap(r"image files\logo.ico")

# window background
withdraw_background = ImageTk.PhotoImage(file=r'image files\BG-2.jpg')
withdrawcanvas = Canvas(withdraw, width=1100, height=628)
withdrawcanvas.pack(fill = "both", expand = True)
withdrawcanvas.create_image( 0, 0, image = withdraw_background, anchor = "nw")

# logo of bank it
logo = ImageTk.PhotoImage(file=r"image files\logo.png")
withdrawcanvas.create_image(80, 40, image=logo,
                     anchor="nw")

#window page font
withdraw_mainfont = Font(family="Myriad Pro", size=75, weight="bold")
withdraw_subfont = Font(family="Myriad Pro", size=14)
withdrawfont = Font(family="Myriad Pro", size=30)

# window page logo
logo = ImageTk.PhotoImage(file=r'image files\logo.png')
withdrawcanvas.create_image(80, 40, image = logo, anchor="nw")

# window text
withdrawcanvas.create_text( 550, 160, text = "Withdraw", fill='white', font=withdraw_mainfont)
withdrawcanvas.create_text( 550, 240, text = "How much do you wish to withdraw?", fill='white', font=withdraw_subfont)
withdrawcanvas.create_text( 550, 260, text = "Enter your desired amount:", fill='white', font=withdraw_subfont)

# window textbox
withdraw_image = Image.open(r"image files\php_txtbox.png")
withdraw_resize = withdraw_image.resize((330, 60))
withdraw_img = ImageTk.PhotoImage(withdraw_resize)
withdrawcanvas.create_image(385, 300, anchor="nw", image=withdraw_img)

withdraw_value1 = StringVar()
specialchar=['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/',"'","[",']',"|","\\",'.',';','{','}',':','"']

#creating textbox limit
def withdraw_limit(*args):

    if withdraw_entry.get().isalpha() == True or withdraw_entry.get() in specialchar:
        messagebox.showerror('Error!', 'You must input a number')
        withdraw_entry.delete(0, END)


withdraw_value1.trace("w", lambda *args: withdraw_limit(withdraw_value1))

# creating text box for pin1
withdraw_entry = Entry(withdraw,
                      font=withdrawfont,
                      width=8,
                      fg="white",
                      bd=0,
                      bg="#161B81",
                      justify="right",
                      textvariable=withdraw_value1)
withdraw_entry.pack()
depositbox = withdrawcanvas.create_window(605, 329, window=withdraw_entry)
withdraw_entry.bind('<BackSpace>', lambda *args: 'break')

# button for one thousand
def onethou(event):
    value1 = 1000
    if len(withdraw_entry.get()) != 0:
        withdraw_entry.delete(0, END)
        withdraw_entry.insert(0, value1)

    elif len(withdraw_entry.get()) == 0:
        withdraw_entry.insert(0, value1)


onethou_image = Image.open(r'image files\1k.png')
onethou_resize = onethou_image.resize((150,50))
onethou_final = ImageTk.PhotoImage(onethou_resize)
onethou_layout = withdrawcanvas.create_image(220, 400, anchor=NW, image=onethou_final)
withdrawcanvas.tag_bind(onethou_layout, "<Button-1>", onethou)

# button for two thousand
def twothou(event):
    value1 = 2000
    if len(withdraw_entry.get()) != 0:
        withdraw_entry.delete(0, END)
        withdraw_entry.insert(0, value1)

    elif len(withdraw_entry.get()) == 0:
        withdraw_entry.insert(0, value1)


twothou_image = Image.open(r'image files\2k.png')
twothou_resize = twothou_image.resize((150,53))
twothou_final = ImageTk.PhotoImage(twothou_resize)
twothou_layout = withdrawcanvas.create_image(390, 400, anchor=NW, image=twothou_final)
withdrawcanvas.tag_bind(twothou_layout, "<Button-1>", twothou)

# button for five thousand
def fivethou(event):
    value1 = 5000
    if len(withdraw_entry.get()) != 0:
        withdraw_entry.delete(0, END)
        withdraw_entry.insert(0, value1)

    elif len(withdraw_entry.get()) == 0:
        withdraw_entry.insert(0, value1)


fivethou_image = Image.open(r'image files\5k.png')
fivethou_resize = fivethou_image.resize((150,50))
fivethou_final = ImageTk.PhotoImage(fivethou_resize)
fivethou_layout = withdrawcanvas.create_image(560, 400, anchor=NW, image=fivethou_final)
withdrawcanvas.tag_bind(fivethou_layout, "<Button-1>", fivethou)

# button for ten thousand
def tenthou(event):
    value1 = 10000
    if len(withdraw_entry.get()) != 0:
        withdraw_entry.delete(0, END)
        withdraw_entry.insert(0, value1)

    elif len(withdraw_entry.get()) == 0:
        withdraw_entry.insert(0, value1)

tenthou_image = Image.open(r'image files\10k.png')
tenthou_resize = tenthou_image.resize((150,50))
tenthou_final = ImageTk.PhotoImage(tenthou_resize)
tenthou_layout = withdrawcanvas.create_image(730, 400, anchor=NW, image=tenthou_final)
withdrawcanvas.tag_bind(tenthou_layout, "<Button-1>", tenthou)

# button for deleting
def clicked(event):
    withdraw_entry.delete(0,END)

backspace_img = Image.open(r"image files/Backspace.png")
backspace_resize = backspace_img.resize((50,50))
backspace = ImageTk.PhotoImage(backspace_resize)
backspacebtn = withdrawcanvas.create_image(750, 330, image=backspace)
withdrawcanvas.tag_bind(backspacebtn, "<Button-1>", clicked)


withdraw.resizable(False, False)
withdraw.mainloop()
