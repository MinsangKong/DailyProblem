#https://www.acmicpc.net/problem/18513
#백준 18513번 샘터(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
springs = list(map(int, input().split()))

q = deque()
visited = set()

for spring in springs:
    q.append((spring, 1))
    visited.add(spring)
    
total = 0
direction = [1,-1]

while q:
    if k == 0 :
        break
    now, idx = q.popleft()
    for d in direction:
        nx = now+d
        if nx in visited:
            continue
        visited.add(nx)
        total += idx
        k -= 1
        q.append((nx, idx+1))
        if k == 0 :
            break
            
print(total)
#계속 spring을 반복하면 시간초과가 발생하고
#시간 내에 문제를 도출하기 위해서는 현재 값을 기준으로 1씩 더하거나 빼줘야한다.