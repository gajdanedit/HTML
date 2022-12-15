import turtle

def sokszog_rajzolas(t, n, sz):
     for x in range(n):
          t.forward(50)
          t.left(sz)

screen = turtle.Screen()
Eszti = turtle.Turtle()
sokszog_rajzolas(Eszti, 8, 45)
screen.mainloop()