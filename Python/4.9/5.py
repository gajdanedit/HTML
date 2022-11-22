import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
hossz = 1
t.penup()
t.goto(-300,0)
t.pendown()

for  x in range(100):
     t.forward(hossz)
     t.right(90)
     hossz += 1
t.penup()
t.goto(300,0)
t.pendown()

hossz = 1
szog = 91
for x in range(100):
     t.forward(hossz)
     t.left(szog)
     hossz += 1
     

screen.mainloop()