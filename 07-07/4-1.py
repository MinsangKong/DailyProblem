#https://www.acmicpc.net/problem/20010
#백준 20010번 악덕 영주 혜유(MST)
#import sys
#input = sys.stdin.readline
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

for cost,s,e in graph:
    if find_parent(parent,s) != find_parent(parent,e):
        union_parent(parent, s, e)
        cnt += 1
        total += cost
        
    if cnt == n-1:
        break
        
print(total)
print(total-graph[0][0])
# 평범한 크루스컬로는 풀 수 없는 문제, 최악의 경로는 경우의 수가 다양하다.