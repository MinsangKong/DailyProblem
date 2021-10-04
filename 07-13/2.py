#https://www.acmicpc.net/problem/9205
#백준 9205번 맥주 마시면서 걸어가기(플로이드)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for i in range(t):
    n = int(input())
    board = []
    distance = [[INF]*(n+2) for _ in range(n+2)]
    
    for i in range(n+2):
        board.append(list(map(int, input().split())))
        
    for i in range(n+2):
        for j in range(i+1,n+2):
            dist = abs(board[i][0]-board[j][0])+abs(board[i][1]-board[j][1])
            
            if dist <= 1000:
                distance[i][j] = 1
                distance[j][i] = 1
                
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                if distance[i][k] == 1 and distance[k][j] == 1:
                    distance[i][j] = 1
    
    if distance[n+1][0] != INF:
        print("happy")
    else:
        print("sad")