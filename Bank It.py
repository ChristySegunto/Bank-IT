from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as TkFont

timesclicked = 0
specialchar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',',
                                       '<', '>', '/', "'", "[", ']', "|", "\\", '.', ';', '{', '}', ':', '"']
#phptextbox1_string1 = StringVar()


#Start page
main = Tk()
main.geometry("1100x628")
main.title("Bank IT")
main.iconbitmap(r"image files/logo.ico")


#login window background
mainbg = ImageTk.PhotoImage(file=r"image files/BG-1.png")

#Creating canvas for bg and texts
maincanvas = Canvas(main, width = 1100,
                 height = 628)

maincanvas.pack(fill = "both", expand = True)
maincanvas.create_image( 0, 0, image = mainbg,
                     anchor = "nw")

#declaring the properties of font
mainfont = TkFont.Font(family="Myriad Pro", size=100, weight="bold")
subfont = TkFont.Font(family="Myriad Pro", size=14)
smallfont = TkFont.Font(family="Myriad Pro", size=8)

#creatings texts
maincanvas.create_text( 490, 280, text = "Bank", fill='white', font=mainfont)
maincanvas.create_text( 715, 280, text = "IT", fill='#f6008d', font=mainfont)

maincanvas.create_text( 550, 360, text = "Automated Teller Machine System", fill='white', font=subfont)

def start(event):
    main.withdraw()
    login = Toplevel()
    login.geometry("1100x628")
    login.title("Bank IT")
    login.iconbitmap(r"image files\logo.ico")

    loginbg = ImageTk.PhotoImage(file=r"image files\BG-1.png")

    logincanvas = Canvas(login, width=1100,
                     height=628)
    logincanvas.pack(fill="both", expand=True)
    logincanvas.create_image(0, 0, image=loginbg,
                         anchor="nw")

    # logo of bank it
    logo = ImageTk.PhotoImage(file=r"image files\logo.png")
    logincanvas.create_image(80, 40, image=logo,
                         anchor="nw")

    # creating font
    login_mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
    login_subfont = TkFont.Font(family="Myriad Pro", size=14)
    login_smallfont = TkFont.Font(family="Myriad Pro", size=8)
    # creatings texts
    logincanvas.create_text(240, 280, text="Bank", fill='white', font=login_mainfont)
    logincanvas.create_text(420, 280, text="IT", fill='#f6008d', font=login_mainfont)
    logincanvas.create_text(270, 340, text="Automated Teller Machine System", fill='white', font=login_subfont)

    # login acc
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # Username section
    logincanvas.create_text(670, 210, text="USERNAME", fill='white', font=smallfont)
    txtbox_img = Image.open(r"image files\textbox.png")
    txtbox_resize = txtbox_img.resize((450, 140))
    txtbox = ImageTk.PhotoImage(txtbox_resize)
    logincanvas.create_image(570, 175, anchor=NW, image=txtbox)

    un_entry = Entry(logincanvas,
                     bd=0,
                     bg="#050519",
                     fg="#fff",
                     highlightthickness=0,
                     font=("Myriad pro", 16 * -1),
                     insertbackground="#fff",
                     textvariable=USERNAME)

    un_entry.pack()
    username = logincanvas.create_window(750, 245, window=un_entry)

    # Password Section
    logincanvas.create_text(670, 300, text="PASSWORD", fill='white', font=smallfont)
    txtbox2 = ImageTk.PhotoImage(txtbox_resize)
    logincanvas.create_image(570, 265, anchor=NW, image=txtbox2)
    pass_entry = Entry(logincanvas,
                       bd=0,
                       bg="#050519",
                       fg="#fff",
                       highlightthickness=0,
                       font=("Myriad pro", 16 * -1),
                       insertbackground="#fff",
                       show='*',
                       textvariable=PASSWORD)
    pass_entry.pack()
    password = logincanvas.create_window(750, 334, window=pass_entry)

    # login btn
    def checkacc(event):
        if USERNAME.get() == 'Christysegunto' and PASSWORD.get() == '12345':
            login.withdraw()
            pin = Toplevel()
            pin.geometry("1100x628")
            pin.title("Bank IT")
            pin.iconbitmap(r"image files\logo.ico")
            pinbg = ImageTk.PhotoImage(file=r"image files\BG-1.png")
            pincanvas = Canvas(pin, width=1100,
                             height=628)

            pincanvas.pack(fill="both", expand=True)
            pincanvas.create_image(0, 0, image=pinbg,
                                 anchor="nw")

            logo = ImageTk.PhotoImage(file=r"image files\logo.png")
            pincanvas.create_image(80, 40, image=logo,
                                 anchor="nw")

            #creating fonts for pin page
            pin_mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
            pin_subfont = TkFont.Font(family="Myriad Pro", size=11)
            pin_pinfont = TkFont.Font(family="Myriad Pro", size=50)
            #creating text
            pincanvas.create_text(550, 160, text="PIN", fill='white', font=mainfont)
            pincanvas.create_text(550, 250, text="Please enter your 4-digit pin code:", fill='white', font=subfont)

            def back(event):
                pin.withdraw()
                login.deiconify()

            backPhoto = ImageTk.PhotoImage(Image.open(r"image files\backbtn.png"))
            btnBack = pincanvas.create_image(1000, 590, image=backPhoto)
            pincanvas.tag_bind(btnBack, "<Button-1>", back)

            #pin box
            pin1Photo = ImageTk.PhotoImage(Image.open(r"image files\pinbtn.png"))
            entryPin1 = pincanvas.create_image(298, 350, image=pin1Photo)
            pin2Photo = ImageTk.PhotoImage(Image.open(r"image files\pinbtn.png"))
            entryPin2 = pincanvas.create_image(458, 350, image=pin2Photo)
            pin3Photo = ImageTk.PhotoImage(Image.open(r"image files\pinbtn.png"))
            entryPin3 = pincanvas.create_image(618, 350, image=pin3Photo)
            pin4Photo = ImageTk.PhotoImage(Image.open(r"image files\pinbtn.png"))
            entryPin4 = pincanvas.create_image(778, 350, image=pin4Photo)

            #declaring pin
            pinfont = TkFont.Font(family="Myriad Pro", size=50)
            pin_value1 = StringVar()
            pin_value2 = StringVar()
            pin_value3 = StringVar()
            pin_value4 = StringVar()


            # declaring limits for pin 1
            def pin1_limit(*args):
                if len(pin_value1.get()) > 0:
                    pin_value1.set(pin_value1.get()[-1])
                if pin_value1.get().isalpha() == True or pin_value1.get() in specialchar:
                    messagebox.showerror('Error!', 'You must input a number')
                    pin1_entry.delete(len(pin1_entry.get()) - 1)
            pin_value1.trace("w", lambda *args: pin1_limit(pin_value1))

            # declaring limits for pin 2
            def pin2_limit(*args):
                if len(pin_value2.get()) > 0:
                    pin_value2.set(pin_value2.get()[-1])
                if pin_value2.get().isalpha() == True or pin_value2.get() in specialchar:
                    messagebox.showerror('Error!', 'You must input a number')
                    pin2_entry.delete(len(pin2_entry.get()) - 1)
            pin_value2.trace("w", lambda *args: pin2_limit(pin_value2))

            # declaring limits for pin 3
            def pin3_limit(*args):
                if len(pin_value3.get()) > 0:
                    pin_value3.set(pin_value3.get()[-1])
                if pin_value3.get().isalpha() == True or pin_value3.get() in specialchar:
                    messagebox.showerror('Error!', 'You must input a number')
                    pin3_entry.delete(len(pin3_entry.get()) - 1)
            pin_value3.trace("w", lambda *args: pin3_limit(pin_value3))

            # declaring limits for pin 4
            def pin4_limit(*args):
                if len(pin_value4.get()) > 0:
                    pin_value4.set(pin_value4.get()[-1])
                if pin_value4.get().isalpha() == True or pin_value4.get() in specialchar:
                    messagebox.showerror('Error!', 'You must input a number')
                    pin4_entry.delete(len(pin4_entry.get()) - 1)
            pin_value4.trace("w", lambda *args: pin4_limit(pin_value4))

            # creating text box for pin1
            pin1_entry = Entry(pin,
                               font=pinfont,
                               width=2,
                               fg="white",
                               bd=0,
                               bg="#161B81",
                               justify="center",
                               textvariable=pin_value1)
            pin1_entry.pack()
            pin1 = pincanvas.create_window(297, 350, window=pin1_entry)
            pin1_entry.bind('<BackSpace>', lambda *args: 'break')

            # creating text box for pin2
            pin2_entry = Entry(pin,
                               font=pinfont,
                               width=2,
                               fg="white",
                               bd=0,
                               bg="#161B81",
                               justify="center",
                               textvariable=pin_value2)
            pin2_entry.pack()
            pin2 = pincanvas.create_window(455, 350, window=pin2_entry)
            pin2_entry.bind('<BackSpace>', lambda *args: 'break')

            # creating text box for pin3
            pin3_entry = Entry(pin,
                               font=pinfont,
                               width=2,
                               fg="white",
                               bd=0,
                               bg="#161B81",
                               justify="center",
                               textvariable=pin_value3)
            pin3_entry.pack()
            pin3 = pincanvas.create_window(615, 350, window=pin3_entry)
            pin3_entry.bind('<BackSpace>', lambda *args: 'break')

            # creating text box for pin4
            pin4_entry = Entry(pin,
                               font=pinfont,
                               width=2,
                               fg="white",
                               bd=0,
                               bg="#161B81",
                               justify="center",
                               textvariable=pin_value4)
            pin4_entry.pack()
            pin4 = pincanvas.create_window(780, 350, window=pin4_entry)
            pin4_entry.bind('<BackSpace>', lambda *args: 'break')

            def checkpin(event):
                if pin_value1.get() == '5' and pin_value2.get() == '2' and pin_value3.get() == '4' and pin_value4.get() == '1':
                    pin.withdraw()
                    home = Toplevel()
                    home.geometry("1100x628")
                    home.title("Bank IT")
                    home.iconbitmap(r"image files\logo.ico")
                    homebg = ImageTk.PhotoImage(file=r"image files\BG-3.jpg")

                    homecanvas = Canvas(home, width=1100,
                                     height=628)
                    homecanvas.pack(fill="both", expand=True)
                    homecanvas.create_image(0, 0, image=homebg,
                                         anchor="nw")
                    logo = ImageTk.PhotoImage(file=r"image files\logo.png")
                    homecanvas.create_image(80, 40, image=logo,
                                         anchor="nw")

                    #creating font for home page
                    home_mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
                    home_subfont = TkFont.Font(family="Myriad Pro", size=11)
                    #creating texts for home page
                    homecanvas.create_text(550, 180, text="Hello,", fill='white', font=home_mainfont)
                    homecanvas.create_text(550, 270, text="How can we help you today?", fill='white', font=home_subfont)


                    #for withdraw button
                    def withdraw(event):
                        home.destroy()
                        withdraw = Toplevel()
                        withdraw.geometry("1100x628")
                        withdraw.title("Bank IT")
                        withdraw.iconbitmap(r"image files\logo.ico")
                        withdrawbg = ImageTk.PhotoImage(file=r"image files\BG-2.jpg")

                        withdrawcanvas = Canvas(withdraw, width=1100, height=628)
                        withdrawcanvas.pack(fill="both", expand=True)
                        withdrawcanvas.create_image(0, 0, image=withdrawbg, anchor="nw")

                        # logo of bank it
                        logo = ImageTk.PhotoImage(file=r"image files\logo.png")
                        withdrawcanvas.create_image(80, 40, image=logo,
                                                    anchor="nw")

                        # window page font
                        withdraw_mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
                        withdraw_subfont = TkFont.Font(family="Myriad Pro", size=14)
                        withdrawfont = TkFont.Font(family="Myriad Pro", size=30)

                        # window page logo
                        logo = ImageTk.PhotoImage(file=r'image files\logo.png')
                        withdrawcanvas.create_image(80, 40, image=logo, anchor="nw")

                        # window text
                        withdrawcanvas.create_text(550, 160, text="Withdraw", fill='white', font=withdraw_mainfont)
                        withdrawcanvas.create_text(550, 240, text="How much do you wish to withdraw?", fill='white',
                                                   font=withdraw_subfont)
                        withdrawcanvas.create_text(550, 260, text="Enter your desired amount:", fill='white',
                                                   font=withdraw_subfont)

                        # window textbox
                        withdraw_image = Image.open(r"image files\php_txtbox.png")
                        withdraw_resize = withdraw_image.resize((330, 60))
                        withdraw_img = ImageTk.PhotoImage(withdraw_resize)
                        withdrawcanvas.create_image(385, 300, anchor="nw", image=withdraw_img)

                        withdraw_value1 = StringVar()
                        value1 = int()
                        amount = int()


                        # creating textbox limit
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
                        withdrawbox = withdrawcanvas.create_window(605, 329, window=withdraw_entry)
                        withdraw_entry.bind('<BackSpace>', lambda *args: 'break')

                        # button for one thousand
                        def onethou(event):

                            value1 = "1000"
                            if len(withdraw_entry.get()) != 0:
                                withdraw_entry.delete(0, END)
                                withdraw_entry.insert(0, value1)

                            elif len(withdraw_entry.get()) == 0:
                                withdraw_entry.insert(0, value1)

                        onethou_image = Image.open(r'image files\1k.png')
                        onethou_resize = onethou_image.resize((150, 50))
                        onethou_final = ImageTk.PhotoImage(onethou_resize)
                        onethou_layout = withdrawcanvas.create_image(220, 400, anchor=NW, image=onethou_final)
                        withdrawcanvas.tag_bind(onethou_layout, "<Button-1>", onethou)

                        # button for two thousand
                        def twothou(event):

                            value1 = "2000"
                            if len(withdraw_entry.get()) != 0:
                                withdraw_entry.delete(0, END)
                                withdraw_entry.insert(0, value1)

                            elif len(withdraw_entry.get()) == 0:
                                withdraw_entry.insert(0, value1)

                        twothou_image = Image.open(r'image files\2k.png')
                        twothou_resize = twothou_image.resize((150, 53))
                        twothou_final = ImageTk.PhotoImage(twothou_resize)
                        twothou_layout = withdrawcanvas.create_image(390, 400, anchor=NW, image=twothou_final)
                        withdrawcanvas.tag_bind(twothou_layout, "<Button-1>", twothou)

                        # button for five thousand
                        def fivethou(event):
                            global amount
                            value1 = "5000"
                            if len(withdraw_entry.get()) != 0:
                                withdraw_entry.delete(0, END)
                                withdraw_entry.insert(0, value1)

                            elif len(withdraw_entry.get()) == 0:
                                withdraw_entry.insert(0, value1)

                        fivethou_image = Image.open(r'image files\5k.png')
                        fivethou_resize = fivethou_image.resize((150, 50))
                        fivethou_final = ImageTk.PhotoImage(fivethou_resize)
                        fivethou_layout = withdrawcanvas.create_image(560, 400, anchor=NW, image=fivethou_final)
                        withdrawcanvas.tag_bind(fivethou_layout, "<Button-1>", fivethou)

                        # button for ten thousand
                        def tenthou(event):
                            global amount
                            value1 = "10000"
                            if len(withdraw_entry.get()) != 0:
                                withdraw_entry.delete(0, END)
                                withdraw_entry.insert(0, value1)
                            elif len(withdraw_entry.get()) == 0:
                                withdraw_entry.insert(0, value1)

                        tenthou_image = Image.open(r'image files\10k.png')
                        tenthou_resize = tenthou_image.resize((150, 50))
                        tenthou_final = ImageTk.PhotoImage(tenthou_resize)
                        tenthou_layout = withdrawcanvas.create_image(730, 400, anchor=NW, image=tenthou_final)
                        withdrawcanvas.tag_bind(tenthou_layout, "<Button-1>", tenthou)

                        # button for deleting
                        def clicked(event):
                            withdraw_entry.delete(0, END)

                        backspace_img = Image.open(r"image files/Backspace.png")
                        backspace_resize = backspace_img.resize((50, 50))
                        backspace = ImageTk.PhotoImage(backspace_resize)
                        backspacebtn = withdrawcanvas.create_image(750, 330, image=backspace)
                        withdrawcanvas.tag_bind(backspacebtn, "<Button-1>", clicked)

                        def submitbtn(event):
                            if amount > 50000:
                                messagebox.showerror('Error!', 'You have exceeded your limit')
                            # if amount <= balance:

                        submitbtn_img = ImageTk.PhotoImage(Image.open(r"image files/submitbtn.png"))
                        submitbtn = withdrawcanvas.create_image(535, 530, image=submitbtn_img)

                        withdrawcanvas.tag_bind(submitbtn, "<Button-1>", submitbtn)

                        withdraw.resizable(False, False)
                        withdraw.mainloop()




                    withdrawPhoto = ImageTk.PhotoImage(Image.open(r"image files\withdrawbtn.png"))
                    btnWithdraw = homecanvas.create_image(550, 360, image=withdrawPhoto)
                    homecanvas.tag_bind(btnWithdraw, "<Button-1>", withdraw)

                    #for balance inquiry button
                    def balinq(event):
                        home.destroy()

                        balance = Toplevel()
                        balance.geometry("1100x628")
                        balance.title("Bank IT")
                        balance.iconbitmap(r"image files\logo.ico")
                        balancebg = ImageTk.PhotoImage(file=r"image files\BG-2.jpg")

                        balancecanvas = Canvas(balance, width=1100, height=628)
                        balancecanvas.pack(fill="both", expand=True)
                        balancecanvas.create_image(0, 0, image=balancebg, anchor="nw")

                        # logo of bank it
                        logo = ImageTk.PhotoImage(file=r"image files\logo.png")
                        balancecanvas.create_image(80, 40, image=logo,
                                                    anchor="nw")

                        # balance inquiry page font
                        balance_mainfont = TkFont.Font(family="Myriad Pro", size=75, weight="bold")
                        balance_subfont = TkFont.Font(family="Myriad Pro", size=14)
                        balancefont = TkFont.Font(family="Myriad Pro", size=30)

                        # balance inquiry page logo
                        logo = ImageTk.PhotoImage(file=r'image files\logo.png')
                        balancecanvas.create_image(80, 40, image=logo, anchor="nw")

                        # balance inquiry design/layout
                        balancecanvas.create_text(550, 160, text="Balance", fill='white', font=balance_mainfont)
                        balancecanvas.create_text(555, 300, text="Account Balance (Savings)", fill='#F6008d', font=balance_subfont)

                        phptextbox = Image.open('image files\php_txtbox.png')
                        phptextbox_resize = phptextbox.resize((340, 70))
                        phptextbox_final = ImageTk.PhotoImage(phptextbox_resize)
                        balancecanvas.create_image(380, 340, anchor=NW, image=phptextbox_final)

                        # back button
                        def backbutton(event):
                            balance.withdraw()

                        backbutton_image = Image.open(
                            r'image files\backbtn.png')
                        backbutton_image_resize = backbutton_image.resize((200, 40))
                        backbutton_image_final = ImageTk.PhotoImage(backbutton_image_resize)
                        backbutton_image_layout = balancecanvas.create_image(900, 560, anchor=NW, image=backbutton_image_final)
                        balancecanvas.tag_bind(backbutton_image_layout, "<Button-1>", backbutton)




                        balance.resizable(False, False)
                        balance.mainloop()

                    balinqPhoto = ImageTk.PhotoImage(Image.open(r"image files\binquirybtn.png"))
                    btnBInquiry = homecanvas.create_image(550, 420, image=balinqPhoto)
                    homecanvas.tag_bind(btnBInquiry, "<Button-1>", balinq)



                    def deposit(event):
                        home.destroy()



                    depositPhoto = ImageTk.PhotoImage(Image.open(r"image files\depositbtn.png"))
                    btnDeposit = homecanvas.create_image(550, 480, image=depositPhoto)
                    homecanvas.tag_bind(btnDeposit, "<Button-1>", deposit)



                    home.resizable(False, False)
                    home.mainloop()

                else:
                    messagebox.showerror('Error', 'Wrong pin! Please try again.')
                    pin1_entry.delete(len(pin1_entry.get()) - 1)
                    pin2_entry.delete(len(pin1_entry.get()) - 1)
                    pin3_entry.delete(len(pin1_entry.get()) - 1)
                    pin4_entry.delete(len(pin1_entry.get()) - 1)

            submitbtn_img = ImageTk.PhotoImage(Image.open(r"image files\submitbtn.png"))
            submitbtn = pincanvas.create_image(535, 490, image=submitbtn_img)

            pincanvas.tag_bind(submitbtn, "<Button-1>", checkpin)




            def clearclicked(event):
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



            backspace_img = Image.open(r"image files\Backspace.png")
            backspace_resize = backspace_img.resize((50, 50))
            backspace = ImageTk.PhotoImage(backspace_resize)
            backspacebtn = pincanvas.create_image(920, 360, image=backspace)

            pincanvas.tag_bind(backspacebtn, "<Button-1>", clearclicked)

            pin.resizable(False, False)
            pin.mainloop()

    # declaring image as btn
    loginbtn_img = ImageTk.PhotoImage(Image.open(r"image files\loginbtn.png"))
    loginbtn = logincanvas.create_image(785, 450, image=loginbtn_img)

    logincanvas.tag_bind(loginbtn, "<Button-1>", checkacc)

    login.resizable(False, False)
    login.mainloop()

startbtn_img = ImageTk.PhotoImage(Image.open(r"image files\startbtn.png"))
startbtn = maincanvas.create_image(550, 430, image=startbtn_img)
maincanvas.tag_bind(startbtn, "<Button-1>", start)

main.resizable(False, False)
main.mainloop()