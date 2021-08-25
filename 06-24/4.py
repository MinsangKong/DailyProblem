#https://www.acmicpc.net/problem/1045
#백준 1045번 도로(MST)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
parent = [i for i in range(n)]
result = [0]*n
cnt = 0
edges = []

for i in range(n):
    for j in range(i+1, n):
        if board[i][j] == 'Y':
            if find_parent(parent, i) != find_parent(parent, j):
                result[i]+=1
                result[j]+=1
                union_parent(parent,i,j)
                cnt+=1
            else :
                edges.append([i,j])

if cnt != n-1 or len(edges)+cnt < m:
    print(-1)
else:
    for i in range(m-n+1):
        result[edges[i][0]]+=1
        result[edges[i][1]]+=1
    print(*result)