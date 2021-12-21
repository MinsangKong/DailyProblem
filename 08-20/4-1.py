#https://www.acmicpc.net/problem/16562
#백준 16562번 친구비 (유니온 파인드)
import sys
#input = sys.stdin.readline
import heapq

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
        
def dfs(idx):
    parent[idx] = 0
    q = [idx]
    while q :
        friend = q.pop()
        
        for _next in graph[friend]:
            if find_parent(parent, _next) != 0 :
                parent[_next] = 0
                q.append(_next)

n, m, k = map(int, input().split())
costs = list(map(int, input().split()))
parent = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]
result = 0
q = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(n):
    heapq.heappush(q,[costs[i],i+1])

while q :
    cost, now = heapq.heappop(q)

    if find_parent(parent, now) == 0 :
        continue
    if result + cost > k :
        print("Oh no")
        sys.exit(0)
    result += cost
    dfs(now)
    
print(result)