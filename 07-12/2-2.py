N = int(input())

arr = list(map(int,input().split()))
dp = [0]*1001
for i in range(N):
    dp[arr[i]] = max(dp[:arr[i]]) + arr[i]

print(max(dp))
'''
소름돋게 간단한 방법이 있었다... 후 ...
숫자의 제한이 1~1000으로 제한되어 있기 때문에 결국 딕셔너리처럼 사용하면 간단했다...
'''