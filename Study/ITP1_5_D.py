N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 or i % 10 == 3 or str(i).find("3") != -1:
        print(" {}".format(i), end='')
print()