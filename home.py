from tkinter import *

root = Tk()
root.title("Cryptography")
root.geometry("350x350")

def open_caes():
    import caesar
    root.destroy()
def open_vig():
    import viginere
    root.destroy()
def open_hill():
    import hill
    root.destroy()

caes_but=Button(root,text="Caesar", command=open_caes,width=20, pady=10).place(x=100,y=100)
vig_but=Button(root,text="Vigenere", command=open_vig,width=20, pady=10).place(x=100,y=150)
hill_but=Button(root,text="Hill", command=open_hill,width=20, pady=10).place(x=100,y=200)

root.mainloop()