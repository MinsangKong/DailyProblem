#https://www.acmicpc.net/problem/17470
#백준 17470번 배열돌리기 5(최적화,효율성)
#import sys
#input = sys.stdin.readline
def first(board,n,m):
    result = []
    for i in range(n-1,-1,-1):
        result.append(board[i])
    return result,n,m

def second(board,n,m):
    result = []
    for i in range(n):
        result.append(board[i][::-1])
    return result,n,m

def third(board,n,m):
    result = [[] for _ in range(m)]

    for i in range(m):
        for j in range(n-1,-1,-1):
            result[i].append(board[j][i])
    return result,m,n

def fourth(board,n,m):
    result = [[] for _ in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(n):
            num = m-1-i
            result[num].append(board[j][i])
    return result,m,n

def fifth(board,n,m):
    width = n//2
    height = m//2
    result = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i >= width and j >= height:
                result[i][j-height] = board[i][j]
            elif i >= width and j < height:
                result[i-width][j] = board[i][j]
            elif i < width and j < height:
                result[i][j+height] = board[i][j]
            elif i < width and j >= height:
                result[i+width][j] = board[i][j]
    return result,n,m

def sixth(board,n,m):
    width = n//2
    height = m//2
    result = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i >= width and j >= height:
                result[i-width][j] = board[i][j]
            elif i >= width and j < height:
                result[i][j+height] = board[i][j]
            elif i < width and j < height:
                result[i+width][j] = board[i][j]
            elif i < width and j >= height:
                result[i][j-height] = board[i][j]
    return result,n,m

n,m,r = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

oper = list(map(int, input().split()))

x,y = n,m
cnt = 0
op = 0

for i in oper:
    if op == 0:
        op = i
        cnt+=1
    else:
        if op == i:
            cnt+=1
        else:
            if op == 1 or op == 2:
                if cnt%2 == 1:
                    if op == 1:
                        board,x,y = first(board,x,y) 
                    else:
                        board,x,y = second(board,x,y)
                cnt = 1
                op = i
            elif op == 3:
                if i == 4:
                    if cnt == 0:
                        op = i
                        cnt = 1
                    else:
                        cnt-=1
                else:
                    num = cnt%4
                    if num == 3:
                        board,x,y = fourth(board,x,y)
                    else:
                        for i in range(num):
                            board,x,y = third(board,x,y)
                    op = i
                    cnt = 1
            elif op == 4:
                if i == 3:
                    if cnt == 0:
                        op = i
                        cnt = 1
                    else:
                        cnt-=1
                else:
                    num = cnt%4
                    if num == 3:
                        board,x,y = third(board,x,y)
                    else:
                        for i in range(num):
                            board,x,y = fourth(board,x,y)
                    op = i
                    cnt = 1
            elif op == 5:
                if i == 6:
                    if cnt == 0:
                        op = i
                        cnt = 1
                    else:
                        cnt-=1
                else:
                    num = cnt%4
                    if num == 3:
                        board,x,y = sixth(board,x,y)
                    else:
                        for i in range(num):
                            board,x,y = fifth(board,x,y) 
                    op = i
                    cnt = 1
            elif op == 6:
                if i == 5:
                    if cnt == 0:
                        op = i
                        cnt = 1
                    else:
                        cnt-=1
                else:
                    num = cnt%4
                    if num == 3:
                        board,x,y = fifth(board,x,y) 
                    else:
                        for i in range(num):
                            board,x,y = sixth(board,x,y)
                    op = i
                    cnt = 1
                        
if op == 1:
    if cnt % 2 == 1:
        board,x,y = first(board,x,y)
elif op == 2:
    if cnt % 2 == 1:
        board,x,y = second(board,x,y)
elif op == 3:
    num = cnt%4
    if num == 3:
        board,x,y = fourth(board,x,y)
    else:
        for i in range(num):
            board,x,y = third(board,x,y)
elif op == 4:
    num = cnt%4
    if num == 3:
        board,x,y = third(board,x,y) 
    else:
        for i in range(num):
            board,x,y = fourth(board,x,y)    
elif op == 5:
    num = cnt%4
    if num == 3:
        board,x,y = sixth(board,x,y)
    else:
        for i in range(num):
            board,x,y = fifth(board,x,y)
elif op == 6:
    num = cnt%4
    if num == 3:
        board,x,y = fifth(board,x,y)
    else:
        for i in range(num):
            board,x,y = sixth(board,x,y)

for i in board:
    print(*i)
    
'''
명령의 수를 최대한 줄였지만 그래도 시간초과 발생...
어떻게 해결해야 할지 모르겠다
'''