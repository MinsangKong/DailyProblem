#https://www.acmicpc.net/problem/17128
#백준 17128번 소가 정보섬에 올라온 이유 (정수론,구현)
#import sys
#input = sys.stdin.readline

n, q = map(int, input().split())
cows = list(map(int, input().split()))
swaps = list(map(int, input().split()))
dp = [0]*n
dp[0] = cows[0]*cows[1]*cows[2]*cows[3]
s,e = 0, 3
result = dp[0]
for i in range(1,n):
    num = dp[i-1]
    e += 1
    if e >= n :
        e = 0
    num //= cows[s]
    num *= cows[e]
    s += 1
    if s >= n :
        s = 0
    dp[i] = num
    result += num

for swap in swaps:
    target = swap
    for i in range(4):
        target -= 1
        if target < 0 :
            target = n-1
        result -= dp[target]
        dp[target] *= -1
        result += dp[target]
    print(result)