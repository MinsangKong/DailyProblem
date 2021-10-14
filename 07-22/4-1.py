#https://www.acmicpc.net/problem/2629
#백준 2629번 양팔저울()
#import sys
#input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

m = int(input())
balls = list(map(int, input().split()))

total = sum(nums)

dp = [0]*(total+1)
dp[0] = 1

for num in nums:
    for i in range(total+1,num-1,-1):
        if dp[i-num]:
            dp[i] = 1
        
print(dp)
for ball in balls:
    if ball <= total :
        if dp[ball] :
            print('Y', end = " ")
        else:
            flag = False
            for i in range(1,total-ball+1):
                if dp[i] and dp[i+ball]:
                    flag = True
                    break
            if flag:
                print('Y', end = ' ')
            else:
                print('N', end = ' ')
    else:
        print('N', end = " ")
'''
결과적으로 dp[i]와 dp[i+ball]을 만족한다는 의미는 ball을 만족할 수 있는 추가 
존재한다는 뜻이기 때문에 결과적으로 dp[i+ball]를 구성하는 데 dp[i]를 사용하더라도
상관이 없었다...
빠르게 푼 사람들의 코드를 보면 약간 비효율적인 측면이 있지만 그래도 오랜만에
원트에 dp문제를 잘 푼 것같아서 기분이 좋다
'''