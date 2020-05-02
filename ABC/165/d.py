# my answer
import math
a, b, n = map(int, input().split())
x = 0
for i in range(0, n+1):
    c = math.floor(a*i/b)-a*math.floor(i/b)
    if x < c :
        x = c
print(x)
# timeout

# 
a, b, x = map(int, input().split())
if b > x:
    print(a*x//b)
else:
    print(a*(b-1)//b)
