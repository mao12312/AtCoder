import math
a, b, C = map(int, input().split())

S = a * b / 2 * math.sin(math.radians(C))
c = math.sqrt(a ** 2 + b ** 2)
L = a + b + c
h = a*math.tan(math.radians(C))

print(h)
