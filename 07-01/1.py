#https://www.acmicpc.net/problem/2160
#백준 2160번 그림 비교(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

board = [list(input().rstrip()) for _ in range(n*5)]

cnt = int(1e9)
s, e = 0, 0
for i in range(n):
    for j in range(i+1,n):
        temp = 0
        for x in range(5):
            for y in range(7):
                if board[i*5+x][y] != board[j*5+x][y]:
                    temp+=1
        if cnt > temp :
            cnt = temp
            s, e = i+1, j+1
            
print(s, e)