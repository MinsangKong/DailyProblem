#https://www.acmicpc.net/problem/11399
#백준 11399번 ATM(그리디)
#import sys
#input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))

line.sort()
sub = 0
result = 0
for cost in line:
    sub+=cost
    result+=sub
    
print(result)