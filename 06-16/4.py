#https://www.acmicpc.net/problem/1949
#백준 1949번 우수 마을(그래프이론)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node):
    visited[node] = 1
    dp[node][0] = nums[node]
    
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
            dp[node][0] += dp[i][1]
            dp[node][1] += max(dp[i][1],dp[i][0])

n = int(input())
nums = [0]+list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dp = [[0]*2 for _ in range(n+1)] #0이면 해당 마을 포함, 1이면 불포함
visited = [0]*(n+1)

dfs(1)
print(*dp)
print(max(dp[1]))