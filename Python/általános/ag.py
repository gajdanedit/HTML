# 1. feladat
"""a = int(input("Szám: "))
b = int(input("Szám: "))
if a > b:
    print(a, "nagyobb, mint", b)
elif a < b:
    print(a, "nem nagyobb, mint", b)
else:
    print("a két szám egyforma")
"""
# 2. feladat
"""def MagasE(mag):
    if mag>170:
        return True
    else:
        return False

nev = input("Név: ")
while(nev!=""):
    m = int(input("Magasság: "))
    if MagasE(m):
        print(nev, "magasabb, mint az átlag!")
    else:
        print(nev, "nem magasabb, mint az átlag!")
    nev = input("Név: ")
"""

# 3. feladat
import random

class Szere:
    def __init__(self,nev,nem,fog,szam):
        self.nev = nev
        self.fog = fog
        self.nem = nem
        self.szam = szam
    
    def FvN(nem):
        if nem == "f":
            return "férfi"
        elif nem == "n":
            return "nő"

t = []
for x in range(3):
    a = input("Add meg a nevet! ")
    b = input("Add meg a foglalkozást! ")
    c = input("Add meg a nemet (f/n)!")
    d = random.randint(1,50)
    Szere(a,b,c,d)
    t.append(Szere(a,b,c,d))
for x in range(3):
    print(t[x].nev,"")
