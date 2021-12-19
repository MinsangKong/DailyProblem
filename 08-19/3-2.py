import sys

N = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

info.sort(key=lambda x:x[1])

def isPossible(time:int) -> bool:
    global N, info
    for i in range(N):
        time += info[i][0]
        if time > info[i][1]:
            return False
    return True

answer = -1
L, R = 0, info[-1][1]
while L <= R:
    mid = (L + R) // 2
    if isPossible(mid):
        L = mid + 1
        answer = max(answer, mid)
    else:
        R = mid - 1

print(answer)