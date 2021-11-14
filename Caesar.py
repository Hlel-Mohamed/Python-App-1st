from tkinter import Label
from alphab import *

def cae_encrypt(text,key,self):
    x=text.get().upper()
    test_text=alphabatical(x)
    y=key.get()
    test_key=str.isnumeric(y)

    if x=="" or test_text==False:
        error = Label(self,text='Plain text needs to be alphabetical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=55,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        error = Label(self,text='Encryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=45,y=60)
        self.after(2000, error.destroy)
    else:
        z=''
        for i in range(len(x)):
            if x[i]==" ":
                z+=" "
            else:
                res=ord(x[i])-64+int(y)
                while res>26:
                    res=res-26
                z+=chr(res+64)
        result = Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=100,y=270)
            

def cae_decrypt(text,key,self):
    x=text.get().upper()
    test_text=alphabatical(x)
    y=key.get()
    test_key=str.isnumeric(y)

    if x=="" or test_text==False:
        error = Label(self,text='Encrypted text needs to be alphabetical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=50,y=60)
        self.after(2000, error.destroy)
    elif test_key == False:
        error = Label(self,text='Decryption key needs to be numeratical, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=45,y=60)
        self.after(2000, error.destroy)
    else:
        z=''
        for i in range(len(x)):
            if x[i]==" ":
                z+=" "
            else:
                res=ord(x[i])-int(y)
                while res<65:
                    res=res+26
                z+=chr(res)
        result = Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=100,y=270)