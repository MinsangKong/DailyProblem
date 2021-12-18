#https://www.acmicpc.net/problem/2018
#백준 2018번 수들의 합5 (투포인터)
#import sys
#input = sys.stdin.readline

n = int(input())
cnt = 1
s = 1
e = 2
total = s+e

while s < e :
    if total >= n :
        if total == n :
            cnt += 1
        total -= s
        s += 1
    else:
        e += 1
        total += e
print(cnt)  