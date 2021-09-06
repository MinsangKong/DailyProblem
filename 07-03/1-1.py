#https://www.acmicpc.net/problem/14929
#백준 14929번 귀찮아 (SIB) (누적합)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

totals = [0]*n

totals[0] = nums[0]

for i in range(1,n):
    totals[i]+=totals[i-1]+nums[i]
    
result = 0
for i in range(n):
    result+=nums[i]*(totals[n-1]-totals[i])
    
print(result)