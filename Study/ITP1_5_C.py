while True:
    h, w = map(int, input().split())
    if h == 0 or w == 0:
        break
    for i in range(1, h+1):
        if i % 2 == 0:
            for j in range(1, w+1):
                if j % 2 == 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        else:
            for t in range(1, w+1):
                if t % 2 == 0:
                    print(".", end="")
                else:
                    print("#", end="")
            print()
    print()

# good
while True:
    h, w = input().split()
    h, w = int(h), int(w)
    if h+w == 0:
        break
    for i in range(h):
        for j in range(w):
            print('#.'[(i+j) & 1], end='')
        print()
    print()
