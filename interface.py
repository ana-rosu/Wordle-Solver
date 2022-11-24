from tkinter import *
from tkinter.ttk import *
import os
def wordle():
    os.system('base.py')
root = Tk()
root.title('Wordle')
root.geometry('500x700')
label = Label(root, text='Wordle', background = '#67c1d5', foreground = 'white',width=87, anchor=CENTER, ).place(x=0, y=0)
frame = Frame(root).place(x=200, y=300)
button = Button(frame, text='START', command= lambda: wordle()).place(x=200,y=300)
frameexit = Frame(root, relief='flat').place(x=420,y=20)
exit = Button(frameexit, text='Quit', command= lambda:root.quit()).place(x=420,y=20)

root.mainloop()
