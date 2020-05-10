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
a,b,c,k = map(int,input().split())
xa = min(a,k)
k -= xa
xb = min(b, k)
k -= xb
xc = k
print(xa-xc)