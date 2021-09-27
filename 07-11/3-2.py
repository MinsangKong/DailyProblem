#https://www.acmicpc.net/problem/13422
#백준 13422번 도둑(누적합)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    prefixSum = [0]*n
    prefixSum[0] = nums[0]
    
    for i in range(1,n):
        prefixSum[i] = prefixSum[i-1]+nums[i]
        
    if m == n :
        if prefixSum[n-1] < k :
            print(1)
        else:
            print(0)
    else:
        cnt = 0
        for i in range(n):
            s = i
            e = i+m
            if e >= n :
                if prefixSum[n-1]-prefixSum[s]+prefixSum[m-n+s] < k:
                    cnt += 1
            else:
                if prefixSum[e]-prefixSum[s] < k :
                    cnt += 1
        print(cnt)    