def potega(a,n):
    pot = 1
    for i in range(0,n):
        pot*=a
    return pot

def prawy_dolny(w,k,n):
    binar = 0
    mnoznik = 0
    while n>0:
        reszta = n%2
        binar+=reszta*potega(10,mnoznik)
        mnoznik+=1
        n = n//2
    print(binar)
    print(mnoznik)
    dlugosc_tablicy = w*k
    for i in range(0,dlugosc_tablicy):
        if i == 9:
            return


prawy_dolny(4,5,179)