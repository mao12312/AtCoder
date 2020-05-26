C, R = map(int, input().split())
T = [[0]*(R+1) for i in range(C+1)]

for row in range(C):
    work = list(map(int, input().split()))
    for col in range(R):
        T[row][col] = work[col]

for row in range(C):
    for col in range(0, R):
        T[row][R] += T[row][col]

for row in range(C):
    for col in range(0, R):
        T[C][col] += T[row][col]

for row in range(C):
    T[C][R] += T[row][R]

for row in T:
    print(*row)

