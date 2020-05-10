import random

h = 10
w = 3
arr = [[random.randint(0, 10)] * w for _ in range(h)]

print(arr)
# [[6, 6, 6], [4, 4, 4], [7, 7, 7], [3, 3, 3], [6, 6, 6],[4, 4, 4], [8, 8, 8], [10, 10, 10], [6, 6, 6], [2, 2, 2]]

print(*arr)
# [6, 6, 6][4, 4, 4][7, 7, 7][3, 3, 3][6, 6, 6][4, 4, 4][8, 8, 8][10, 10, 10][6, 6, 6][2, 2, 2]

# 要素の前に空白を挿入
for a in arr:
    print('', *a)
#  7 7 7
#  0 0 0
#  2 2 2
#  5 5 5
#  3 3 3
#  1 1 1
#  7 7 7
#  9 9 9
#  1 1 1
#  1 1 1

# 参考
# https: // note.nkmk.me/python-tuple-list-unpack/
# https: // www.suzu6.net/posts/74-sort-2d-list-print/
