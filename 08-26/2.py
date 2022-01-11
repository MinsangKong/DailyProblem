#https://www.acmicpc.net/problem/17829
#백준 17829번 222-풀링 (분할 정복, 구현)
#import sys
#input = sys.stdin.readline 

def pulling(board):
    temp = []
    while True:
        size = len(board)
        if size == 1 :
            return board[0][0]
        
        for i in range(0,size,2):
            data = []
            for j in range(0,size,2):
                case = sorted([board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1]])
                data.append(case[2])
            temp.append(data)
        board = temp
        temp = []

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0

print(pulling(board))