#https://www.acmicpc.net/problem/4315
#백준 4315번 나무 위의 구슬(DFS,위상정렬)
#import sys
#input = sys.stdin.readline
def dfs(node):
    global result
    if not graph[node]: #leafnode
        balls[parent[node]]+=balls[node]-1 
        result += abs(balls[node]-1)
    else: #parentnode
        for nextnode in graph[node]:
            dfs(nextnode) #자식이 없는 leafnode부터 1씩 맞춰줌
        if parent[node] != -1: #parentnode가 존재하는 경우
            balls[parent[node]] += balls[node]-1
            result += abs(balls[node]-1)

while True:
    n = int(input())
    
    if n == 0:
        break
        
    graph = [[] for _ in range(n+1)]
    parent = [-1]*(n+1)
    balls = [0]*(n+1)
    indegree = [0]*(n+1)
    
    for _ in range(n):
        data = list(map(int, input().split()))
        node = data[0]
        cnt = data[1]
        if data[2] > 0:
            for child in data[3:]:
                graph[node].append(child)
                parent[child] = node
                indegree[child]+=1
        balls[node] = cnt
        
    result = 0
    for i in range(1,n+1):
        if indegree[i] == 0: #부모 노드부터 실행
            dfs(i)
    print(result)