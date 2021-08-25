#https://www.acmicpc.net/problem/14226
#백준 14226번 이모티콘(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def bfs(target):
    q = deque()
    q.append([2,2,1])
    visited = [[int(1e9)]*2001 for _ in range(2001)] #속도를 개선하려면 set으로 방문 여부 체크
    visited[1][1] = 1
    visited[2][1] = 2
    while q :
        sec, display, board = q.popleft()
        if display == target:
            return sec
        
        if 2 <= display+board <= 2000 and visited[display+board][board] > sec+1:
            visited[display+board][board] = sec+1
            q.append([sec+1, display+board, board])
        if 2 <= display-1 <= 2000 and visited[display-1][board] > sec+1:
            visited[display-1][board] = sec+1
            q.append([sec+1, display-1, board])
        if 2 <= display <= 2000 and visited[display][display] > sec+1:
            visited[display][display] = sec+1
            q.append([sec+1,display,display])
        

n = int(input())
print(bfs(n))