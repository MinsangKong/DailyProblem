import sys, collections

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
check = [[False] * m for _ in range(n)]
group = [[0] * m for _ in range(n)]
cnt = 0
res = dict()
blank = dict()
for i in range(n):
    for j in range(m):
        if not check[i][j] and arr[i][j] == 2:
            q = collections.deque()
            q.append((i,j))
            cnt += 1
            group[i][j] = cnt
            size = 1
            check[i][j] = True
            blank[cnt] = set()
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m:
                        if not check[nx][ny] and arr[nx][ny] == 2:
                            check[nx][ny] = True
                            group[nx][ny] = cnt
                            size += 1
                            q.append((nx, ny))
                        if arr[nx][ny] == 0:
                            blank[cnt].add((nx, ny))
            blank[cnt] = list(blank[cnt])
            res[cnt] = size

ans = 0
for i in range(n):
    for j in range(m):
        for a in range(n):
            for b in range(m):
                x1, y1, x2, y2 = i, j, a, b
                if x1 == x2 and y1 == y2:
                    continue
                arr[x1][y1] = 1
                arr[x2][y2] = 1
                temp = 0
                for k in range(1, cnt + 1):
                    if len(blank[k]) == 1:
                        if (blank[k][0][0] == x1 and blank[k][0][1] == y1) or (blank[k][0][0] == x2 and blank[k][0][1] == y2):
                            temp += res[k]
                    elif len(blank[k]) == 2:
                        if (blank[k][0][0] == x1 and blank[k][0][1] == y1 and blank[k][1][0] == x2 and blank[k][1][1] == y2) or (blank[k][0][0] == x2 and blank[k][0][1] == y2 and blank[k][1][0] == x1 and blank[k][1][1] == y1):
                            temp += res[k]
                ans = max(temp, ans)
print(ans)