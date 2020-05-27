while True:
    s = str(input())
    if int(s) == 0 : break
    n = sum([int(i) for i in s])
    print(n)

    