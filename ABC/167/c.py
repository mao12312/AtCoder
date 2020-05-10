# answer
import sys
import numpy as np
import itertools

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

""" Input
S = input().rstrip()
N = int(input())
A = np.array(input().split(), dtype=np.float64)
D = [int(input()) for _ in range(N)]
AB = [[int(x) for x in input().split()] for _ in range(N)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]
"""

N, M, X = map(int, input().split())
algorithm = [0] * M

prices = []
rikai = []
for _ in range(N):
    C, *A = list(map(int, input().split()))
    prices.append(C)
    rikai.append(A)

idx = range(N)

prices_min = 10 ** 12
flag = False

for i, _ in enumerate(idx, 1):
    for candidate in itertools.combinations(idx, r=i):

        total = 0
        for c in candidate:
            c_arr = np.array(rikai[c])
            total += c_arr

        if np.all(total >= X):
            flag = True
            price = 0
            for c in candidate:
                price += prices[c]

            prices_min = min(price, prices_min)


print(prices_min if flag else '-1')
