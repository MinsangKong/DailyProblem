import sys

N, M = map(int, sys.stdin.readline().split())
occupied = [[False for _ in range(N+1)] for _ in range(N+1)]
answer = 0


for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    occupied[x][y], occupied[y][x] = True, True

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if occupied[i][j]:
            continue
        for k in range(j+1, N+1):
            if (occupied[i][k] or occupied[j][k]):
                continue
            answer += 1
print(answer)