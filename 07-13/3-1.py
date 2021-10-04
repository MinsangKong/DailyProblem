#https://www.acmicpc.net/problem/13910
#백준 13910번 개업(dp)
#import sys
#input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
woks = sorted(list(map(int, input().split())))
visited = [0]*(n+1)

prefixSum = [0]*n
prefixSum[0] = woks[0] 

for i in range(1,m):
    prefixSum[i] = prefixSum[i-1]+woks[i]

q = deque()
q.append((0,0))

result = -1

while q : 
    now, cnt = q.popleft()
    
    if now == n :
        result = cnt
        break

    for i in range(m):
        temp = now + prefixSum[i]
        if temp <= n and not visited[temp]:
            visited[temp] = 1
            q.append([temp,cnt+1])
        for j in range(i-1,-1,-1):
            temp = now + (prefixSum[i]-prefixSum[j])
            if temp > n : 
                break
            if not visited[temp]:
                visited[temp] = 1
                q.append([temp,cnt+1])
            
print(result)
#아무리 봐도 맞았는데 틀린 이유는 동시에 사용할 수 있는 웍의 수는 2개로 제한되어 있었다...