plik = open('./dane/slowa.txt')
tekst = plik.readlines()
plik.close()
tablica_slowa = []
for linia in tekst:
    tablica_slowa.append(linia.strip())
for linia in tablica_slowa:
    slownik_litery = dict()
    for i in linia:
        slownik_litery[i] = 0

    for i in linia:
        slownik_litery[i] = slownik_litery[i] + 1
        if slownik_litery[i] >= len(linia)/2:
            print(linia)
            break





