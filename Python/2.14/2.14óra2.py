jelenlegi_ido = int(input("Írd be a jelenlegi időt: "))
csengetesi_ido = int(input("Írd be hány óra múlva jelezzen az óra: "))

for i in range(0, csengetesi_ido):
     if jelenlegi_ido == 23:
          jelenlegi_ido = 0
     else:
          jelenlegi_ido += 1

print("Az óra", jelenlegi_ido, 'órakor fog csengetni')