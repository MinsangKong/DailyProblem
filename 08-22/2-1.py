#https://www.acmicpc.net/problem/15565
#백준 15565번 귀여운 라이언 (투 포인터)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
items = list(map(int, input().split()))

if k == 1 or n == 1:
    print(-1 if 1 not in items else 1)
else:
    s = 0
    e = 0
    count = [0]*3
    result = INF
    count[items[0]] += 1

    while s <= e :
        e += 1
        if e == n :
            break
        count[items[e]] += 1
        if count[1] == k :
            while count[1] == k :
                count[items[s]] -= 1
                s += 1
            result = min(result, e-s+2)
            
    print(-1 if result == INF else result)   