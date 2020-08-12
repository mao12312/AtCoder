n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def binarySearch(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


ans = []
for j in range(q):
    if binarySearch(S, T[j]) > -1:
        ans.append(binarySearch(S, T[j]))
print(len(ans))
