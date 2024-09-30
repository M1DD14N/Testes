import math
a = 3
b = -2
c = -8

delta = (b**2) - (4 * a * c)

print(b**2)

print(- 4 * a * c)

print("Delta: ", delta)

if delta < 0:
    print("Não tem raiz")
else:
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)
  print("X1: ",round(x1, 2),"\nX2: ",round(x2, 2))
