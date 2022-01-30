import sys

N = int(sys.stdin.readline())
dp = [[0] * (N + 1) for _ in range(5)]
for i in range(1, N + 1):
    l, r = map(int, sys.stdin.readline().split())
    dp[l - 1][i] = dp[l - 1][i - 1] + 1
    dp[r - 1][i] = dp[r - 1][i - 1] + 1
min_grade = 6
max_stu = 0
for i in range(5):
    if max(dp[i]) > max_stu:
        max_stu = max(dp[i])
        min_grade = i + 1
print(max_stu, min_grade)