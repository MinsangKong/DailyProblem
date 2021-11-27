#https://www.acmicpc.net/problem/20364
#백준 20364번 부동산 다툼 (트리)
#import sys
#input = sys.stdin.readline

n, q = map(int, input().split())
visited = [0]*(n+1)

for _ in range(q):
    target = int(input())
    cur = target
    flag = False
    owned = 0
    
    while cur > 1 :
        if visited[cur]:
            flag = True
            owned = cur
        if cur%2 :
            cur -= 1
        cur //= 2
    if flag:
        print(owned)
    else:
        visited[target] = 1
        print(0)