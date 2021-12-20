import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coords = [0] + [list(map(int, input().split())) for _ in range(n)]

dist = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dist[i][j] = sum(abs(a - b) for a, b in zip(coords[i], coords[j]))

dp = [[float('inf') for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + dist[i - 1][i]

    for j in range(1, k + 1):
        if 0 < j < i - 1:
            dp[i][j] = min(dp[i - 1 - x][j - x] + dist[i - 1 - x][i] for x in range(j + 1))
        else:
            break

print(dp[-1][-1])