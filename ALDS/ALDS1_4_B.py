# n = int(input())
# S = list(map(int, input().split()))
# q = int(input())
# T = list(map(int, input().split()))


# def binarySearch(data, value):
#     left = 0
#     right = len(data) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if data[mid] == value:
#             return mid
#         elif data[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


# ans = []
# for j in range(q):
#     if binarySearch(S, T[j]) > -1:
#         ans.append(binarySearch(S, T[j]))
# print(len(ans))
import sys


def s():
    n, k = map(int, input().split())
    w = list(map(int, sys.stdin.readlines()))

    def f():
        c = t = 0
        for j in w:
            t += j
            if t > m:
                t = j
                c += 1
                if c >= k:
                    return 0
        return 1
    l, r = max(w), sum(w)
    while l < r:
        m = (l+r)//2
        if f():
            r = m
        else:
            l = m+1
    print(r)


if'__main__' == __name__:
    s()
