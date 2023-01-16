class Konyv:
    def __init__(self,cim,olldal,mufaj):
        self.cim = cim
        self.oldal = olldal
        self.mufaj = mufaj 

print("könyvbebevő")
a = Konyv(input("Cim:"),int(input("Oldalak: ")),input("Mufaj: "))

print(a.cim)
print(a.cioldal)
print(a.mufaj)
