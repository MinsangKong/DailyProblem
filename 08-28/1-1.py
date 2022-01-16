#https://www.acmicpc.net/problem/2578
#백준 2578번 빙고 (구현)
import sys
#input = sys.stdin.readline

def count():
    cnt = 0
    for i in range(5):
        if board[i][0] == 0:
            cnt += row(i)
        if board[0][i] == 0 :
            cnt += colunm(i)
    cnt += diagonal(0,0)
    cnt += diagonal(4,0)
    return cnt
            
                
def diagonal(x,y):
    if x == 0 :
        while x < 5 :
            if board[x][x] != 0 :
                return False
            x += 1
        return True
    else:
        while x >= 0 :
            if board[x][y] != 0 :
                return False
            x -= 1
            y += 1
        return True
    
def row(x):
    for j in range(5):
        if board[x][j] != 0:
            return False
    return True

def colunm(y):
    for i in range(5):
        if board[i][y] != 0 :
            return False
    return True

board = [list(map(int, input().split())) for _ in range(5)]
index = dict()
question = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        index[board[i][j]] = i*5+j
        
result = 0

for i in range(5):
    for j in range(5):
        a,b = divmod(index[question[i][j]],5)
        board[a][b] = 0
        result += 1
        if result >= 12 :
            num = count()
            if num >= 3 :
                print(result)
                sys.exit(0)