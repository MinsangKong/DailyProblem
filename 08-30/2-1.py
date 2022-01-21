#https://www.acmicpc.net/problem/15886
#백준 15886번 내 선물을 받아줘 2 (DFS)
#import sys
#input = sys.stdin.readline

def dfs(x):
    q = [x]
    flag = False
    while q :
        now = q.pop()
        
        if board[now] == 'E' and now+1 < n:
            if not visited[now+1] :
                flag= True
                visited[now+1] = 1
                q.append(now+1)
        elif board[now] == 'W' and now-1 >= 0:
            if not visited[now-1]:
                flag = True
                visited[now-1] = 1
                q.append(now-1)
    return flag

n = int(input())
board = input().rstrip()
visited = [0]*n
cnt = 0
for i in range(n):
    if not visited[i]:
        visited[i] = 1
        cnt += dfs(i)
        
print(cnt)