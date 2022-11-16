# t = [1,3,5,7,"jolán"]
# print(t)
import random
t = []
for i in range(5):
    t.append(random.randint(1,100))
print(t)

összeg = 0
for i in t:
    összeg += i
print(összeg)

# átlagtétel
atl = összeg / len(t)
print(atl)

# Min
min = 101
for i in t:
    if min > i:
        min = i
print(min)

# Max
max =- 1
for i in t:
    if max < i:
        max = i
print(max)

# keresés





