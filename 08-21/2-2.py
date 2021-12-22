import sys
from collections import deque
input = sys.stdin.readline
D = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = ans
    union = [(i, j)]
    cnt = 1
    total = board[i][j]
    while q:
        x, y = q.popleft()
        now = board[x][y]
        for dx, dy in D:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] != ans and l<=abs(now-board[nx][ny])<=r:
                cnt += 1
                total += board[nx][ny]
                union.append((nx, ny))
                visited[nx][ny] = ans
                q.append((nx, ny))
    if cnt > 1:
        population = total // cnt
        for x, y in union:
            board[x][y] = population
            search_list.append((x, y))
        return True
    return False
        

n, l, r = map(int, input().split())
board = []
search_list = []
visited = [[-1] * n for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().split())))
    search_list += [(i, j) for j in range(n)]

search_list = deque(search_list)
ans = 0
while search_list:
    stop = True
    for _ in range(len(search_list)):
        si, sj = search_list.popleft()
        if visited[si][sj] != ans:
            if bfs(si, sj):
                stop = False
    if stop:
        break
    ans += 1
print(ans)