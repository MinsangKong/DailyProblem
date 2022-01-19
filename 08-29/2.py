#https://www.acmicpc.net/problem/13913
#백준 13913번 숨바꼭질 4 (DFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def dfs(n,k):
    visited = [-1]*100001
    visited[n] = 0
    q = deque([n])
    way = dict()
    while q :
        now = q.popleft()
        if now == k :
            result = []
            cur = now
            while True:
                if cur not in way:
                    result.append(cur)
                    break
                else:
                    result.append(cur)
                    cur = way[cur]
            return result[::-1]
        
        if now+1 <= 100000 and visited[now+1] == -1:
            visited[now+1] = visited[now]+1
            way[now+1] = now
            q.append(now+1)
        if now*2 <= 100000 and visited[now*2] == -1 :
            visited[now*2] = visited[now]+1
            way[now*2] = now
            q.append(now*2)
        if now-1 >= 0 and visited[now-1] == -1:
            visited[now-1] = visited[now]+1
            way[now-1] = now
            q.append(now-1)

n, k = map(int, input().split())
answer = dfs(n,k)
print(len(answer)-1)
print(*answer)