from scipy.stats import entropy
import math
permutari_fisier = open('permutari.txt')
permutari_lista = permutari_fisier.read().split()
cuvinte = open('cuvinte_wordle.txt').read().split() #lista
cuvinte2 = cuvinte.copy()
def remove_word(lista,ch):
    for el in list(lista):
        if ch in el:
            lista.remove(el)
def entropy1(lista):
    # l = [(el * (-math.log2(el)) for el in lista)]
    l=[]
    for el in lista:
        l.append(el * (-math.log2(el)))
    print(l)
    return sum(l)

def parcurgere():
   # while open('cuvinte_wordle.txt').read():
        max=0
        cuvinte = open('cuvinte_wordle.txt').read().split() #lista
        for cuv in cuvinte:
      #      copie = open('copie_cuvinte.txt').read().split() #lista
          #  copie = []
          #   copie = cuvinte.copy()
            prob = []
            for cod in permutari_lista:
                copie = cuvinte.copy()
                n = len(copie)
                for i, cifra in enumerate(str(cod)):
                    if cifra == '0':
                        remove_word(copie, cuv[i])
                ramase = len(copie)
                prob.append(ramase/n)
            print(entropy(prob, base=2))
            if entropy(prob, base=2) > max:
                max = entropy(prob, base=2)
                guess = cuv

        print(guess)

parcurgere()





