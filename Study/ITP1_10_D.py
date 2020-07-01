n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(sum([abs(x[i] - y[i]) for i in range(n)]))
print(pow(sum([(x[i] - y[i]) ** 2 for i in range(n)]), 1/2))
print(pow(sum([abs(x[i] - y[i]) ** 3 for i in range(n)]), 1/3))
print(max([abs(x[i] - y[i]) for i in range(n)]))
