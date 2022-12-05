napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
def nap_nev(n):
     if n >= 0 and n <= 6:
          return napok[n]
     else: return None

print(nap_nev(int(input())))