napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]

def melyik_nap(index):
     return napok[index]

napIndex = int(input("Írd be a nap számát: "))
print(melyik_nap(napIndex))