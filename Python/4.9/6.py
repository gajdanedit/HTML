import turtle
def poligon_rajzolas(t, sz):
     n = 360/sz
     for x in range(int(n)):
          t.forward(50)
          t.left(sz)
screen = turtle.Screen()
t = turtle.Turtle()
poligon_rajzolas(t, 120)
screen.mainloop()