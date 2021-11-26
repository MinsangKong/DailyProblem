#https://www.acmicpc.net/problem/1789
#백준 1789번 수들의 합 (정수론)
#import sys
#input = sys.stdin.readline

n = int(input())
target = 1
limit = 2*n
while target*(target+1) <= limit:
    target += 1
    
print(target-1)