import turtle
screen = turtle.Screen()
t = turtle.Turtle()

def rajzolj_oszlopot(t, magassag):
     t.begin_fill()
     t.left(90)
     t.forward(magassag)
     if magassag < 0:
          t.penup()
          t.forward(-20)
          t.write(" "+ str(magassag))
          t.forward(20)
          t.pendown()
     else:
          t.write(" "+ str(magassag))
     t.right(90)
     t.forward(40)
     t.right(90)
     t.forward(magassag)
     t.left(90)
     t.end_fill()
     t.penup()
     t.forward(10)
     t.pendown()

def szin(t, magassag):
     if magassag > 200:
          t.fillcolor("red")
     elif magassag <= 200 and magassag > 100:
          t.fillcolor("yellow")
     elif magassag <= 100:
          t.fillcolor("green")

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)

xs = [48,117,-67,200,240,-160,110,260,220]

for m in xs:
     szin(Eszti, m)
     rajzolj_oszlopot(Eszti, m)

ablak.mainloop()