import turtle

screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("lightgreen")
t.color("pink")
t.pensize(3)

def Négyzet():
     t.pendown()
     for x in range(4):
          t.forward(20)
          t.left(90)

for x in range(5):
     Négyzet()
     t.penup()
     t.forward(40)

screen.mainloop()