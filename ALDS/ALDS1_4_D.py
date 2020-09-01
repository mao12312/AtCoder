import sys
n, k = map(int, input().split())
w = [int(sys.stdin.readline()) for _ in range(n)]
l, r = max(w), sum(w)


def ok():
    c = 0
    t = 0
    for j in w:
        t += j
        if t > m:
            t = j
            c += 1
            if c >= k:
                return 0
    return 1


while l < r:
    m = (l+r)//2
    if ok():
        r = m
    else:
        l = m+1
print(r)


# 参考
# http: // www.graco.c.u-tokyo.ac.jp/icpc-challenge/wp-content/uploads/2014/12/2014.pdf
