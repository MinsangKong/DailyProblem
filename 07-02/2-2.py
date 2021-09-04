#https://www.acmicpc.net/problem/14712
#백준 14712번 넴모넴모(Easy) (DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(cnt):
    global result
    for i in range(cnt, n*m):
        x = i // m + 1
        y = i % m + 1

        if board[x-1][y] and board[x][y-1] and board[x-1][y-1]:
            continue
        else:
            result += 1
            board[x][y] = 1
            dfs(i+1)
            board[x][y] = 0

n, m = map(int, input().split())

board = [[0]*(m+1) for _ in range(n+1)]
result = 1

dfs(0)

print(result)
#재귀의 횟수를 줄이고 for문으로 처리하는 방식으로도 시간초과 발생