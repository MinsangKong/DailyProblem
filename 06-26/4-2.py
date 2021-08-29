import sys
input = sys.stdin.readline

n = int(input())
parent = [0]*(n+1)
cost = [0]*(n+1)
ind = [0]*(n+1)
for i in range(2,n+1):
    s = input().split()
    cost[i],parent[i] = map(int, s[1:])
    ind[parent[i]] += 1
    if s[0] == 'W': cost[i] = -cost[i]

q = [i for i in range(2,n+1) if ind[i] == 0]
while q:
    cur = q.pop()
    if cost[cur] < 0:
        cost[cur] = 0
    nextNode = parent[cur]
    
    cost[nextNode] += cost[cur]
    ind[nextNode] -= 1
    if ind[nextNode] == 0:
        q += [nextNode]
print(cost[1])