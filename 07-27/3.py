#https://www.acmicpc.net/problem/15685
#백준 15685번 드래곤 커브 (구현,시뮬레이션)
#import sys
#ipnut = sys.stdin.readline

n = int(input())
direction = [(0,1),(-1,0),(0,-1),(1,0)]
board = [[0]*101 for _ in range(101)]

for i in range(n):
    y,x,d,g = map(int, input().split())
    board[x][y] = 1
    ways = [d]
    temp = [d]
    for _ in range(g+1):
        for idx in temp:
            x += direction[idx][0]
            y += direction[idx][1]
            board[x][y] = 1
        temp = [(way+1)%4 for way in ways]
        temp.reverse()
        ways += temp
        
result = 0 
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            result += 1
print(result)
'''
방향이 0 인 드래곤 커브의 세대별 방향 정보 규칙

0세대 : 0

1세대 : 0 1

2세대 : 0 1 2 1

3세대 : 0 1 2 1 2 3 2 1

4세대 : 0 1 2 1 2 3 2 1 2 3 0 3 2 3 2 1

즉, 그 전 세대의 reverse로 +1 씩 증가하는 형태이다.
'''