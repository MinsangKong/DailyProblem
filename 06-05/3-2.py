from collections import deque
DIR = ((0,1),(1,0),(0,-1),(-1,0))   #동남서북
def bfs(sy,sx):
    queue = deque([(sy,sx)])
    visited[sy][sx] = 0
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            dy,dx = DIR[i]
            ny,nx = y+dy,x+dx
            while True:
                if not((0<=ny<N)and(0<=nx<M)): break
                if board[ny][nx] =='*': break
                if visited[ny][nx] < visited[y][x] + 1: break
                queue.append((ny,nx))
                visited[ny][nx] = visited[y][x]+1
                ny+=dy
                nx+=dx

M,N = map(int,input().split())
board = [input() for _ in range(N)]
visited = [[float('inf')]*M for _ in range(N)]
c_pos = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 'C': c_pos.append((y,x))
(sy,sx),(ey,ex) = c_pos
bfs(sy,sx)
print(visited[ey][ex]-1)