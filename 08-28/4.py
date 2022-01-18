#https://www.acmicpc.net/problem/13418
#백준 13418번 학교 탐방하기 (유니온 파인드)
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


n, m = map(int, input().split())
graph = []

for _ in range(m+1):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])
    
best = 0
worst = 0
cnt = 0

worst_graph = sorted(graph)
worst_parent = [i for i in range(n+1)]
best_parent = [i for i in range(n+1)]

for i in worst_graph:
    check, a, b = i
    if find_parent(worst_parent,a) != find_parent(worst_parent,b):
        union_parent(worst_parent,a,b)
        cnt += 1
        if check == 0:
            worst+=1
    if cnt == n :
        break
best_graph = worst_graph[::-1]
cnt = 0
for i in best_graph:
    check, a, b = i
    if find_parent(best_parent,a) != find_parent(best_parent, b):
        union_parent(best_parent,a,b)
        cnt += 1
        if check == 0:
            best+=1
    if cnt == n :
        break
            
print(worst**2-best**2)