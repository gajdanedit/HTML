napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

def nap_index(nap):
     nap = nap.lower()
     for x in range(0, len(napok)):
          if nap == napok[x].lower():
               return x
     return None

print(nap_index(input()))