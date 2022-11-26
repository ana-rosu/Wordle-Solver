import random
import colorama
import subprocess
import sys
from solver import remove_word0, remove_word1, remove_word2
from colorama import Back, Fore
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
        if cuvant == guess:
            open('communication.txt', 'w')
            print(f'{Fore.BLACK}{Back.GREEN}{cuvant}', 'Solved', f'Number of tries: {cnt}', sep='\n')
            break
        for i, litera in enumerate(guess):
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
        print()
        f2 = open('communication.txt', 'w')
        f2.writelines("\n".join(cuvinte))
        f2.close()
        subprocess.call([sys.executable, 'C:/Users/Flavia/PycharmProjects/Wordle-Solver/solver.py'])


cuvinte = set(open('cuvinte_wordle.txt').read().split('\n'))
cuvant = random.choice(open('cuvinte_wordle.txt').read().split('\n'))

print(f'Cuvant de ghicit : {cuvant}')
cnt = 0

solve()
