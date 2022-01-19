#https://www.acmicpc.net/problem/2581
#백준 2581번 소수 (정수론)
#import sys
#input = sys.stdin.readline

m = int(input())
n = int(input())
result = []

prime = [0]*(n+1)
prime[1] = 1

for i in range(2,int(n**0.5)+1):
    if prime[i] :
        continue
    for j in range(i+i,n+1,i):
        prime[j] = 1
        
for i in range(m,n+1):
    if not prime[i]:
        result.append(i)
        
if result :
    print(sum(result),result[0],sep='\n')
else:
    print(-1)