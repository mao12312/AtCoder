# S = {
#     1: {
#         1: [0]*10,
#         2: [0]*10,
#         3: [0]*10
#     },
#     2: {
#         1: [0]*10,
#         2: [0]*10,
#         3: [0]*10
#     },
#     3: {
#         1: [0]*10,
#         2: [0]*10,
#         3: [0]*10,
#     },
#     4: {
#         1: [0]*10,
#         2: [0]*10,
#         3: [0]*10,
#     }
# }
# n = int(input())
# for _ in range(n):
#     b, f, r, v = map(int, input().split())
#     S[b][f][r-1] = v

# for i in [1, 2, 3, 4]:
#     if i != 1:
#         print()
#         print("#"*20, end='')
#     for j in [1, 2, 3]:
#         print()
#         for t in range(10):
#             if i == 4 and j == 3 and t == 9:
#                 print(' %d' % (S[i][j][t]), end='')
#                 print()
#             else:
#                 print(' %d' % (S[i][j][t]), end='')

a = [[10*[0]for _ in[0]*3]for _ in[0]*4]
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    a[b-1][f-1][r-1] += v
for i in range(4):
    for j in range(3):
        print('',*a[i][j])
    if i < 3:
        print('#'*20)