from tkinter import *

root = Tk()
root.title("Caesar")
root.geometry("350x350")

Label(root, text="Plain text").place(x=40,y=100)
Enc_text = Entry(root, width=30)
Enc_text.place(x=130,y=100)
Label(root, text="Encryption key").place(x=40,y=150)
Enc_key = Entry(root, width=30)
Enc_key.place(x=130,y=150)


def myClick():
    res = "Result : " + Enc_text.get()
    myLabel1 = Label(root, text=res, bg="red").place(x=140,y=250)


myButton = Button(root, text="Encrypt", padx=70,pady=10, command=myClick, bg="grey", fg="#fff")
myButton.place(x=90,y=200)

root.mainloop()