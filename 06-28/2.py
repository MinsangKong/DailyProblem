#https://www.acmicpc.net/problem/14499
#백준 14499번 주사위 굴리기(구현)
#import sys
#input = sys.stdin.readline

def roll(oper):
    if oper == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif oper == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif oper == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    elif oper == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        
def changer(x,y,oper):
    roll(oper)
    if board[x][y] == 0:
        board[x][y] = dice[5]
    else:
        dice[5]= board[x][y]
        board[x][y] = 0

n, m, x, y, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
opers = list(map(int, input().split()))

dice = [0]*6 #top,north,east,west,south,bottom

for oper in opers:
    if oper == 1:
        if y+1 >= m :
            continue
        else:
            y+=1
            changer(x,y,oper)
    elif oper == 2:
        if y-1 < 0:
            continue
        else:
            y-=1
            changer(x,y,oper)
    elif oper == 3:
        if x-1 < 0:
            continue
        else:
            x-=1
            changer(x,y,oper)
    else :
        if x+1 >= n:
            continue
        else:
            x+=1
            changer(x,y,oper)
    #print(dice)
    print(dice[0])