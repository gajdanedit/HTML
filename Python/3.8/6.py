import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()

def Kiiras(hanyszor, fok):
     screen.clear()
     teknos = turtle.Turtle()
     for i in range(0, hanyszor):
          teknos.left(fok)
          teknos.forward(100)

Kiiras(3,120)
Kiiras(4,90)
Kiiras(6,60)
Kiiras(8,45)

screen.mainloop()