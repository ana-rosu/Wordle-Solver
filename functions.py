from math import log
import colorama
from colorama import Fore, Back
import subprocess
import sys


def remove_word0(multime, ch):
    for el in multime.copy():
        if ch in el:
            multime.remove(el)


# pastrez doar cuvintele care contin ch pe alta pozitie
def remove_word1(multime, ch, indice):
    for el in multime.copy():
        if ch not in el or (ch in el and ch == el[indice]):
            multime.remove(el)


def remove_word2(multime, ch, indice):
    for el in multime.copy():
        if ch != el[indice]:
            multime.remove(el)


def entropy1(multime):
    # l = [(el * (-math.log2(el)) for el in lista)]
    entropy = 0
    for el in multime:
        if el > 0:
            entropy -= el * log(el, 2)
    return entropy


def solve(cnt):
    # while True:
        global cuvinte, cuvant
        f2 = open('communication.txt', 'r')
        if cnt == 0:
            guess = 'TAREI'
        else:
            guess = f2.read()
        cnt += 1
        if cuvant == guess:
            open('communication.txt', 'w')
            #print(f'{Fore.BLACK}{Back.GREEN}{cuvant}', 'Solved', f'Number of tries: {cnt}', sep='\n')
            return
        for i, litera in enumerate(guess):
            if litera == cuvant[i]:
                #print(f'{Fore.BLACK}{Back.GREEN}{litera}', end='')
                # eliminam toate cuvintele cuv care nu au pe poz i litera
                remove_word2(cuvinte, litera, i)
            elif cuvant.find(litera) != -1:
                #print(f'{Fore.BLACK}{Back.YELLOW}{litera}', end='')
                remove_word1(cuvinte, litera, i)
            else:
                #print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX}{litera}', end='')
                remove_word0(cuvinte, litera)
        #print()
        f2 = open('communication.txt', 'w')
        f2.writelines("\n".join(cuvinte))
        f2.close()
        subprocess.call([sys.executable, 'C:/Users/Flavia/PycharmProjects/Wordle-Solver/solver.py'])
