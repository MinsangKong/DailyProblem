#https://www.acmicpc.net/problem/19699
#백준 19699번 소-난다! (정수론)
#import sys
#input = sys.stdin.readline

def dfs(idx,total,cnt):
    global result 
    if idx == n:
        if cnt == m and not primes[total]:
            result.add(total)
        return
    dfs(idx+1,total,cnt)
    dfs(idx+1,total+weights[idx],cnt+1)

n, m = map(int, input().split())
weights = list(map(int, input().split()))

primes = [0]*9001
primes[0] = 1
primes[1] = 1
result = set()
for i in range(2,int(9001**0.5)+1):
    for j in range(i+i,9001,i):
        primes[j] = 1
        
dfs(0,0,0)
if result :
    print(*sorted(result))
else:
    print(-1)