xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in xs:
     if x > 90:
          print("Jeles")
     elif x <= 90 and x >= 80:
          print("Jó")
     elif x < 80 and x >= 70:
          print("Közepes")
     elif x < 70 and x >= 60:
          print("Elégséges")
     elif x < 60:
          print("Elégtelen")
          