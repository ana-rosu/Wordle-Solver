from functions import remove_word1, remove_word2, remove_word0, entropy1

def parcurgere():
    global ghiciri
    max = 0
    guess = ''
    for cuv in comunicare:
        prob = []
        for cod in coduri_set:
            copie = comunicare.intersection()
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
parcurgere()
f2 = open('communication.txt', 'w')
f2.write(ghiciri[max(ghiciri)])
f2.close()