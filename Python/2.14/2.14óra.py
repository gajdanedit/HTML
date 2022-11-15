jelenlegi_ido = 14
csengetesi_ido = 51

for i in range (0, csengetesi_ido):
     if jelenlegi_ido == 23:
          jelenlegi_ido = 0
     else: jelenlegi_ido += 1
print("Az óra", jelenlegi_ido, 'órakor fog csengetni')