
from tkinter import *
from tkinter import font


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
            x=text.get()
            test=False
            for i in range(len(x)):
                if (ord(x[i])<65 or ord(x[i])>90):
                    test=False
                    error = Label(self,text='Plain text needs to be uppercase, Re enter: ').pack()
                    #error.after(1000, error.destroy())
            y=key.get()
            z=''
            for i in range(len(x)):
                res=ord(x[i])-64+int(y)
                while res>26:
                    res=res-26
                z=z+chr(res+64)
            result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)
        def decrypt():
            x=text.get()
            test=False
            while test==False:
                test=True
                for i in range(len(x)):
                    if (ord(x[i])<65 or ord(x[i])>90):
                        test=False
                        
            y=key.get()
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
            result = Label(self, text=text.get(), bg="#ccc", width=20,height=2).place(x=100,y=270)
        def decrypt():
            result = Label(self, text=text.get(), bg="#ccc", width=20,height=2).place(x=100,y=270)


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