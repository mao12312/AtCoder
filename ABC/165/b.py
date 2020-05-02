import math
x = int(input())
m = 100
y = 0

while m < x:
    m = math.floor(m*1.01)
    y += 1
print(y)
