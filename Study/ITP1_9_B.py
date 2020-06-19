while 1:
    S = input()
    if S == "-":
        break
    m = int(input())
    for i in range(m):
        H = int(input())
        S = S[H:] + S[:H]
    print(S)
