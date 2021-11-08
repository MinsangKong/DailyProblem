import sys
input = sys.stdin.readline

def watch(x, y, direction):
    ret = set()
    for d in direction:  # 0 ~ 3 : 북, 동, 남, 서
        new_x, new_y = x + dx[d], y + dy[d]
        while 0 <= new_x < N and 0 <= new_y < M:
            if office[new_x][new_y] == 6: break
            if office[new_x][new_y] == 0: ret.add((new_x, new_y))
            new_x, new_y = new_x + dx[d], new_y + dy[d]

    return ret


def dfs(n, watched_set):
    global max_watched_cnt
    if n == len(cctvs_cases):
        if max_watched_cnt < len(watched_set):
            max_watched_cnt = len(watched_set)
        return
    for cctv_cases in cctvs_cases[n]:
        dfs(n + 1, watched_set | cctv_cases)


cctvs_cases = []  # 각 cctv의 가능한 케이스

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)  # 동서남북, 좌표 이동 백터

N, M = map(int, input().split())  # N: 세로, M: 가로
office = [[*map(int, input().split())] for _ in range(N)]  # cctv, 벽 정보

will_watched_cnt = 0
for idx in range(N * M):
    i, j = divmod(idx, M)
    if office[i][j] == 0:
        will_watched_cnt += 1
    elif office[i][j] == 1:
        cctvs_cases.append([watch(i, j, [v]) for v in range(4)])
    elif office[i][j] == 2:
        cctvs_cases.append([watch(i, j, [v % 4, (v + 2) % 4]) for v in range(2)])
    elif office[i][j] == 3:
        cctvs_cases.append([watch(i, j, [v % 4, (v + 1) % 4]) for v in range(4)])
    elif office[i][j] == 4:
        cctvs_cases.append([watch(i, j, [(_ + v) % 4 for _ in range(3)]) for v in range(4)])
    elif office[i][j] == 5:
        cctvs_cases.append([watch(i, j, [0, 1, 2, 3])])

max_watched_cnt = 0
dfs(0, set())  # 감시 가능한 최대 영역 개수

print(will_watched_cnt - max_watched_cnt)  # 최소 사각지대 개수