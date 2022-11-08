import shutil

permutari = open('permutari.txt')
def remove_word(file,cuv,i):
    for line in file:
        if cuv[i] in line:
            yield line
def parcurgere():
    while open('cuvinte_wordle.txt').read():
        cuvinte = open('cuvinte_wordle.txt').read().split()
        for cuv in cuvinte:
            copie = open('copie_cuvinte.txt', 'r+')
            copie.truncate()
            shutil.copyfile('cuvinte_wordle.txt', 'Wordle-Game/copie_cuvinte.txt')
            for cod in permutari.read().split():
                for i,cifra in enumerate(str(cod)):
                    if cifra == 0:
                        remove_word(copie,cuv,i)
                        print('a')
        break

parcurgere()




