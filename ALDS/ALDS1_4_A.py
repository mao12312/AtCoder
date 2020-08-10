n = int(input())
S = set(input().split())
q = int(input())
T = set(input().split())

print(len(S & T))

# n = int(input())
# S =list(map(int,input().split()))
# q = int(input())
# T =list(map(int,input().split()))

# ans = 0
# countMap = dict()

# ST = S
# ST.extend(T)

# for i in ST:
#     if i in countMap:
#         countMap[i] += 1
#     else:
#         countMap[i] = 1
# for j in countMap:
#     if countMap[j] >= 2:
#         ans += 1

# print(ans)
