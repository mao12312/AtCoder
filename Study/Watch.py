t = int(input())
h = t//3600
m = t % 3600//60
s = t % 60
print('{0}:{1}:{2}'.format(h,m,s))