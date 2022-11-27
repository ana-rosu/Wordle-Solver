from tkinter import *
from tkinter.ttk import *
from functions import solve
import random

cuvinte = set(open('cuvinte_wordle.txt').read().split('\n'))
cuvant = random.choice(open('cuvinte_wordle.txt').read().split('\n'))
cnt = 0

root = Tk()
root.title('Wordle')
root.geometry('500x700')


GREEN = '#6baa64'
YELLOW = '#c9b459'
WHITE = '#f9fdfa'
GREY = '#787c7f'
BLACK = '#000000'
width = -5
height = 0
root.config(bg=BLACK)
label = Label(root, text=' W O R D L E ', background = BLACK, foreground = WHITE, anchor=CENTER, font=('Neue Helvetica', 60, 'bold', 'underline')).place(x=-5,y=0)
#label1 = Label(root, text=' '.join(cuvant).upper(), background = BLACK, foreground=WHITE, anchor=CENTER, font=('Neue Helvetica', 60, 'bold')).grid(row=1, column=0)
frame = Frame(root).place(x=500, y=300)




root.resizable(False, False)
root.mainloop()
