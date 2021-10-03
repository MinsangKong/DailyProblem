#https://www.acmicpc.net/problem/2447
#백준 2447번 별 찍기 - 10 (구현,분할정복)
#import sys
#input = sys.stdin.readline

def dfs(x,y,depth):
    if depth == 3 :
        for i in range(x,x+3):
            for j in range(y,y+3):
                if i == x+1  and j == y+1:
                    result[i][j] = ' '
                else:
                    result[i][j] = '*'
    else:
        base = depth//3
        for i in range(x,x+depth,base):
            for j in range(y,y+depth,base):
                if i == x+base and j == y+base:
                    for v in range(x+base,x+base*2):
                        for w in range(y+base,y+base*2):
                            result[v][w] = ' '
                else:
                    dfs(i,j,base)

n = int(input())
result = [[0]*n for _ in range(n)]

dfs(0,0,n)

for i in result:
    print(''.join(i))