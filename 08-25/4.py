#https://www.acmicpc.net/problem/15789
#백준 15789번 CTP 왕국은 한솔 왕국을 이길 수 있을까? ()
#import sys
#input = sys.stdin.readline
import heapq

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
        count[b] += count[a]
    else:
        parent[b] = a
        count[a] += count[b]

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
count = [1]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    
c,h,k = map(int, input().split())
    
visited = [0]*(n+1)
ctp = find_parent(parent, c)
visited[ctp] = 1
visited[find_parent(parent, h)] = 1
q = []
result = count[ctp]

for i in range(1,n+1):
    cur = find_parent(parent,i)
    if not visited[cur] :
        heapq.heappush(q,-count[cur])
        visited[cur] = 1
if q :
    while q and k > 0:
        result -= heapq.heappop(q)
        k -= 1
print(result)