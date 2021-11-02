from sys import stdin, maxsize
input = stdin.readline
INF = maxsize

def floyd(graph, path, n):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j] = k

def find_path(path, i, j, result):
    if path[i][j] == -1:
        return
    
    x = path[i][j]
    find_path(path, i, x, result)
    result.append(x)
    find_path(path, x, j, result)

def solution():
    n = int(input())
    m = int(input())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    path = [[-1] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] > c:
            graph[a][b] = c
    
    floyd(graph, path, n)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] != INF:
                print(graph[i][j], end=" ")
            else:
                print(0, end=" ")
        print()

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or graph[i][j] == INF:
                print(0)
            elif path[i][j] == -1:
                print(2, i, j)
            else:
                result = []
                find_path(path, i, j, result)
                print(len(result) + 2, i, " ".join(map(str, result)), j)

solution()