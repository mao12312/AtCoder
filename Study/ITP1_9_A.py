w = input()
T = []
c = 0
while True:
    t = input()
    if t == "END_OF_TEXT":
        break
    T.append(t.split())

for t in T:
    for i in t:
        if i.lower() == w:
            c += 1
print(c)
