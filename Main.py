
import os
from tkinter import Tk, simpledialog
from tkinter.filedialog import askdirectory


Tk().withdraw()

path = askdirectory (title = 'Please select a files to Bulk Rename')
walker2 = os.walk(path)
 
user_input = simpledialog.askstring(title ='Enter Name for Files', prompt ='Files will be named:')

def rename():
    path 
    for count, filename in enumerate (os.listdir(path)):
        dst = f"{path}/{user_input}{count}"
        src = f"{path}/{filename}"
        
        os.rename(src,dst)


if __name__ == '__main__':
    rename()

    ## need to make cancel button exit () code , not tkinter mainloop.