C, R = map(int, input().split())
T = [[0]*(R+1) for i in range(C+1)]

for row in range(C):
    work = list(map(int,input().split()))
    for column in range(R):
        T[row][column] = work[column]


