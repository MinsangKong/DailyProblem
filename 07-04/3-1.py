#https://www.acmicpc.net/problem/14500
#백준 14500번 테트로미노 (부르트포스)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
total = 0

board = [list(map(int, input().split())) for _ in range(n)]

case = [
    [[0,1],[0,2],[0,3]],
    [[1,0],[2,0],[3,0]],

    [[0,1],[1,0],[1,1]],

    [[1,0],[2,0],[2,1]],
    [[1,0],[0,1],[0,2]],
    [[0,1],[1,1],[2,1]],
    [[0,1],[0,2],[-1,2]],
    [[0,1],[1,0],[2,0]],
    [[0,1],[0,2],[1,2]],
    [[1,0],[2,0],[2,-1]],
    [[-1,0],[0,1],[0,2]],

    [[1,0],[1,1],[2,1]],
    [[-1,1],[0,1],[-1,2]],
    [[0,1],[1,1],[1,2]],
    [[1,0],[1,-1],[2,-1]],

    [[1,-1],[1,0],[1,1]],
    [[1,0],[1,1],[2,0]],
    [[0,1],[0,2],[1,1]],
    [[1,0],[1,-1],[2,0]],
]  

for i in range(n):
    for j in range(m):
        for direction in case:
            temp = board[i][j]
            for a,b in direction:
                nx = i+a
                ny = j+b
                if 0 <= nx < n and 0 <= ny < m:
                    temp+= board[nx][ny]
                else:
                    break
            total = max(total, temp)
            
print(total)
#경우의 수를 줄였더니 시간초과 없이 해결됨
#but pypy3같은 경우에는 백트래킹 수준으로 빨랐지만 그냥 파이썬에서는 너무 느렸다.