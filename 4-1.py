#https://www.acmicpc.net/problem/16971
#백준 16971번 배열 B의 값 (누적합)
#import sys
#input = sys.stdin.readline
INF = float('inf')

def change(s,e,state):
    if state:
        for j in range(m):
            board[s][j], board[e][j] = board[e][j], board[s][j]
    else:
        for i in range(n):
            board[i][s], board[i][e] = board[i][e], board[i][s]
            
def count():
    total = 0
    for i in range(n-1):
        for j in range(m-1):
            total += board[i][j]+board[i+1][j]+board[i][j+1]+board[i+1][j+1]
    return total

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
rows = [0]*n
colunms = [0]*m
for i in range(n):
    for j in range(m):
        rows[i] += board[i][j]
        colunms[j] += board[i][j]
result = count()
rMin = INF
rIdx = -1
cMin = INF
cIdx = -1

for i in range(1,n-1):
    rows[i] *= 4
    rows[i] -= 2*(board[i][0]+board[i][m-1])
    if rMin > rows[i]:
        rMin = rows[i]
        rIdx = i

for j in range(1,m-1):
    colunms[j] *= 4
    colunms[j] -= 2*(board[0][j]+board[n-1][j])
    if cMin > colunms[j]:
        cMin = colunms[j]
        cIdx = j

change(0,rIdx,1)
result = max(count(),result)
change(0,rIdx,1)
change(n-1,rIdx,1)
result = max(count(),result)
change(n-1,rIdx,1)
change(0,cIdx,0)
result = max(count(),result)
change(0,cIdx,0)
change(m-1,cIdx,0)
result = max(count(),result)
change(m-1,cIdx,0)

print(result)