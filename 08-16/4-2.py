from collections import deque
from copy import deepcopy
from itertools import permutations

N, K = list(map(int, input().split()))
pyo = [list(map(int, input().split())) for _ in range(N)]
miri = [[]]
miri += [list(map(int, input().split())) for _ in range(2)]

def sol():
    for order in permutations([i for i in range(1, N+1)], N):
        miri[0] = order
        idx = [0, 0, 0]
        win = [0, 0, 0]
        player = [0, 1, 2]

        while True:
            # game
            p_1 = miri[player[0]][idx[player[0]]] - 1
            p_2 = miri[player[1]][idx[player[1]]] - 1
            idx[player[0]] += 1
            idx[player[1]] += 1
            result = pyo[p_1][p_2]
            if result == 0 or (result == 1 and player[1] > player[0]):
                win[player[1]] += 1
                temp = player[0]
                player[0] = player[2]
                player[2] = temp
            elif result == 2 or (result == 1 and player[0] > player[1]):
                win[player[0]] += 1
                temp = player[1]
                player[1] = player[2]
                player[2] = temp

            if win[0] == K:
                return 1
            elif win[1] == K or win[2] == K or 20 in win or idx[0] == N:
                break
    return 0

print(sol())