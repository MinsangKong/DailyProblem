#https://www.acmicpc.net/problem/15558
#백준 15558번 점프 게임(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append([1,0,0])
    visited = [[0]*n for _ in range(2)]
    visited[0][0] = 1
    while q:
        sec, idx, state = q.popleft()
        #print(sec,idx,state)
        if state :
            if idx+k >= n:
                return 1
            elif not visited[0][idx+k] and l[idx+k] == '1':
                visited[0][idx+k] = 1
                q.append([sec+1, idx+k, 0])
            
            if idx+1 >= n:
                return 1
            elif not visited[state][idx+1] and r[idx+1] == '1':
                visited[state][idx+1] = 1
                q.append([sec+1, idx+1, state])
            
            if idx-1 >= sec:
                if not visited[state][idx-1] and r[idx-1] == '1':
                    visited[state][idx-1] = 1
                    q.append([sec+1, idx-1, state])
        else:
            if idx+k >= n:
                return 1
            elif not visited[1][idx+k] and r[idx+k] == '1':
                visited[1][idx+k] = 1
                q.append([sec+1, idx+k, 1])
            
            if idx+1 >= n:
                return 1
            elif not visited[state][idx+1] and l[idx+1] == '1':
                visited[state][idx+1] = 1
                q.append([sec+1, idx+1, state])
            
            if idx-1 >= sec:
                if not visited[state][idx-1] and l[idx-1] == '1':
                    visited[state][idx-1] = 1
                    q.append([sec+1, idx-1, state])
    return 0

n ,k = map(int, input().split())

l = list(input().rstrip())
r = list(input().rstrip())

print(bfs())