# time out
N, K = map(int, input().split())
T = list(map(int, input().split()))

V = 1
for _ in range(K):
    V = T[V-1]
print(V)
