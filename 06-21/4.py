import sys
input = sys.stdin.readline

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
        
n = int(input())

length = 0
edges = []
parent = [i for i in range(n)]

for i in range(n):
    data = input().rstrip()
    for j in range(n):
        if ord('a') <= ord(data[j]) <= ord('z'):
            weight = ord(data[j]) - ord('a') + 1
        elif ord('A') <= ord(data[j]) <= ord('Z'):
            weight = ord(data[j]) - ord('A') + 27
        else:
            weight = 0
                
        if weight != 0:
            edges.append((weight,i,j))
            length += weight
                
edges.sort(key = lambda x : x[0])

cnt = 1
total = 0
for cost, i, j in edges:
    if find_parent(parent,i) != find_parent(parent,j):
        cnt+=1
        union_parent(parent, i, j)
        total+=cost
    if cnt == n:
        break

if cnt == n:
    print(length-total)
else:
    print(-1)