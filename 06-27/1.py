#https://www.acmicpc.net/problem/13410
#백준 13410번 거꾸로 구구단(그리디)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())

total = 0

for i in range(1,k+1):
    num = str(n*i)
    total = max(int(num[::-1]), total)
    
print(total)