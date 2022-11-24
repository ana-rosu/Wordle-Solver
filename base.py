import random
import colorama
from solver import cuvant_optim, remove_word0, remove_word1, remove_word2

from colorama import Back, Fore

colorama.init(autoreset=True)
# f = open('cuvinte_wordle.txt')
cuvinte = set(open('cuvinte_wordle.txt').read().split())
cuvant = random.choice(open('cuvinte_wordle.txt').read().split())
print(cuvant)

L = [0] * 5
# while True:
guess = cuvant_optim
if cuvant == guess:
    print('Solved')
    # break
for i, litera in enumerate(guess):
    if litera == cuvant[i]:
        # print(f'{Fore.BLACK}{Back.GREEN}{litera}', end='')
        #eliminam toate cuvintele cuv care nu au pe poz i litera
        remove_word2(cuvinte, litera, i)
        L[i] = 2
    elif cuvant.find(litera) != -1:
        # print(f'{Fore.BLACK}{Back.YELLOW}{litera}', end='')
        L[i] = 1
        remove_word1(cuvinte, litera, i)
    else:
        # print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX}{litera}', end='')
        L[i] = 0
        remove_word0(cuvinte, litera)

file = open('communication.txt', 'w')
file.writelines("\n".join(cuvinte))
file.close()