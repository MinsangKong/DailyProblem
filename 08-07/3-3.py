import sys
read = sys.stdin.readline

n = int(read())
h = [[*map(int, read().split())] for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
ans = float('inf')

for k in range(3):
    for l in range(3):
        if k == l:
            dp[0][l] = h[0][l]
        else:
            dp[0][l] = float('inf')

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + h[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + h[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + h[i][2]

    for m in range(3):
        if m != k:
            ans = min(ans, dp[-1][m])

print(ans)