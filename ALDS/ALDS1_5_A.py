import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

# print(n)
# print(a)
# print(q)
# print(m)

s = set()
for i in a:
    lst = list(s)
    for j in lst:
        s.add(i+j)
    s.add(i)
for i in m:
    if i in s:
        print("yes")
    else:
        print("no")
