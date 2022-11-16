import threading as th
from math import log

permutari_fisier = open('permutari.txt')
permutari_lista = set(permutari_fisier.read().split('\n'))
cuvinte = set(open('cuvinte_wordle.txt').read().split())



def remove_word0(multime, ch):
    for el in multime.copy():
        if ch in el:
            multime.remove(el)


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


def parcurgere(nr):
    max = 0
    f = open('cuvinte_wordle.txt')
    if nr == 0:
        cuvinte = set(f.read(8592).split('\n'))
        cuvinte.discard('')
    elif nr != 0:
        f.read(8592*nr)
        cuvinte = set(f.read(8592).split('\n'))
        cuvinte.discard('')
    for cuv in cuvinte:
        prob = []
        for cod in permutari_lista:
            copie = cuvinte.intersection()
            n = len(copie)
            for i, cifra in enumerate(cod):
                if cifra == '0':
                    remove_word0(copie, cuv[i])
                if cifra == '2':
                    remove_word2(copie, cuv[i], i)
                if cifra == '1':
                    remove_word1(copie, cuv[i], i)
            ramase = len(copie)
            prob.append(ramase / n)
        ent = (entropy1(prob))
        #print(ent, cuv, sep = '\n')
        if ent > max:
            max = ent
            guess = cuv
    maxime.append(max)
    ghiciri.append(cuv)


maxime=[]
ghiciri=[]
t1 = th.Thread(target = parcurgere, args=(0,))
t2 = th.Thread(target = parcurgere, args=(1,))
t3 = th.Thread(target = parcurgere, args=(2,))
t4 = th.Thread(target = parcurgere, args=(3,))
t5 = th.Thread(target = parcurgere, args=(4,))
t6 = th.Thread(target = parcurgere, args=(5,))
t7 = th.Thread(target = parcurgere, args=(6,))
t8 = th.Thread(target = parcurgere, args=(7,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

print(ghiciri[maxime[max(maxime)]], max(maxime))  #list indices must be integers or slices, not float - de reparat
