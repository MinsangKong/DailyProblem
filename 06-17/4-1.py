#https://www.acmicpc.net/problem/1799
#백준 1799번 비숍(DFS,이분매칭)
#import sys
#input = sys.stdin.readline

def dfs(idx):
    visited[idx] = 1
    s = link[idx]
    for p in s:
        if r2l[p] == 0 or (not visited[r2l[p]] and dfs(r2l[p])):
            r2l[p] = idx
            l2r[idx] = p
            return True
    return False

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
left = [[0]*n for _ in range(n)]
right = [[0]*n for _ in range(n)]
s, e = 1,1

for j in range(n):
    i = 0
    while i < n and 0 <= j:
        if board[i][j] == 1:
            right[i][j] = e
        i += 1
        j -= 1
    e +=1
for i in range(1,n):
    j = n-1
    while i < n and 0 <= j:
        if board[i][j] == 1:
            right[i][j] = e
        i += 1
        j -= 1
    e += 1
    
for j in range(n-1,-1,-1):
    i = 0
    while i < n and j < n:
        if board[i][j] == 1:
            left[i][j] = s
        i += 1
        j += 1
    s += 1
for i in range(1,n):
    j = 0
    while i < n and j < n:
        if board[i][j] == 1:
            left[i][j] = s
        i += 1
        j += 1
    s += 1
    
link = [[] for _ in range(s)]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            link[left[i][j]].append(right[i][j])

l2r = [0] * (2*n) 
r2l = [0] * (2*n) 
ans = 0 
for i in range(1, 2*n):
    visited = [0] * (2*n) 
    if dfs(i): 
        ans += 1 
        
print(ans)

'''
https://suri78.tistory.com/184
https://blog.naver.com/kks227/220807541506
https://blog.naver.com/PostView.nhn?blogId=na_qa&logNo=221501909499 참고
'''