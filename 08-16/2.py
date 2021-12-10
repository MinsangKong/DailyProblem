#https://www.acmicpc.net/problem/20207
#백준 20207번 달력 (누적합)
#import sys
#input = sys.stdin.readline

n = int(input())
date = [0]*367

for _ in range(n):
    s,e = map(int, input().split())
    date[s] += 1
    date[e+1] -= 1
    
for i in range(1,367):
    date[i] += date[i-1]
    
cnt = 0
s = 0
result = 0

for i in range(1,367):
    if s :
        if not date[i] :
            result += cnt*(i-s)
            s = 0
            cnt = 0
        else:
            cnt = max(cnt, date[i])
    elif date[i] :
        s = i
        cnt = 1

print(result)