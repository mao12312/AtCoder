n = int(input())
t = 0
h = 0
for i in range(n):
    s = input().split()
    if s[0] < s[1]:
        h += 3
    elif s[0] > s[1]:
        t += 3
    else:
        t += 1
        h += 1
print(t,h)
