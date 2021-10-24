#https://www.acmicpc.net/problem/11051
#백준 11051번 이항 계수 2 (정수론)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())

result = 1

for i in range(n,n-k,-1):
    result *= i 
    
for j in range(2,k+1):
    result = result // j
    
print(result%10007)