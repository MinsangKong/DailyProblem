import sys

v = dict()
m = 0
for i in range(int(input())):
    a,b=map(int,sys.stdin.readline().split())
    v[a]=b
    m += b
m/=2
l = sorted(v.keys())

for i in l:
    m -= v[i]
    if m<=0:
        print(i)
        break