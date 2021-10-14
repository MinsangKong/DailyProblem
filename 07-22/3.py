#https://www.acmicpc.net/problem/5014
#백준 5014번 스타트링크(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [-1]*(f+1)
    visited[s] = 0
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        
        if now == g :
            return visited[now]
        
        for way in direction:
            total = way+now
            if 0 < total <= f :
                if visited[total] == -1:
                    visited[total] = visited[now]+1
                    q.append(total)
    return "use the stairs"

f,s,g,u,d = map(int, input().split())

elevator = [0]*(f+1)
direction = [u,-d]

print(bfs())