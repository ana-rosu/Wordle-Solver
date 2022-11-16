import random
import colorama
from colorama import Back, Fore
colorama.init(autoreset=True)
cuvinte = open("cuvinte_wordle.txt")
cuvant = random.choice(cuvinte.read().split())
#cuvant = 'DELIA'
L = [0] * 5
while True:
    guess = input("Dati cuvant: ")
    if cuvant == guess:
        print('Solved')
        break
    for i, litera in enumerate(guess):
        if litera == cuvant[i]:
            #print(f'{Fore.BLACK}{Back.GREEN}{litera}', end='')
            L[i] = 2
        elif cuvant.find(litera) != -1:
            #print(f'{Fore.BLACK}{Back.YELLOW}{litera}', end='')
            L[i] = 1
        else:
            #print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX}{litera}', end='')
            L[i] = 0
    print()
