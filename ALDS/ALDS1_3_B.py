import sys
import collections

p_q = collections.deque(maxlen=100000)

n, q = map(int, sys.stdin.readline().split())
# print(n,q)

for i in range(n):
    p_name, r_time = sys.stdin.readline().split()
    p_q.append([p_name, int(r_time)])

print(p_q)

# head, tail = 0


# def empty():
#     return head == tail


# def full():
#     return head == (tail+1) % len()


# def enqueue():
#     if full():
#         return 0
