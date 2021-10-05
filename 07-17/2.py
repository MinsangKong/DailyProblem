#https://www.acmicpc.net/problem/11060
#백준 11060번 점프 점프(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    visited = [0]*n
    q = deque()
    visited[0] = 1
    q.append([0, 0])
    while q:
        cnt, now = q.popleft()
        #print(now, cnt)
        if now == n-1:
            return cnt
        for i in range(1,nums[now]+1):
            if now+i < n and not visited[now+i]:
                visited[now+i] = 1
                q.append([cnt+1, now+i])
    return -1
    
n = int(input())
nums = list(map(int, input().split()))

print(bfs())