#https://www.acmicpc.net/problem/2637
#백준 2637번 장난감 조립(위상정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
result = [0]*(n+1)

for _ in range(m):
    x,y,k = map(int, input().split())
    graph[x].append([y,k])
    indegree[y] += 1

q = [n]
result[n] = 1

while q:
    now = q.pop()
    for node,cnt in graph[now]:
        indegree[node] -= 1
        result[node] += result[now]*cnt
        if not indegree[node]:
            q.append(node)
            
for i in range(1,n+1):
    if not graph[i]:
        print(i, result[i])
        
'''
또 dfs로 처리해서 시간초과 발생...
그렇지만 dfs로 처리해도 문제 없을 것 같았는데 왜 dfs로 처리하면 시간초과인지 모르겠다.
반복된 부분을 dfs로 처리하는 것이 비효율적인걸까?? 
정올에서는 정답처리되는 거 보면 백준 문제인듯
'''