plik = open('./dane/odbiorcy_przyklad.txt')
tekst = plik.readlines()
plik.close()
zbior = set()
tab_linie = []
slownik_adresacja = dict()
for linia in tekst:
    tab_linie.append(int(linia.strip()))

for i in range(1,len(tab_linie)+1):
    slownik_adresacja[i] = tab_linie[i-1]

slownik_droga = dict()
flaga = True
for i in range(1,len(tab_linie)+1):
    slownik_droga[i] = slownik_adresacja[i] #Pierwsze przejście
    if slownik_droga[i] == i:
        print(1)
        flaga = False
tab = []

maks = 0
for i in slownik_droga:
    if i > maks:
        maks = i
tab.append(maks)
nr_rundy = 1
while nr_rundy<9:
    nr_rundy+=1
    for i in range(1, len(tab_linie) + 1):
        slownik_droga[i] = slownik_adresacja[slownik_droga[i]]
        if nr_rundy == 2 or nr_rundy == 4 or nr_rundy == 8:
            slownik_tmp = dict()
            for k in range(1,len(tab_linie)+1):
                slownik_tmp[k] = 0
            for j in slownik_droga:
                slownik_tmp[slownik_droga[j]] = slownik_tmp[slownik_droga[j]] + 1
            maks = 0
            for j in slownik_droga:
                if slownik_tmp[j] > maks:
                    maks = slownik_tmp[j]
            tab.append(maks)

print(tab[0],tab[1],tab[2],tab[4])

