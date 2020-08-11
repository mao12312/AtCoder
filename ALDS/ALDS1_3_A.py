arr = list(input().split())
stack = []

for i in arr:
    if i == "+":
        stack.append(stack.pop()+stack.pop())
    elif i == "-":
        stack.append(-(stack.pop()-stack.pop()))
    elif i == "*":
        stack.append(stack.pop()*stack.pop())
    else:
        stack.append(int(i))
print(stack[-1])
