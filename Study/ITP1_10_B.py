import math
a, b, C = map(int, input().split())

S = a * b / 2 * math.sin(math.radians(C))
c = math.sqrt(b**2 + a**2 - 2*b*a*math.cos(math.radians(C)))
L = a + b + c
h = S*2/a

print(S, L, h, sep='\n')
