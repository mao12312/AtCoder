# # time out
# import sys
# A, B, C, K = map(int, input().split())
# S = {'A': 1, 'B': 0, 'C': -1}
# M = {'A': 0, 'B': 0, 'C': 0}
# while K > 0:
#     if A > 0:
#         K -= 1
#         A -= 1
#         M['A'] += 1
#     elif B > 0:
#         K -= 1
#         B -= 1
#         M['B'] += 1
#     elif C > 0:
#         K -= 1
#         C -= 1
#         M['C'] += 1

# ans = S["A"]*M["A"] + S["B"]*M["B"] + S["C"]*M["C"]
# print(ans)


# answer
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

""" Input
S = input().rstrip()
N = int(input())
N, A, B = map(int, input().split())
A = list(map(int, input().split()))
A = np.array(input().split(), dtype=np.float64)
D = [int(input()) for _ in range(N)]
AB = [[int(x) for x in input().split()] for _ in range(N)]
PX = [[int(x) for x in input().split()] for _ in range(Q)]
"""

A, B, C, K = map(int, input().split())

total = 0
if K >= A:
    total += 1 * A
    K -= A
    if K >= B:
        total += 0 * B
        K -= B
        if K >= C:
            total += (-1) * C
        else:
            total += (-1) * K
    else:
        pass

else:
    total = K * 1

print(total)