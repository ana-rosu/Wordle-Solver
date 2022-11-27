from tkinter import *
from tkinter.ttk import *
import random
import subprocess
import sys
import os
from functions import remove_word1, remove_word2, remove_word0


cuvinte = set(open('cuvinte_wordle.txt').read().split('\n'))
cuvant = random.choice(open('cuvinte_wordle.txt').read().split('\n'))
cnt = 0

root = Tk()
root.title('Wordle')
root.geometry('632x800')



GREEN = '#6baa64'
YELLOW = '#c9b459'
WHITE = '#f9fdfa'
GREY = '#787c7f'
BLACK = '#000000'


root.config(bg=BLACK)
root.grid_columnconfigure(5, weight=0)
root.grid_rowconfigure(8, weight=1)
label = Label(root, text='   W O R D L E   ', background=BLACK, foreground = WHITE, font=('Clear Sans', 65, 'bold', 'underline'))
label.place(x=-5, y=0)
root.rowconfigure(0, minsize=105)


def update():
    root.destroy()
    os.system('interface.py')

while True:
    f2 = open('communication.txt', 'r')
    if cnt == 0:
        guess = 'TAREI'
    else:
        guess = f2.read()
    cnt += 1
    if cuvant == guess:
        open('communication.txt', 'w')
        for i, litera in enumerate(guess):
            Label(root, text=f' {litera} ', background=GREEN, anchor=CENTER, foreground=WHITE, font=('Clear Sans', 65, 'bold')).grid(row=cnt+1, column=i, sticky='ew', padx=4 ,pady=4)
        break
    for i, litera in enumerate(guess):
        if litera == cuvant[i]:
            remove_word2(cuvinte, litera, i)
            Label(root, text=f' {litera} ', background=GREEN, anchor=CENTER, foreground=WHITE, font=('Clear Sans', 65, 'bold')).grid(row=cnt+1, column=i, sticky='ew', padx=4 ,pady=4)
        elif cuvant.find(litera) != -1:
            remove_word1(cuvinte, litera, i)
            Label(root, text=f' {litera} ', background=YELLOW, anchor=CENTER, foreground=WHITE, font=('Clear Sans', 65, 'bold')).grid(row=cnt+1, column=i, sticky='ew', padx=4 ,pady=4)
        else:
            remove_word0(cuvinte, litera)
            Label(root, text=f' {litera} ', background=GREY, anchor=CENTER, foreground=WHITE, font=('Clear Sans', 65, 'bold')).grid(row=cnt+1, column=i, sticky='ew', padx=4 ,pady=4)
    f2 = open('communication.txt', 'w')
    f2.writelines("\n".join(cuvinte))
    f2.close()
    subprocess.call([sys.executable, './solver.py'])

for i in range(5):
    root.columnconfigure(i,minsize=125)
button = Button(root, text = 'Another Word', command = lambda:update())
button.grid(row=8, column=2)
root.resizable(False, True)
root.mainloop()
