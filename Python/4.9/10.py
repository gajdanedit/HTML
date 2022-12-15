import turtle

class Csillagok:
     def kis_csillag(t):
          for x in range(5):
               t.forward(100)
               t.left(144)
     
     def nagy_csillag(t):
          for x in range(5):
               t.pendown()
               Csillagok.kis_csillag(t)
               t.penup()
               t.forward(650)
               t.left(144)

screen = turtle.Screen()
t = turtle.Turtle()

Csillagok.nagy_csillag(t)
screen.mainloop()