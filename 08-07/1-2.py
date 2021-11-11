from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
event = []
for i in range(m):
    a, b = map(int,input().split())
    event.append((a,1)) # in
    event.append((b,2)) # out
event.sort()

lay = 0
tot = 0
start = -1
for i, ev in event:
    if ev == 1:
        lay+= 1
        if lay == 1: start = i
    else:
        lay-= 1
        if lay == 0: tot+= i-start
print(n-tot)