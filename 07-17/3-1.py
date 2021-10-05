#https://www.acmicpc.net/problem/17123
#백준 17123번 배열 놀이 (누적합)
#import sys
#input =  sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp =[[0]*(n+1) for _ in range(n+1)]
    
    for _ in range(m):
        r1,c1,r2,c2,v = map(int, input().split())
        dp[r1-1][c1-1] += v
        dp[r2][c1-1] -= v
        dp[r1-1][c2] -= v
        dp[r2][c2] += v
        
    for i in range(n):
        for j in range(n):
            if i > 0 and j > 0 :
                dp[i][j] += dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
            elif i > 0 :
                dp[i][j] += dp[i-1][j]
            elif j > 0 : 
                dp[i][j] += dp[i][j-1]
                
    for i in range(n):
        for j in range(n):
            board[i][j] += dp[i][j]
    prefixSum = [[0]*(n+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = prefixSum[i][j-1]+prefixSum[i-1][j]-prefixSum[i-1][j-1]+board[i-1][j-1]
            
    row = []
    column = []
    for i in range(1, n+1):
        row.append(prefixSum[i][n]-prefixSum[i-1][n])
        column.append(prefixSum[n][i]-prefixSum[n][i-1])
    print(*row)
    print(*column)