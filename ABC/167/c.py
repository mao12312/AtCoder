# bit全探索
import itertools
import numpy as np

N, M, X = map(int, input().split())
CAs = [list(map(int, input().split())) for i in range(N)]

Cs = [ca[0] for ca in CAs]
As = [ca[1:] for ca in CAs]

ans = -1
for i in range(1 << N):
    t = [0]*M
    c = 0
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        c += Cs[j]
        for k in range(M):
            t[k] += As[j][k]
    if all(x >= X for x in t):
        if ans == -1:
            ans = c
        else:
            ans = min(ans, c)
print(ans)
