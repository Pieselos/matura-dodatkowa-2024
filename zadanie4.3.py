plik = open('./dane/odbiorcy.txt')
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

nr_rundy = 1
while True:
    if flaga:
        nr_rundy+=1
        for i in range(1, len(tab_linie) + 1):
            slownik_droga[i] = slownik_adresacja[slownik_droga[i]]
            if slownik_droga[i] == i:
                print(nr_rundy,i)
                flaga = False
                break

    else:
        break
