#https://www.acmicpc.net/problem/20327
#백준 20327번 배열 뒤집기 6 (구현, 시뮬레이션)
#import sys
#input = sys.stdin.readline

def first(l):
    length = 2**l
    cnt = 0
    for x in range(0,N,length):
        for y in range(0,N,length):
            ex = x+length
            ey = y+length
            for i in range(x,ex):
                for j in range(y,ey):
                    changedBoard[ex-1-i+length*cnt][j] = board[i][j]
        cnt += 1
    change()
        
def second(l):
    length = 2**l
    cnt = 0
    for x in range(0,N,length):
        for y in range(0,N,length):
            ex = x+length
            ey = y+length
            for i in range(x,ex):
                for j in range(y,ey):
                    changedBoard[i][ey-1-j+length*cnt] = board[i][j]
            cnt += 1
        cnt = 0
    change()
    
def third(l):
    length = 2**l
    gap = 0
    cnt = 0
    for x in range(0,N,length):
        for y in range(0,N,length):
            ex = x+length
            ey = y+length
            for i in range(x,ex):
                for j in range(y,ey):
                    changedBoard[j-length*gap+length*cnt][ex-1-i+length*gap] = board[i][j]
            gap += 1
        cnt += 1
        gap = 0
    change()
    
def fourth(l):
    length = 2**l
    gap_x, gap_y = 0, 0
    cnt = 0
    for x in range(0,N,length):
        for y in range(0,N,length):
            ex = x+length
            ey = y+length
            for i in range(x,ex):
                for j in range(y,ey):
                    changedBoard[ey-1-j+length*gap_x][i+length*gap_y-length*cnt] = board[i][j]
            gap_y += 1
        cnt += 1
        gap_x += 1
        gap_y = 0
    change()
    
def fifth(l):
    first(n)
    first(l)
    
def sixth(l):
    second(n)
    second(l)
    
def seventh(l):
    third(n)
    fourth(l)
    
def eighth(l):
    fourth(n)
    third(l)
    
def change():
    global board, changedBoard
    board = [item[:] for item in changedBoard]
        
n, r = map(int, input().split())
N = 2**n
board = [list(map(int, input().split())) for _ in range(N)]
changedBoard = [[0]*(N) for _ in range(N)]

for i in range(r):
    a, b = map(int, input().split())
    if a <= 4 and b == 0 :
        continue
    if a == 1 :
        first(b)
    elif a == 2:
        second(b)
    elif a == 3:
        third(b)
    elif a == 4:
        fourth(b)
    elif a == 5:
        fifth(b)
    elif a == 6 :
        sixth(b)
    elif a == 7 :
        seventh(b)
    else:
        eighth(b)
        
for nums in board:
    print(*nums)
#https://conkjh032.tistory.com/287 참고