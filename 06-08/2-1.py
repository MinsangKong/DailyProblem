#https://www.acmicpc.net/problem/14699
#백준 14699번 관악산 등산(백트래킹)
#import sys
#input = sys.stdin.readline
def dfs(x,cnt,result):
    for i in graph[x]:
        if visited[i] == 0 and heights[i] > heights[x]:
            visited[i] = 1
            result = dfs(i,cnt+1,max(result,cnt+1))
            visited[i] = 0
    return result

n,m = map(int, input().split())

heights = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    
for i in range(n):
    visited = [0]*n
    visited[i] = 1
    print(dfs(i,1,1))
'''
백 트래킹을 해서 해결 할 경우 시간초과 발생
'''