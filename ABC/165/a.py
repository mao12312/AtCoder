# my answer
k = int(input())
a, b = map(int, input().split())
for i in range(a, b+1):
    if(i % k == 0):
        print("OK")
        break
    elif i == b:
        print("NG")
        break
    else:
        continue

# don't use loop
k = int(input())
a, b = map(int, input().split())
if(a <= b//k*k):
    print('OK')
else:
    print('NG')