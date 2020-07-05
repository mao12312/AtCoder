# O(n2)
# n = int(input())
# p = []
# c = []
# for i in range(n):
#     p.append(int(input()))

# for i in range(n):
#     for j in p[i+1:]:
#         c.append(j - p[i])
# print(max(c))

# O(1)
n = int(input())
p = [int(input()) for i in range(n)]
minv = p[0]
maxv = p[1] - p[0]
for i in range(1,n):
    maxv = max(p[i] - minv,maxv)
    minv = min(minv,p[i])
print(maxv)