import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, cnt):
    temp = cnt
    for i in nodes[node]:
        if not visited[i]:
            temp+=1
            result[i][0] = temp
            visited[node] = 1
            temp = dfs(i,temp)
            result[i][1] = temp
    return temp+1

n = int(input())
nodes = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int, input().split()))
    for i in range(1,len(data)-1):
        nodes[data[0]].append(data[i])
        
for i in range(1,n+1):
    nodes[i].sort()
    
root = int(input())
result = [[0,0] for _ in range(n+1)] #left,right
result[root][0] = 1
result[root][1] = n*2
visited = [0]*(n+1)
visited[root] = 1 

dfs(root,1)

for i in range(n):
    print(i+1,result[i+1][0],result[i+1][1])