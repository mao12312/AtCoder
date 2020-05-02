import math
a, b, n = map(int, input().split())
x = 0
for i in range(0, n+1):
    c = math.floor(a*i/b)-a*math.floor(i/b)
    if x < c :
        x = c
print(x)
# timeout
