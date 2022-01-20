#https://www.acmicpc.net/problem/14621
#백준 14621번 나만 안되는 연애 (MST, 크루스컬)
#import sys
#input = sys.stdin.readline
def find_parent(parent, x):
    if parent[x] != x:
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
sexes = list(input().split())
parent = [i for i in range(n)]

graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([c,a-1,b-1])
    
graph.sort()

result = 0
cnt = 0
for edge in graph:
    cost, s, e = edge
    if sexes[s] !=  sexes[e] and find_parent(parent, s) != find_parent(parent, e) :
        union_parent(parent, s, e)
        result += cost
        cnt+=1
    if cnt == n-1 :
        break
if cnt == n-1:
    print(result)
else:
    print(-1)