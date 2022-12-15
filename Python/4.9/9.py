import turtle

def csillag(t):
     for x in range(5):
          t.forward(100)
          t.left(144)

screen = turtle.Screen()
t = turtle.Turtle()

csillag(t)

screen.mainloop()