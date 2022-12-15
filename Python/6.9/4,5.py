napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def napok_hozzaadasa(napot,n):
     napot = napot.lower()
     napI = 0
     for x in range(len(napok)):
          if napot == napok[x].lower():
               napI = x
     napI += int(n)
     return napok[napI%7]

print(napok_hozzaadasa(input(), input()))