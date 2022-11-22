napok = [ "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap" ]
def melyik_nap(index):
     return napok[index]

indul = int(input("Hanyadik napon indulsz: "))
hazater = int(input("Hanyadik nap után térsz haza: "))

napIndex = (hazater - indul) % 7
print(f"A hazatérés napja: {napok[napIndex]}")