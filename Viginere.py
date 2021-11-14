from tkinter import Label

def vig_encrypt(text,key,self):
    x=text.get().upper()
    y=key.get()
    test_text=False
    test_key=False
    for i in range(len(x)):
        if (ord(x[i])>=65 and ord(x[i])<=90)or(ord(x[i])>=97 or ord(x[i])<=122):
            test_text=True
    for i in range(len(y)):
        if (ord(y[i])>=65 and ord(y[i])<=90)or(ord(y[i])>=97 or ord(y[i])<=122):
            test_key=True
    if test_text == False or x=="":
        error = Label(self,text='Plain text needs to be alphabetical , Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=50,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        error = Label(self,text='Encryption key needs to be alphabetical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=45,y=60)
        self.after(2000, error.destroy)
    else:
        z=''
        nb=0
        for i in range(len(x)):
            if nb>len(y)-1:
                nb=0
            if x[i]==" ":
                z+=" "
            else:
                aux1=ord(x[i])-64
                aux2=ord(y[nb])-64
                res=aux1+aux2
                while res>26:
                    res=res-26
                z=z+chr(res+64)
                nb+=1
        result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)
    

def vig_decrypt(text,key,self):
    x=text.get().upper()
    y=key.get().upper()
    test_text=False
    test_key=False
    for i in range(len(x)):
        if (ord(x[i])>=65 and ord(x[i])<=90)or(ord(x[i])>=97 or ord(x[i])<=122):
            test_text=True
    for i in range(len(y)):
        if (ord(y[i])>=65 and ord(y[i])<=90)or(ord(y[i])>=97 or ord(y[i])<=122):
            test_key=True
    if test_text == False or x=="":
        error = Label(self,text='Encrypted text needs to be alphabetical , Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=40,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        error = Label(self,text='Decryption key needs to be alphabatical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=45,y=60)
        self.after(2000, error.destroy)
    else:
        z=''
        nb=0
        for i in range(len(x)):
            if nb>len(y)-1:
                nb=0
            if x[i]==" ":
                z+=" "
            else:
                aux1=ord(x[i])
                aux2=ord(y[nb])-64
                res=aux1-aux2
                while res<65:
                    res=res+26
                z+=chr(res)
                nb+=1
        result = Label(self, text=z, bg="#ccc", width=20,height=2).place(x=100,y=270)