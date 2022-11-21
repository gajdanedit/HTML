import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

for x in range(20):
     t.forward(100)
     t.back(100)
     t.left(18)

t.left(9)
for x in range(5):
     t.penup()
     t.forward(140)
     t.left(135)
     t.pendown()
     for x in range(4):
          t.forward(200)
          t.left(90)
     t.penup()
     t.right(135)
     t.back(140)
     t.left(18)

t.forward(200)
screen.mainloop()