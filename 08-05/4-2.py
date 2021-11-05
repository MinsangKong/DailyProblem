import sys

answer = 999999999999
input = sys.stdin.readline
def rotation(grid, N, M):
    new_grid = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            new_grid[i][j] = grid[j][M -1 - i]
    return new_grid
N1, M1 = map(int, input().split(' '))
grid1 = []
for i in range(N1):
    grid1.append(list(input().rstrip()))
N2, M2 = map(int, input().split(' '))
max2 = max(N2, M2)
grid2 = []
for j in range(N2):
    grid2.append(list(input().rstrip()))

max_grid = [[0 for i in range(2 * max2 + M1)] for i in range(max2)] \
    + [([0 for i in range(max2)] + grid1[i][:] + [0 for i in range(max2)]) for i in range(N1)] \
    + [[0 for i in range(2 * max2 + M1)] for i in range(max2)]

# for i in max_grid:
#     print(i)
grid2s = [grid2]
for i in range(3):
    grid2s.append(rotation(grid2s[-1], len(grid2s[-1]), len(grid2s[-1][0])))


def find(ng, si, sj):
    for i in range(len(ng)):
        for j in range(len(ng[0])):
            if ng[i][j] == '1' and max_grid[i + si][j + sj] == '1':
                return False
    return True
for i, g in enumerate(grid2s):
    for si in range(N1 + max2):
        for sj in range(M1 + max2):
            if find(g, si,sj):
                # print(si, sj)
                a, b = 0, 0
                if si < max2:
                    a = max(len(g), max2 + N1 - si)
                else:
                    a = max(len(g) + si - max2, N1)
                if sj < max2:
                    b = max(len(g[0]), max2 + M1 - sj)
                else:
                    b = max(len(g[0]) + sj - max2, M1)
                # print(answer, a, b,len(g[0]), len(g[0]) + si - max2, i, si, sj)
                answer = min(answer, a * b)

print(answer)