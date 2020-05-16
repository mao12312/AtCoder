grade = []
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        grade.append("F")
    elif m + f >= 80:
        grade.append("A")
    elif 65 <= m + f < 80:
        grade.append("B")
    elif 50 <= m + f < 65:
        grade.append("C")
    elif 30 <= m + f < 50:
        if r >= 50:
            grade.append("C")
        else:
            grade.append("D")
    elif m + f < 30:
        grade.append("F")
for i in grade:
    print(i)
