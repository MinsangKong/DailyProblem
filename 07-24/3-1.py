#https://www.acmicpc.net/problem/19598
#백준 19595번 최소 회의실의 개수 (누적합)
#import sys
#input = sys.stdin.readline

n = int(input())

data = dict()

for _ in range(n):
    a,b = map(int, input().split())
    if a in data :
        data[a] += 1
    else:
        data[a] = 1
    if b in data :
        data[b] -= 1
    else:
        data[b] = -1
        
cnt = 1
prefixsum = 0

for time in sorted(data):
    prefixsum += data[time]
    cnt = max(prefixsum,cnt)

print(cnt)