def Reverce(S, a, b):
    S[a:b+1] = reversed(S[a:b+1])
    return S[a:b+1]


def Replace(S, a, b, c):
    S[a:b+1] = c[0]
    return S[a:b+1]


S = list(input())
q = int(input())
for i in range(q):
    cmd, a, b, *c = input().split()
    a = int(a)
    b = int(b)
    if cmd == "replace":
        S = Replace(S, a, b, c)
    elif cmd == "reverse":
        S = Reverce(S, a, b)
    else:
        print(*S[a:b+1], sep='')
