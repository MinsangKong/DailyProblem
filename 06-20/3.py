#https://www.acmicpc.net/problem/16398
#백준 16398번 행성 연결(크루스컬, MST)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [i for i in range(n)]

edges = []

for i in range(n):
    info = list(map(int, input().split()))
    for j in range(i+1, n):
        edges.append([info[j],i,j])
            
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+= cost
        
print(result)