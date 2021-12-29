#https://www.acmicpc.net/problem/15831
#백준 15831번 준표의 조약돌 (투 포인터)
#import sys
#input = sys.stdin.readline

n,b,w = map(int, input().split())
load = input().rstrip()
count = {'W' : 0, 'B' : 0}
result = 0

s = 0
e = 0
while e <= n:
    if e == n :
        if count['W'] >= w and count['B'] <= b:
            result = max(result, e-s)
        break
    if count['W'] >= w and count['B'] <= b:
        result = max(result, e-s)
        count[load[e]] += 1
        e += 1
    elif count['W'] < w :
        count[load[e]] += 1
        e += 1
    else :
        count[load[s]] -= 1
        s += 1

print(result)