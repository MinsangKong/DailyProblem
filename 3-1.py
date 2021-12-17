#https://www.acmicpc.net/problem/14925
#백준 14925번 목장 건설하기 (백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(x,y):
    global l
    if x == n:
        dfs(0,y+1)
        return
    if y == m or l == limit:
        return
    
    if not board[x][y]:
        l = max(l,count(x,y))
    dfs(x+1,y)
    
def count(x,y):
    cnt = 1
    for k in range(2,limit+1):
        if x+k > n or y+k > m :
            return cnt
        for i in range(x,x+k):
            for j in range(y,y+k):
                if board[i][j]:
                    return cnt
        cnt += 1
    return cnt

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
limit = min(n,m)
l = 0

dfs(0,0)
print(l)
#옳은 풀이법이지만 시간 초과 문제