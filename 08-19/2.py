#https://www.acmicpc.net/problem/12101
#백준 12101번 1,2,3 더하기 2 (백트래킹)
import sys
#input = sys.stdin.readline

def dfs(total, num):
    global count
    if total >= n :
        if total == n :
            count += 1
            if count == k :
                print('+'.join(map(str,num)))
                sys.exit(0)
        return
    for i in range(1,4):
        num.append(i)
        dfs(total+i, num)
        num.pop()

n, k = map(int, input().split())
count = 0
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

if dp[n] < k :
    print(-1)
else:
    dfs(0,[])