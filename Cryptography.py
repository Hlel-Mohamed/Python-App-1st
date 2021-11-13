from tkinter import *
from tkinter import font
from sys import exit


class root(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home, Caesar, Viginere, Hill):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.winfo_toplevel().title(page_name)


class Home(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5896ed")

        label = Label(self, text="Cryptography", font=controller.title_font, bg="#5896ed")
        label.pack(side="top", fill="x", pady=10)

        caes_but = Button(self, text="Caesar",command=lambda: controller.show_frame("Caesar"),width=20, pady=10)
        vig_but = Button(self, text="Viginere",command=lambda: controller.show_frame("Viginere"),width=20, pady=10)
        hill_but = Button(self, text="Hill",command=lambda: controller.show_frame("Hill"),width=20, pady=10)
        caes_but.place(x=100,y=100)
        vig_but.place(x=100,y=150)
        hill_but.place(x=100,y=200)
        Button(self, text="Exit",command=exit).place(x=0,y=0)



class Caesar(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5896ed")

        label = Label(self, text="Caesar", font=controller.title_font, bg="#5896ed")
        label.pack(side="top", fill="x", pady=10)
        
        Button(self, text="Back",command=lambda: controller.show_frame("Home")).place(x=0,y=0)
        Label(self, text="Text", bg="#5896ed").place(x=60,y=100)
        text = Entry(self, width=30)
        text.place(x=110,y=100)
        Label(self, text="Key", bg="#5896ed").place(x=60,y=150)
        key = Entry(self, width=30)
        key.place(x=110,y=150)

        Label(self, text="Result", bg="#ccc", width=20,height=2).place(x=100,y=270)


        def encrypt():
            x=text.get().upper()
            y=key.get()
            test_key=str.isnumeric(y)
            if test_key == False:
                error = Label(self,text='Encryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=45,y=60)
                self.after(2000, error.destroy)
            else:
                z=''
                for i in range(len(x)):
                    res=ord(x[i])-64+int(y)
                    while res>26:
                        res=res-26
                    z=z+chr(res+64)
                result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)
            

        def decrypt():
            x=text.get().upper()
            y=key.get()
            test_key=str.isnumeric(y)
            if test_key == False:
                error = Label(self,text='Decryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=45,y=60)
                self.after(2000, error.destroy)
            else:
                z=''
                for i in range(len(x)):
                    res=ord(x[i])-int(y)
                    while res<65:
                        res=res+26
                    z=z+chr(res)
                result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)


        enc_but = Button(self, text="Encrypt", padx=50,pady=10, command=encrypt, bg="#b0b0b0", fg="black")
        enc_but.place(x=30,y=200)
        dec_but = Button(self, text="Decrypt", padx=50,pady=10, command=decrypt, bg="#b0b0b0", fg="black")
        dec_but.place(x=180,y=200)



class Viginere(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5896ed")

        label = Label(self, text="Viginere", font=controller.title_font, bg="#5896ed")
        label.pack(side="top", fill="x", pady=10)

        Button(self, text="Back",command=lambda: controller.show_frame("Home")).place(x=0,y=0)

        Label(self, text="Text", bg="#5896ed").place(x=60,y=100)
        text = Entry(self, width=30)
        text.place(x=110,y=100)
        Label(self, text="Key", bg="#5896ed").place(x=60,y=150)
        key = Entry(self, width=30)
        key.place(x=110,y=150)

        Label(self, text="Result", bg="#ccc", width=20,height=2).place(x=100,y=270)


        def encrypt():
            x=text.get()
            y=key.get()
            test_text=True
            test_key=True
            for i in range(len(x)):
                if (ord(x[i])<65 or ord(x[i])>90):
                    test_text=False
            for i in range(len(y)):
                if (ord(y[i])<65 or ord(y[i])>90):
                    test_key=False
            if test_text == False or x=="":
                error = Label(self,text='Plain text needs to be alphabetical uppercase, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=25,y=60)
                self.after(2000, error.destroy)
            elif test_key == False:
                error = Label(self,text='Encryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=45,y=60)
                self.after(2000, error.destroy)
            else:
                z=''
                for i in range(len(x)):
                    aux1=ord(x[i])-64
                    aux2=ord(y[i])-64
                    res=aux1+aux2
                    while res>26:
                        res=res-26
                    z=z+chr(res+64)
                result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)
            

        def decrypt():
            x=text.get()
            y=key.get()
            test_text=True
            test_key=True
            for i in range(len(x)):
                if (ord(x[i])<65 or ord(x[i])>90):
                    test_text=False
            for i in range(len(y)):
                if (ord(y[i])<65 or ord(y[i])>90):
                    test_key=False
            if test_text == False or x=="":
                error = Label(self,text='Encrypted text needs to be alphabetical uppercase, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=10,y=60)
                self.after(2000, error.destroy)
            elif test_key == False:
                error = Label(self,text='Decryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
                error.place(x=45,y=60)
                self.after(2000, error.destroy)
            else:
                z=''
                for i in range(len(x)):
                    aux1=ord(x[i])
                    aux2=ord(y[i])-64
                    res=aux1-aux2
                    while res<65:
                        res=res+26
                    z=z+chr(res)
                result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)


        enc_but = Button(self, text="Encrypt", padx=50,pady=10, command=encrypt, bg="#b0b0b0", fg="black")
        enc_but.place(x=30,y=200)
        dec_but = Button(self, text="Decrypt", padx=50,pady=10, command=decrypt, bg="#b0b0b0", fg="black")
        dec_but.place(x=180,y=200)

class Hill(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#5896ed")

        label = Label(self, text="Hill", font=controller.title_font, bg="#5896ed")
        label.pack(side="top", fill="x", pady=10)

        Button(self, text="Back",command=lambda: controller.show_frame("Home")).place(x=0,y=0)

        Label(self, text="Text", bg="#5896ed").place(x=60,y=100)
        text = Entry(self, width=30)
        text.place(x=110,y=100)
        Label(self, text="Key", bg="#5896ed").place(x=60,y=150)
        key = Entry(self, width=30)
        key.place(x=110,y=150)

        Label(self, text="Result", bg="#ccc", width=20,height=2).place(x=100,y=270)


        def encrypt():
            result = Label(self, text=text.get(), bg="#ccc", width=20,height=2).place(x=100,y=270)
        def decrypt():
            result = Label(self, text=text.get(), bg="#ccc", width=20,height=2).place(x=100,y=270)


        enc_but = Button(self, text="Encrypt", padx=50,pady=10, command=encrypt, bg="#b0b0b0", fg="black")
        enc_but.place(x=30,y=200)
        dec_but = Button(self, text="Decrypt", padx=50,pady=10, command=decrypt, bg="#b0b0b0", fg="black")
        dec_but.place(x=180,y=200)


app = root()
app.geometry("350x350")
app.resizable(False, False)
app.mainloop()