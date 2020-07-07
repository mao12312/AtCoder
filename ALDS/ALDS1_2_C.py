def BubbleSort(C, n):
    for i in range(n):
        for j in range(n-1, i+1, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                C[j], C[j-1] = C[j-1], C[j]
    return C


n = int(input())
C = list(input().split())

print(BubbleSort(C, n))
