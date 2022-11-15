import threading
from math import log

permutari_fisier = open('permutari.txt')
permutari_lista = set(permutari_fisier.read().split('\n'))
cuvinte = set(open('cuvinte_wordle.txt').read().split())



def remove_word0(multime, ch):
    for el in set(multime):
        if ch in el:
            multime.remove(el)


def remove_word1(multime, ch, indice):
    for el in set(multime):
        if ch in el and ch != el[indice]:
            multime.remove(el)


def remove_word2(multime, ch, indice):
    for el in set(multime):
        if ch not in el and ch == el[indice]:
            multime.remove(el)


def entropy1(multime):
    # l = [(el * (-math.log2(el)) for el in lista)]
    entropy = 0
    for el in multime:
        entropy -= el * log(el, 2)
    return entropy


def parcurgere():
    max = 0
    f = open('cuvinte_wordle.txt')
    cuvinte = set(f.read().split('\n'))
    for cuv in cuvinte:
        prob = []
        for cod in permutari_lista:
            copie = cuvinte.intersection()
            n = len(copie)
            for i, cifra in enumerate(cod):
                if cifra == '0':
                    remove_word0(copie, cuv[i])
                #if cifra == '2':
                #    remove_word2(copie, cuv[i], i)
                #if cifra == '1':
                #    remove_word1(copie, cuv[i], i)
            ramase = len(copie)
            prob.append(ramase / n)
        ent = (entropy1(prob))
        print(prob, ent, cuv, sep = '\n')
        if ent > max:
            max = ent
            guess = cuv
        break

    #print(guess)

parcurgere()
