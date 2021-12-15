import copy
from collections import deque
from itertools import permutations
inf = 0xfffffff
D = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [1, 0, 0], [0, 1, 0], [-1, 0, 0]]

def perm2(arr2 = [0, 1, 2, 3, 4], i = 0):
    if i == 5:
        arr2
        return
    for idx in range(i, 5):
        arr2[i], arr2[idx] = arr2[idx], arr2[i]
        perm2(arr2, i+1)
        arr2[i], arr2[idx] = arr2[idx], arr2[i]
perm2()

def perm(arr=[0, 0, 0, 0, 0], i=0):
    if i == 5:
        for arr2 in permutations([0, 1, 2, 3, 4]):
            # 5개의 방향이 다 정해짐
            temp_map = [[[d[arr[idx]][arr2[idx]][j][i] for i in range(5)] for j in range(5)] for idx in range(5)]
            if temp_map[0][0][0] and temp_map[4][4][4]:
                Q = deque()
                Q.append([0, 0, 0, 0])
                vl = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
                vl[0][0][0] = 1
                while Q:
                    x, y, z, dis = Q.popleft()
                    if x == 4 and y == 4 and z == 4:
                        global r
                        r = min(dis, r)
                        return
                    for dx, dy, dz in D:
                        tx, ty, tz = x + dx, y + dy, z + dz
                        if -1 < tx < 5 and -1 < ty < 5 and -1 < tz < 5 and temp_map[tz][ty][tx] and not vl[tz][ty][tx]:
                            vl[tz][ty][tx] = 1
                            Q.append([tx, ty, tz, dis+1])
                            # if tx == 2 and ty == 2 and tz == 1:
                            #     kkkk = 0
        return
    for j in range(4):
        arr[i] = j
        perm(arr, i+1)
    arr[i] = 0


nl = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
d = [nl]
r = inf
for i in range(3):
    temp = [[[d[-1][k][i][4-j] for i in range(5)] for j in range(5)] for k in range(5)]
    d.append(temp)
perm()
if r == inf:
    r = -1
print(r)