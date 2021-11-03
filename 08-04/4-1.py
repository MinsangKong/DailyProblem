#https://www.acmicpc.net/problem/1445
#백준 1445번 일요일 아침의 데이트 (다익스트라)
#import sys
#input = sys.stdin.readline
import heapq
INF = int(1e9)

class node:
    def __init__(self, cnt, near, x, y):
        self.cnt = cnt
        self.near = near
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.cnt < other.cnt:   #오름차순
            return True
        elif self.cnt == other.cnt:
            return self.near < other.near  #첫번재 변수가 같으면 두번재 변수로 내림차순
        else:
            return False

def dijkstra(x,y):
    distance = [[INF]*m for _ in range(n)]
    distance[x][y] = 0
    nearcount = [[INF]*m for _ in range(n)]
    nearcount[x][y] = 0
    q = []
    heapq.heappush(q, node(0,0,x,y))
    while q:
        now = heapq.heappop(q)
        g, ng, dx, dy = now.cnt, now.near, now.x, now.y
        
        if distance[dx][dy] != g or nearcount[dx][dy] != ng:
            continue
        
        if board[dx][dy] == 'F':
            print(g, ng)
            return
        
        for a,b in direction:
            nx = a + dx
            ny = b + dy
            check = 0
            cnt = 0
            if 0 <= nx < n and 0 <= ny < m :
                if board[nx][ny] == 'g':
                    check += 1
                if board[nx][ny] == '.':
                    cnt = count(nx,ny)
                if distance[nx][ny] > g + check:
                    distance[nx][ny] = g + check
                    nearcount[nx][ny] = ng + cnt
                    heapq.heappush(q, node(g+check, nearcount[nx][ny],nx,ny))
                elif distance[nx][ny] == g+check and nearcount[nx][ny] > ng+ cnt:
                    nearcount[nx][ny] = ng + cnt
                    heapq.heappush(q, node(g+check, nearcount[nx][ny],nx,ny))

def count(x,y):
    cnt = 0
    for a,b in direction:
        nx = x+a
        ny = y+b
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 'g':
                return 1
    return 0
    
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
direction = [(1,0),(-1,0),(0,1),(0,-1)]

sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            sx, sy = i, j
            break

dijkstra(sx,sy)
#https://lucky516.tistory.com/5에서 custom heap 참고