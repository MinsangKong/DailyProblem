#https://www.acmicpc.net/problem/20010
#백준 20010번 악덕 영주 혜유()
#import sys
#input = sys.stdin.readline

def dfs(idx,total):
    visited[idx] = 1
    maxCost = total
    for target,cost in distance[idx]:
        if not visited[target]:
            maxCost = max(maxCost, dfs(target, cost+total))
    return maxCost

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c,a,b])
    
graph.sort()
total = 0
cnt = 0
distance = [[] for _ in range(n)]

for cost,s,e in graph:
    if find_parent(parent,s) != find_parent(parent,e):
        union_parent(parent, s, e)
        cnt += 1
        total += cost
        distance[s].append([e,cost])
        distance[e].append([s,cost])
        
    if cnt == n-1:
        break
    
print(distance)
costMax = 0
for i in range(n):
    visited = [0]*n
    costMax = max(costMax, dfs(i,0))
    print(costMax)
    
print(total)
print(costMax)
'''
그림을 그려보면서 풀어본 결과 결과로 얻어낸 최종 그래프를 기준으로 dfs를 돌려
가장 큰 값을 추출하는 방법으로 푸는게 맞았다.
'''