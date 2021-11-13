#https://www.acmicpc.net/problem/19535
#백준 19535번 ㄷㄷㄷㅈ (트리,DFS)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def comb(num):
    c = 1
    for i in range(num,num-3,-1):
        c *= i
    return c//6

def dfs(idx, cnt):
    global dcount
    for node in graph[idx]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, cnt+1)
            if len(graph[idx]) >= 2 and len(graph[node]) >= 2:
                dcount += (len(graph[idx])-1)*(len(graph[node])-1)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
dcount = 0
gcount = 0

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,n+1):
    if len(graph[i]) >= 3 :
        gcount += comb(len(graph[i]))

visited[1] = 1
dfs(1,0)

if dcount == 3*gcount:
    print("DUDUDUNGA")
elif dcount > 3*gcount:
    print("D")
else:
    print("G")
#재귀 방식으로는 아슬아슬하게 통과