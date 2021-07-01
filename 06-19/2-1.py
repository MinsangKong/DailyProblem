#https://www.acmicpc.net/problem/10971
#백준 10971번 외판원 순회2(DFS, 백트래킹)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

def dfs(cost, node, idx):
    global result
    if sum(visited) == n :
        if board[node][idx] > 0:
            result = min(cost+board[node][idx],result)
        return
    else:
        for i in range(n):
            if visited[i] == 0 and board[node][i] > 0:
                visited[i] = 1
                dfs(cost+board[node][i],i,idx)
                visited[i] = 0

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

result = INF
for i in range(n):
    visited = [0]*n
    visited[i] = 1
    dfs(0,i,i)
    
print(result)
'''
dfs를 통한 백트래킹 완전 탐색은 python3로는 시간초과 발생
'''