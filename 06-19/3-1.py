#https://www.acmicpc.net/problem/18232
#백준 18232번 텔레포트 정거장(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
INF =int(1e9)

n, m = map(int, input().split())
s, e = map(int, input().split())

teleport = dict()
for _ in range(m):
    a, b = map(int, input().split())
    if a in teleport:
        teleport[a].append(b)
    else:
        teleport[a] = [b]
    if b in teleport:
        teleport[b].append(a)
    else:
        teleport[b] = [a]
dp = [INF]*(n+1)
dp[s] = 0
q = deque()
q.append(s)
while q:
    now = q.popleft()
    if now == e:
        break
    if 1 <= now-1 <= n and dp[now-1] == INF:
        dp[now-1] = dp[now]+1
        q.append(now-1)
    if 1 <= now+1 <= n and dp[now+1] == INF:
        dp[now+1] = dp[now]+1
        q.append(now+1)
    if now in teleport:
        for i in teleport[now]:
            if dp[i] == INF:
                dp[i] = dp[now]+1
                q.append(i)

print(dp[e])