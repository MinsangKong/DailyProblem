#https://www.acmicpc.net/problem/5549
#백준 5549번 행성 탐사 (DP)
#import sys
#input = sys.stdin.readline

def count(arr,word):
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr[i][j] = arr[i-1][j]+arr[i][j-1]-arr[i-1][j-1]
            if board[i-1][j-1] == word:
                arr[i][j] += 1

n, m = map(int, input().split())
k = int(input())
jungle = [[0]*(m+1) for _ in range(n+1)]
sea = [[0]*(m+1) for _ in range(n+1)]
ice = [[0]*(m+1) for _ in range(n+1)]

board = [input().rstrip() for _ in range(n)]

count(jungle,'J')
count(sea,'O')
count(ice,'I')

for i in range(k):
    a,b,c,d = map(int, input().split())
    print(jungle[c][d]-jungle[a-1][d]-jungle[c][b-1]+jungle[a-1][b-1], end = ' ')
    print(sea[c][d]-sea[a-1][d]-sea[c][b-1]+sea[a-1][b-1], end = ' ')
    print(ice[c][d]-ice[a-1][d]-ice[c][b-1]+ice[a-1][b-1])