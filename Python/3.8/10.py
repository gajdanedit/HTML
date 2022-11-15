import turtle # behívja a "turtle" könyvtárat

ablak = turtle.Screen() # létre hoz egy kijelzési alapot
Eszti = turtle.Turtle() # létre hoz egy "teknős" ecsetet

Eszti.right(90) # jobbra fordul 90 fokkal
Eszti.left(3600) # balra megfordul 10x
Eszti.right(-90) # balra fordul 90 fokkal
Eszti.speed(10) # 10-esre változik a sebessége
Eszti.left(3600) # balra megfordul 10x csak most gyorsabban
Eszti.speed(0) # megáll
Eszti.left(3645) # 10x megfordulna balra + 45 fokkal balra menne HA TUDNA
Eszti.forward(-100) # hátra menne 10 pixelt HA TUDNA