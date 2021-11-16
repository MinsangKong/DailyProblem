#https://www.acmicpc.net/problem/19237
#백준 19237번 어른 상어 (BFS, 구현)
#import sys
#input = sys.stdin.readline

def smell():
    for i in range(n):
        for j in range(n):
            if visited[i][j][0] :
                visited[i][j][1] -= 1
                if not visited[i][j][1]:
                    visited[i][j][0] = 0

n, m, k = map(int, input().split())
board = [list(map(int, input().split() for _ in range(n)))]
result = [[[] for _ in range(n)] for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
sharks = []
direction = {1:(-1,0),2:(1,0),3:(0,-1),4:(0,1)}
start = list(map(int, input().split()))
for i in range(n):
    for j in range(n):
        if board[i][j]:
            result[i][j].append([i,j,board[i][j],start[board[i][j]-1]])
            
prioritys = [[] for _ in range(m+1)]

for i in range(m):
    data = [list(map(int, input().split())) for _ in range(4)]
    prioritys[i+1].append(data)