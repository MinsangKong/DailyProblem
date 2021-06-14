#https://www.acmicpc.net/problem/12893
#백준 12893번 적의적(그래프이론)
#import sys
#input = sys.stdin.readline
from collections import deque

def check():
    visited = [0]*(n+1)
    q = deque()
    while enemy:
        point = enemy.pop()
        if visited[point] != 0:
            continue
        else:
            visited[point] = 1
            q.append(point)
            while q:
                now = q.popleft()
                for i in graph[now]:
                    if visited[i] == 0:
                        visited[i] = -visited[now]
                        q.append(i)
                    elif visited[i] == visited[now]:
                        return False
    return True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
enemy = set()

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    enemy.add(a)
    
if check():
    print(1)
else:
    print(0)