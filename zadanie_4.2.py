plik = open('./dane/odbiorcy.txt')
tekst = plik.readlines()
plik.close()
zbior = set()
tab_linie = []

for linia in tekst:
    tab_linie.append(linia.strip())
for i in range(1,1025):
    zbior.add(i)


for linia in tab_linie:
    print(int(linia))
    zbior.add(int(linia))
    zbior.remove(int(linia))

print(len(zbior))