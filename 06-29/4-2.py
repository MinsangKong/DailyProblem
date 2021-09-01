#https://www.acmicpc.net/problem/16571
#백준 16571번 알파 틱택토(백트래킹)
#import sys
#input = sys.stdin.readline

def checker(turn):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if turn == board[i][0] :
                return True
        if board[0][i] == board[1][i] == board[2][i]:
            if turn  == board[0][i]:
                return True
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if turn == board[1][1]:
            return True
    return False

def game(turn):
    if checker(3-turn): #현재 상태에서 상대턴이 이기면 결과는 정해져 있음
        return -1
    
    case = 2
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = turn 
                case = min(case, game(3-turn)) #상대턴의 결과가 패배하면 내가 이긴 것
                board[i][j] = 0

    if case == 2 or case == 0:
        return 0
    else :
        return -case #상대턴의 입장에서 구한 것이기 때문에 반환할 경우에는 음수로 반환
    
cnt = 0
board = [[0]*3 for _ in range(3)]

for i in range(3):
    data = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = data[j]
        if board[i][j] > 0:
            cnt+=1

result = 0
if cnt%2 == 0 :
    result = game(1)
else:
    result = game(2)
    
if result == 0:
    print("D")
elif result == 1:
    print("W")
else:
    print("L")