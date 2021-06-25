#https://www.acmicpc.net/problem/2213
#백준 2213번 트리의 독립집합
#import sys
#input = sys.stdin.readline

def dfs(node):
    visited[node] = 1
    dp[node][0] = weights[node] 
    trees[node][0].append(node)
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)
            dp[node][0] += dp[i][1]
            for j in trees[i][1]:
                trees[node][0].append(j)
            if dp[i][0] <= dp[i][1]:
                dp[node][1] += dp[i][1]
                for j in trees[i][1]:
                    trees[node][1].append(j)
            else:
                dp[node][1] += dp[i][0]
                for j in trees[i][0]:
                    trees[node][1].append(j)

n = int(input())

graph = [[] for _ in range(n+1)]

weights = [0]+list(map(int, input().split()))

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0]*(n+1)
dp = [[0]*2 for _ in range(n+1)] #0이면 해당 node 포함, 1이면 해당 node 불포함
trees = [[[],[]] for _ in range(n+1)]

dfs(1)

i = 0 if dp[1][0] >= dp[1][1] else 1
print(dp)
print(dp[1][i])
result = trees[1][i]
print(*sorted(result))