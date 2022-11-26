import threading as th
from math import log
import time

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


def parcurgere():
    global ghiciri
    # f2 = open('communication.txt', 'r')
    # comunicare = set(f2.read().split('\n'))
    # comunicare.discard('')
    max = 0
    guess = ''
    # if nr == 0:
    #     cuvinte1 = set(f2.read(int(len(comunicare))).split('\n'))
    #     cuvinte1.discard('')
    # elif nr != 0:
    #     f2.read(len(comunicare) * nr)
    #     cuvinte1 = set(f2.read(int(len(comunicare))).split('\n'))
    #     cuvinte1.discard('')

    for cuv in comunicare:
        prob = []
        for cod in coduri_set:
            copie = comunicare.intersection()
            n = len(copie)
            #t = {}
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
        #print(ent, cuv, sep='\n')
        if ent >= max:
            max = ent
            guess = cuv
    ghiciri[max] = guess




f1 = open('coduri.txt')
f2 = open('communication.txt', 'r')
comunicare = set(f2.read().split('\n'))
comunicare.discard('')
coduri_set = set(f1.read().split('\n'))
f1, f2.close()
ghiciri = {}
guess = ''
# t1 = th.Thread(target=parcurgere, args=(0,))
# t2 = th.Thread(target=parcurgere, args=(1,))
# t3 = th.Thread(target=parcurgere, args=(2,))
# t4 = th.Thread(target=parcurgere, args=(3,))
# t5 = th.Thread(target=parcurgere, args=(4,))
# t6 = th.Thread(target=parcurgere, args=(5,))
#
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()
# t6.join()

parcurgere()
f2 = open('communication.txt', 'w')
f2.write(ghiciri[max(ghiciri)])
f2.close()