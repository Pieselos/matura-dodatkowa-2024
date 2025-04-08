plik = open('./dane/slowa.txt')
tekst = plik.readlines()
plik.close()
licznik = 0
for linia in tekst:
    for i in range(0,len(linia)-2):
        if linia[i]=='k' :
            if linia[i+2] == 't':
                licznik+=1

print(licznik)