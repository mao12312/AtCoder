# bit全探索
money = 300
item = (("orange", 100), ("apple", 200), ("grape", 300))
n = len(item)
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):
        if (i >> j) & 1:
            bag.append(item[j][0])
            total += item[j][1]
    if total <= money:
        print(total,bag)
