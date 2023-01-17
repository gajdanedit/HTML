# 1. feladat

a = int(input("A:"))
b = int(input("B:"))

if a < 0 and b < 0:
    print("Mindkét szám negatív")
elif a > 0 and b >= 0:
    print("Mindkét szám pozitív")
elif a < 0:
    print("Az első szám negatív")
elif b < 0:
    print("Az második szám negatív")


# 2. feladat

def HoE():
    b = False
    if a > 150:
        b = True
    return b
while(cim!=""):
    cim = input("Cím:")
    oldal = int(input("Oldalak"))
    old = HoE(oldal)
    if old:
        print("A könyv hosszú!")
    else:
        print("A könyv rövid!")
    cim = input("cim:")
