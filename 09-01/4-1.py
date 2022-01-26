#https://www.acmicpc.net/problem/14391
#백준 14391번 종이 조각 (DFS)
#import sys
#input = sys.stdin.readline

def bitmask():
    global result
    
    for i in range(1 << n*m):
        total = 0
        for row in range(n):
            rowsum = 0
            for col in range(m):
                idx = row*m + col
                if i & (1 << idx) != 0 :
                    rowsum = rowsum*10 + board[row][col]
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum
            
        for col in range(m):
            colsum = 0 
            for row in range(n):
                idx = row*m + col
                if i & (1 << idx) == 0 :
                    colsum = colsum*10 + board[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum
        result = max(result, total)

n,m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
result = 0
bitmask()
print(result)
#https://vixxcode.tistory.com/23 참고