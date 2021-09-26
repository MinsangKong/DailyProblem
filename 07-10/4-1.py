#https://www.acmicpc.net/problem/17837
#백준 17837번 새로운 게임 2 (시뮬레이션, BFS)
#import sys
#input = sys.stdin.readline

def move(idx):
    x, y, direct = horses[idx]
    nx = x+direction[direct][0]
    ny = y+direction[direct][1]
    
    if (nx < 0 or nx >= n) or (ny < 0 or ny >= n) or board[nx][ny] == 2 :
        if 0 <= direct <= 1:
            ndir = (direct+1)%2
        else:
            ndir = (direct-1)%2 + 2
        horses[idx][2] = ndir
        nx = x + direction[ndir][0]
        ny = y + direction[ndir][1]
        if (nx < 0 or nx >= n) or (ny < 0 or ny >= n) or board[nx][ny] == 2 :
            return 0
    
    horse_Set = []
    for i, key in enumerate(board_State[x][y]):
        if key == idx:
            horse_Set.extend(board_State[x][y][i:])
            board_State[x][y] = board_State[x][y][:i]
            break
            
    if board[nx][ny] == 1 :
        horse_Set = horse_Set[::-1]
    
    for i in horse_Set:
        board_State[nx][ny].append(i)
        horses[i][0], horses[i][1] = nx, ny
        
    if len(board_State[nx][ny]) >= 4 :
        return 1
    return 0

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_State = [[[] for _ in range(n)] for _ in range(n)]
horses = []

for i in range(k):
    x, y, direct = map(int, input().split())
    board_State[x-1][y-1].append(i)
    horses.append([x-1,y-1,direct-1])
    
direction = [(0,1),(0,-1),(-1,0),(1,0)]
cnt = 1

flag = False
while cnt <= 1000:
    for i in range(k):
        if move(i):
            flag = True
            break
    if flag :
        break
    cnt += 1
    
print(cnt if cnt <= 1000 else -1)
'''
https://chldkato.tistory.com/130 참고,
board[x][y]가 빨간색일 때 처리하는 과정에서 엄청 해멧다...
'''