import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
table = [input().rstrip() for x in range(n)]

dist = [[inf for y in range(m)] for x in range(n)]
costs = [[0 for y in range(m)] for x in range(n)]

for x in range(n):
    for y in range(m):
        if table[x][y] == 'S':
            sx, sy = x, y
            dist[x][y] = 0
        if table[x][y] == 'F':
            fx, fy = x, y
        if table[x][y] == 'g':
            costs[x][y] = 10000
            for i in range(4):
                x1 = x + dx[i]
                y1 = y + dy[i]
                if 0 <= x1 < n and 0 <= y1 < m and table[x1][y1] == '.':
                    costs[x1][y1] = 1

heap = []
heappush(heap, (0, sx, sy))

while heap:
    cost, x, y = heappop(heap)

    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]

        if 0 <= x1 < n and 0 <= y1 < m:
            temp = cost + costs[x1][y1]

            if dist[x1][y1] > temp:
                dist[x1][y1] = temp
                heappush(heap, (temp, x1, y1))

a = dist[fx][fy]//10000
b = dist[fx][fy]%10000

print(a, b)