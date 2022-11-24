import multiprocessing as mp
import time
from math import log

permutari_set = set(open('coduri.txt').read().split('\n'))
cuvinte = set(open('cuvinte_wordle.txt').read().split())


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


def parcurgere(nr):
    global ghiciri
    max = 0
    f = open('cuvinte_wordle.txt')
    if nr == 0:
        cuvinte1 = set(f.read(8592).split('\n'))
        cuvinte1.discard('')
    elif nr != 0:
        f.read(8592 * nr)
        cuvinte1 = set(f.read(8592).split('\n'))
        cuvinte1.discard('')

    for cuv in cuvinte1:
        prob = []
        for cod in permutari_set:
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
        print(ent, cuv, sep='\n')
        if ent > max:
            max = ent
            guess = cuv
    ghiciri[max] = guess


ghiciri = {}
if __name__ == "__main__":
    p1 = mp.Process(target=parcurgere, args=(0,))
    p2 = mp.Process(target=parcurgere, args=(1,))
    p3 = mp.Process(target=parcurgere, args=(2,))
    p4 = mp.Process(target=parcurgere, args=(3,))
    p5 = mp.Process(target=parcurgere, args=(4,))
    p6 = mp.Process(target=parcurgere, args=(5,))
    p7 = mp.Process(target=parcurgere, args=(6,))
    p8 = mp.Process(target=parcurgere, args=(7,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    end = time.time()
    print(end-start)
    print(max(ghiciri), ghiciri[max(ghiciri)])
# cuvant_optim = 'TAREI'

