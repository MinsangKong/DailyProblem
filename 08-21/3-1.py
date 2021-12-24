#https://www.acmicpc.net/problem/13902
#백준 13902번 개업 2 (DP)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

if m == 1 :
    print(-1 if n%nums[0] else n//nums[0])
else:
    dp = [INF]*(n+1)
    woks = set()
    for i in range(m):
        if nums[i] > n :
            break
        woks.add(nums[i])
        for j in range(i+1,m):
            if nums[i]+nums[j] > n:
                break
            woks.add(nums[i]+nums[j])
    woks = sorted(list(woks))
    for wok in woks:
        dp[wok] = 1

    for i in range(1, n+1):
        if dp[i] != INF:
            for wok in woks:
                if i+wok > n :
                    break
                dp[i+wok] = min(dp[i+wok], dp[i]+1)
    print(-1 if dp[n] == INF else dp[n])
#바보마냥 n//nums[0]로 해야하는데 n//m으로 해서 틀렸다...