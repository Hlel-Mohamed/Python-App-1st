from tkinter import Label
from genMeth import *
from hillMeth import *

def hill_encrypt(text,key,self):
    x=text.get().upper()
    test_text=alphabatical(x)
    y=key.get().upper()
    test_key=alphabatical(y)

    if test_text == False or x=="":
        error = Label(self,text='Plain text needs to be alphabetical , Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=50,y=60)
        self.after(2000, error.destroy)
    elif test_key == False or (len(y)!=4):
        error = Label(self,text='Encryption key needs to be composed of 4 letters, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=15,y=60)
        self.after(2000, error.destroy)
    else:
        space = [i for i in range(len(x)) if x.startswith(" ", i)]
        x=x.replace(" ", "")
        if len(x)%2 != 0:
            x += "o"
        key_mat=keyToMat(y)
        msg_mat=msgToMat(x)

        determinant = 0
        determinant = key_mat[0][0]*key_mat[1][1]-key_mat[0][1]*key_mat[1][0]
        determinant %= 26

        if(inversible(determinant)!=-1):
            z=""
            for i in range (int((len(x)/2))):
                row=msg_mat[0][i]*key_mat[0][0]+msg_mat[1][i]*key_mat[0][1]
                elem=int (row%26 + 65)
                z+=chr(elem)
                row=msg_mat[0][i]*key_mat[1][0]+msg_mat[1][i]*key_mat[1][1]
                elem=int (row%26 + 65)
                z+=chr(elem)
            for i in space:
                z=z[:i] + " " + z[i:]
            result = Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=100,y=270)
        else:
            error = Label(self,text='Uninvertible key, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
            error.place(x=100,y=60)
            self.after(2000, error.destroy)


def hill_decrypt(text,key,self):
    x=text.get().upper()
    test_text=alphabatical(x)
    y=key.get().upper()
    test_key=alphabatical(y)

    if test_text == False or x=="":
        error = Label(self,text='Encryption text needs to be alphabetical , Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=40,y=60)
        self.after(2000, error.destroy)
    elif test_key == False or (len(y)!=4):
        error = Label(self,text='Decryption key needs to be composed of 4 letters, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
        error.place(x=15,y=60)
        self.after(2000, error.destroy)
    else:
        space = [i for i in range(len(x)) if x.startswith(" ", i)]
        x=x.replace(" ", "")
        if len(x)%2 != 0:
            x += "o"
        key_mat=keyToMat(y)
        msg_mat=msgToMat(x)

        determinant = 0
        determinant = key_mat[0][0]*key_mat[1][1]-key_mat[0][1]*key_mat[1][0]
        determinant %= 26
        
        inv_mat=multDet(key_mat,determinant)
        
        if(inversible(determinant)!=-1):
            z=""
            for i in range (int((len(x)/2))):
                row=msg_mat[0][i]*inv_mat[0][0]+msg_mat[1][i]*inv_mat[0][1]
                elem=int (row%26 + 65)
                z+=chr(elem)
                row=msg_mat[0][i]*inv_mat[1][0]+msg_mat[1][i]*inv_mat[1][1]
                elem=int (row%26 + 65)
                z+=chr(elem)
            if z[-1]=="o":
                z=z[:-1]
            for i in space:
                z=z[:i] + " " + z[i:]
            result = Label(self, text=z, bg="black",fg="white", width=20,height=2).place(x=100,y=270)
        else:
            error = Label(self,text='Uninvertible key, Re enter: ', bg="#5896ed", font=("Times", 10 ,"italic"))
            error.place(x=100,y=60)
            self.after(2000, error.destroy)