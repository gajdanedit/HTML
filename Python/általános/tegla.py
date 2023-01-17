from classes import*

t1 = Teglalap()
t1.SetA(int(input("Írd be a téglalap \"a\" oldalát: ")))
t1.SetB(int(input("Írd be a téglalap \"b\" oldalát: ")))
print("A t1 kerülete: {0}. Területe: {1}".format(t1.GetKerület(), t1.GetTerület()))

n1 = Négyzet()
n1.SetA(int(input("Írd be a négyzet \"a\" oldalát: ")))
print(f"Az n1 kerülete: {n1.GetKerület()}, területe: {n1.GetTerület()}.")