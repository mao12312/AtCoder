# # my answer
# import math
# a, b, n = map(int, input().split())
# x = 0
# for i in range(0, n+1):
#     c = math.floor(a*i/b)-a*math.floor(i/b)
#     if x < c :
#         x = c
# print(x)
# timeout O(N)

#
a, b, n = map(int, input().split())
x = min(b-1, n)
ans = (a*x//b)-a*(x//b)
print(ans)
# O(1) sugoi
# ref: https://drken1215.hatenablog.com/entry/2020/05/02/225600
