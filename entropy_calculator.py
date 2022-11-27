import threading as th
from functions import remove_word1, remove_word2, remove_word0, entropy1

def parcurgere(nr):
    f = open('cuvinte_wordle.txt')
    if nr == 0:
        cuvinte1 = set(f.read(8592).split('\n'))
        cuvinte1.discard('')
    elif nr != 0:
        f.read(8592*nr)
        cuvinte1 = set(f.read(8592).split('\n'))
        cuvinte1.discard('')
    for cuv in cuvinte1:
        prob = []
        for cod in coduri_set:
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
        dict_ent[cuv] = ent


dict_ent = {}
f1 = open('coduri.txt')
f2 = open('cuvinte_wordle.txt')
f3 = open('entropies.txt', 'w')
coduri_set = set(f1.read().split('\n'))
cuvinte = set(f2.read().split())

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

for key, value in sorted(dict_ent.items(), key=lambda dict_ent: dict_ent[1], reverse=True):
    f3.write(f'{key} : {value}\n')
