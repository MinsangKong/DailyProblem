#https://www.acmicpc.net/problem/19645
#백준 19645번 햄최몇?(DP, 플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))
total = sum(values)

dp = [[0]*(50*n+1) for _ in range(50*n+1)] #x는 첫째, y는 둘째

dp[0][0] = 1
for k in range(n):
    for i in range(total,-1,-1):
        for j in range(total,-1,-1):
            if i - values[k] >= 0:
                dp[i][j] = max(dp[i][j],dp[i-values[k]][j])
            if j - values[k] >= 0:
                dp[i][j] = max(dp[i][j],dp[i][j-values[k]])
                
result = 0
for i in range(total+1):
    for j in range(i+1):
        if dp[i][j] and j >= total-i-j: #dp[i][j]가 1이면 가능한 조합이란 의미
            result = max(result, total-i-j)
print(result)
'''
DP로 방향을 바꾸어 풀다보니 맨 처음에는 3차원 배열로 하려고 했지만 메모리 초과발생
생각해보니 x,y의 값이 정해지면 나머지 값은 막내의 몫이기 때문에 해당 조합이 가능한지만
체크하기 위해 dp와 플로이드를 사용했다
'''