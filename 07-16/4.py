#https://www.acmicpc.net/problem/11437
#백준 11437번 LCA(LCA, DP)
#import sys
#input = sys.stdin.readline
from collections import deque
from math import log2

def set_parent():
    q = deque()
    q.append(1)
    visited = [0]*(n+1)
    while q:
        now = q.popleft()
        visited[now] = 1
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                parent[node][0] = now # 바로 위의 부모 정보만 갱신
                depth[node] = depth[now]+1
                
    for i in range(1,logN):
        for j in range(1,n+1):
            # parent[j][i-1] = > parent[j][i]의 부모
            # parent[parent[j][i-1]][i-1] => parent[j][i-1]의 부모, parent[j][i]의 2**1의 조상
            # 계속 이런식으로 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i-1]][i-1]
            
def lca(a,b):
    if depth[a] > depth[b]:
        a, b = b, a
    
    for i in range(logN-1,-1,-1):
        # a,b의 깊이를 일치시키는 과정, b의 깊이를 높여 준다
        '''
            만약 max_level이 4라면
             2^4 -> 2^3 -> 2^2 -> 2^1 -> 2^0방식으로 찾아갈텐데
            결국 1, 2, 3, 4, 5 ..., 31까지 모두 찾는 방식과 같아진다.
            예를들어, i가 4일때와 1일때 만족했다 치면
            depth[a] <= depth[ac[b][4]]에 의해
            b = parent[b][4];가 되어 b는 b의 16번째 조상을 보고 있을 것이고
            depth[a] <= depth[parent[b][1]]에 의해(현재 b는 처음 b의 16번째 조상인 b로 바뀌었다.)
            b = parent[b][1];이 되어 b는 b의 2번째 조상을 보게 된다.
            즉, b의 16번째 조상의 2번째 조상을 보는 것이니 b의 18번째 조상을 보게 된다.
        '''
        if depth[b]-depth[a] >= 2**i:
            b = parent[b][i]
            
        #결국 b의 깊이를 높여줬을 때, 서로 일치한다면 a가 b의 조상이므로 a를 반환
    if a == b :
        return a
        
    for i in range(logN-1,-1,-1):
        # 서로 공통조상을 만날 때까지 비교
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]
    
n = int(input())
logN = int(log2(n))+1

parent = [[0]*logN for _ in range(n+1)]
depth = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
set_parent()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))