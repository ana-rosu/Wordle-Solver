from functions import *
import colorama
from colorama import Fore, Back
import subprocess
import sys
colorama.init(autoreset=True)


def solve():
    while True:
        global cnt
        f2 = open('communication.txt', 'r')
        if cnt == 0:
            guess = 'TAREI'
        else:
            guess = f2.read()
        cnt += 1
        solutions[cuvant].append(guess)
        if cuvant == guess:
            open('communication.txt', 'w')
            print(f'{Fore.BLACK}{Back.GREEN}{cuvant}', 'Solved', f'Number of tries: {cnt}', sep='\n')
            return
        for i, litera in enumerate(guess):
            try:
                if litera == cuvant[i]:
                    print(f'{Fore.BLACK}{Back.GREEN}{litera}', end='')
                    # eliminam toate cuvintele cuv care nu au pe poz i litera
                    remove_word2(cuvinte, litera, i)
                elif cuvant.find(litera) != -1:
                    print(f'{Fore.BLACK}{Back.YELLOW}{litera}', end='')
                    remove_word1(cuvinte, litera, i)
                else:
                    print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX}{litera}', end='')
                    remove_word0(cuvinte, litera)
            except:
                pass
        print()
        f2 = open('communication.txt', 'w')
        f2.writelines("\n".join(cuvinte))
        f2.close()
        subprocess.call([sys.executable, 'C:/Users/Flavia/PycharmProjects/Wordle-Solver/solver.py'])

copie = open('cuvinte_wordle.txt').read().split('\n')
solutii = open('solutii.txt','w')
solutions = {}
total_incercari = 0
incercari = {}
for cuvant in copie:
    cnt = 0
    cuvinte = open('cuvinte_wordle.txt').read().split('\n')
    solutions[cuvant] = []
    solve()
    incercari[cuvant] = cnt
    total_incercari += cnt

for key, value in solutions.items():
    value = ', '.join(map(str, value))
    solutii.write(f'{key} : {value}\n')
solutii.write(f'Incercari medii : {total_incercari/len(copie)}')
