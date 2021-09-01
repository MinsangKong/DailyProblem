#https://www.acmicpc.net/problem/16571
#백준 16571번 알파 틱택토(백트래킹)
#import sys
#input = sys.stdin.readline

def checker(turn): #승리 1, 무승부 2, 패배 3
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if turn == board[i][0]:
                return 1
            else:
                return 3
        if board[0][i] == board[1][i] == board[2][i]:
            if turn == board[0][i]:
                return 1
            else:
                return 3
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if turn == board[1][1]:
            return 1
        else:
            return 3
    return 2

def dfs(cnt, turn):
    global state
    global win
    if cnt == 0 or win == 1:
        return 
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = turn
                result = checker(turn)
                if turn == state:
                    win = min(win, result)
                if result == 3:
                    board[i][j] = 0
                    continue
                if win == 1:
                    return
                if turn == 1:
                    dfs(cnt-1,turn+1)
                else:
                    dfs(cnt-1,turn-1)
                board[i][j] = 0

board = [list(map(int, input().split())) for _ in range(3)]

turn = 0
choice = 0
win = 4
state = 0

for i in range(3):
    for j in range(3):
        if board[i][j] == 1:
            turn +=1
        elif board[i][j] == 2:
            turn -=1
        else:
            choice += 1
            
if turn == 0:
    turn = 1
    state = 1
else:
    turn = 2
    state = 2
    
dfs(choice, turn)

if win == 1:
    print("W")
elif win == 2:
    print("D")
else:
    print("L")
#최선의 경우의 수가 아니여서 계속 틀린다...