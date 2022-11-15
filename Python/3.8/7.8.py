import turtle

screen = turtle.Screen()
szögek = [160, -43, 270, -97, -43, 200, -940, 17,-86]
kalóz = turtle.Turtle()
végsőszög = 0

for szög in szögek:
     turtle.left(szög)
     turtle.forward(100)
     végsőszög = végsőszög + szög

done = True
while done:
     if végsőszög > 360:
          végsőszög = végsőszög - 360
     elif végsőszög < 0:
          végsőszög = végsőszög + 360
     else:
          done = False


print(f"A kalóz {végsőszög} fokba néz.")
