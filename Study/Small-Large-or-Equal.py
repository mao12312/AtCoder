a, b = map(int, input().split())
if a < b:
    res = "a < b"
elif a > b:
    res = "a > b"
else:
    res = "a == b"
print(res)
