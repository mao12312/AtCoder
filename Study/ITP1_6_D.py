# use numpy
import numpy as np
n, m = map(int, input().split())

A = []
b = []
c = []

# input A
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)
# input b
for _ in range(m):
    b.append(int(input()))
A = np.array(A)
b = np.array(b)

c = np.dot(A, b)

for i in c:
    print(i)


# don't use numpy
n, m = map(int, input().split())

A = []
b = []
c = [0 for i in range(n)]

# input A
for _ in range(n):
    a = list(map(int, input().split()))
    A.append(a)
# input b
for _ in range(m):
    b.append(int(input()))

for i in range(n):
    for j in range(m):
        c[i] += A[i][j]*b[j]
    print(c[i])
