import turtle

screen = turtle.Screen()
t = turtle.Turtle()

hossz = 20
for x in range(5):
     for x in range(4):
          t.forward(hossz)
          t.left(90)
     hossz += 20
     t.penup()
     t.right(90)
     t.forward(10)
     t.right(90)
     t.forward(10)
     t.right(180)
     t.pendown()

screen.mainloop()