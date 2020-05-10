import re
S = input()
T = input()
s = re.compile(r'{0}.'.format(S))

if re.match(s,T):
    print("Yes")
else:
    print("No")
