
import os
from tkinter import *
from tkinter import Tk, simpledialog
from tkinter.filedialog import askdirectory



Tk().withdraw()
path = askdirectory (title = 'Please select a Folder to Bulk Rename contained Files')
walker2 = os.walk(path)


def rename():
    path 
    for count, filename in enumerate (os.listdir(path)):
        dst = f"{path}/{T1.get()}{count}"
        src = f"{path}/{filename}"
        
        os.rename(src,dst)


def OK_button_setup(tk):
    print('OK pressed')
    Button(text = "OK")
    rename()
    exit()
    

def Cancel_button_setup(tk): 
    print ('Cancel pressed')   
    Button (text = "CANCEL")
    exit()


top = Tk()
top.geometry('400x200')
top.title("Enter Desired Name for Files")
B1 = Button(top,text ="OK")
B2 = Button(top,text = "Cancel")
Title =Label(top,text="Enter Name", fg='black')
T1=Entry(top, fg='red', bd=3)
T1.get()
Title.pack(fill=X, padx=10)
T1.pack(fill=X, padx=10)
B1.pack(fill=X, padx=10)
B1.bind("<Button->", OK_button_setup)
B2.pack(fill=X, padx=10)
B2.bind("<Button->", Cancel_button_setup)
top.mainloop()
    