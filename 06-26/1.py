#https://www.acmicpc.net/problem/11720
#백준 11720번 숫자의 합(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = list(input().rstrip())

total = 0

for num in nums:
    total+=int(num)
    
print(total)