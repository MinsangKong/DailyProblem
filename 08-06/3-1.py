#https://www.acmicpc.net/problem/15683
#백준 15683번 감시 (DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(idx):
    global result
    if idx == len(cctv):
        num = count()
        if result > num:
            result = num
        return
    x,y,value,way = cctv[idx]
    for j in range(4):
        if j >= 2 and (value == 2 or value == 5):
            break
        for i in range(len(way)):
            way[i] = (way[i]+1)%4
        for i in range(len(way)):
            nx = x + direction[way[i]][0]
            ny = y + direction[way[i]][1]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6 :
                    break
                else:
                    if board[nx][ny] == 0 :
                        board[nx][ny] = 7
                    elif board[nx][ny] >= 7:
                        board[nx][ny] += 1
                    nx += direction[way[i]][0]
                    ny += direction[way[i]][1]
        dfs(idx+1)
        for i in range(len(way)):
            nx = x + direction[way[i]][0]
            ny = y + direction[way[i]][1]
            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6 :
                    break
                else:
                    if board[nx][ny] >= 7 :
                        if board[nx][ny] == 7 :
                            board[nx][ny] = 0
                        else:
                            board[nx][ny] -= 1
                    nx += direction[way[i]][0]
                    ny += direction[way[i]][1]

def count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 :
                cnt += 1
    return cnt

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(0,1),(1,0),(0,-1),(-1,0)]
rotation = {1:[0], 2:[0,2],3:[0,3],4:[0,2,3],5:[0,1,2,3]}

cctv = []


for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6 :
            cctv.append((i,j,board[i][j],rotation[board[i][j]]))
if cctv :
    result = int(1e9)
    dfs(0)
    print(result)
else:
    print(count())
#속도 효율 높이기 위해서는 매번 세주지 말고 set을 활용하면 더 빠르게 처리할 수 있었다
import sys