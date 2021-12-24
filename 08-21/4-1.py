#https://www.acmicpc.net/problem/16438
#백준 16438번 원숭이 스포츠 (분할 정복)
#import sys
#input = sys.stdin.readline

def dfs(l,r,date,idx):
    if date == 7:
        return
    mid = (l+r)//2
    for i in range(l,r+1):
        if i <= mid :
            board[date][i] = change(idx)
        else:
            board[date][i] = change(not idx)
            
    dfs(l,mid,date+1,not idx)
    dfs(mid+1,r,date+1,idx)
            
def change(idx):
    if idx :
        return 'A'
    else:
        return 'B'
        

n = int(input())
board = [[0]*n for _ in range(7)]

dfs(0,n-1,0,0)

for i in board:
    print(''.join(i))