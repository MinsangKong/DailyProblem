#https://www.acmicpc.net/problem/20924
#백준 20924번 트리의 기둥과 가지(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
        
def find_rl(root):
    q = deque()
    q.append(root)
    flag = False
    rl = 0
    distLeaf = 0
    distance = [-1]*n
    distance[root] = 0
    while q:
        node = q.popleft()
        if not flag and len(graph[node]) >= 2:
            if node == root or len(graph[node]) >= 3:
                flag = True
                rl = node
        for nextnode,nextdist in graph[node]:
            if distance[nextnode] == -1:
                distance[nextnode] = distance[node]+nextdist
                q.append(nextnode)
            
    for i in range(n):
        distLeaf = max(distLeaf,distance[i]-distance[rl])
    if rl == root:
        if not flag:
            return [distLeaf,0]
        else:
            return [0,distLeaf]
    return [distance[rl],distLeaf]
    
n, r = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
     
result = find_rl(r-1)
print(*result)
'''
문제를 통해서 방향성이 없다는 것을 도출할 수가 없었다.
그래서 엄청 헤메다가 겨우 풀었다... 
'''