#https://www.acmicpc.net/problem/20955
#백준 20955번 민서의 응급 수술(MST,크루스컬)
#import sys
#input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [i for i in range(n)]
result = 0
cnt = n-1
for _ in range(m):
    a,b = map(int, input().split())
    if find_parent(parent,a-1) != find_parent(parent, b-1):
        union_parent(parent, a-1, b-1)
        cnt-=1
    else:
        result+=1
        
print(result+cnt)