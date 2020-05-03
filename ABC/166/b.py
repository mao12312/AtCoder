import itertools
N, K = map(int, input().split())
d = [0]*K
a = [0]*K

for i in range(K):
    d[i] = int(input())
    a[i] = list(map(int, input().split()))

menber = list(range(1, N+1))
have_list = list(set(itertools.chain.from_iterable(a)))

res = len(menber) - len(have_list)
print(res)