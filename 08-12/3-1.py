#https://www.acmicpc.net/problem/15723
#백준 15723번 n단 논법 (플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())
board = [[0]*26 for _ in range(26)]

for _ in range(n):
    a,_,b = input().split()
    na, nb = ord('z')-ord(a), ord('z')-ord(b)
    board[na][nb] = 1
    
for k in range(26):
    for i in range(26):
        for j in range(26):
            if board[i][k] and board[k][j]:
                board[i][j] = 1
                
m = int(input())
for _ in range(m):
    a,_,b = input().split()
    na, nb = ord('z')-ord(a), ord('z')-ord(b) 
    if na == nb :
        print("T")
    elif board[na][nb]:
        print("T")
    else:
        print("F")