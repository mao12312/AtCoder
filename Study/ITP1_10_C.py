import statistics
import math

while True:
    n = int(input())
    if n == 0:
        break
    d = list(map(int, input().split()))
    pstdev = statistics.pstdev(d)
    print(pstdev)
