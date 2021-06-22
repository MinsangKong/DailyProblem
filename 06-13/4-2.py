import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

cost = list(map(int, input().split()))
# g considers broken or not
g = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    # N, 1의 경우 빼고는 a가 더 작게 만들어야 한다.
    if sorted([a, b]) == [1, N]:
        g[N-1] = 1
        continue
    if a > b:
        a, b = b, a
    # 왼쪽 mark
    g[a-1] = 1

if g.count(1) < 2:
    print("YES")
    exit()

INF = float('inf')
for i in range(N):
    if g[i] == 1:
        index = i + 1
        break
g = g[index:] + g[:index]
cost = cost[index:] + cost[:index]
total_value = 0
min_value = INF
# index + i
# print(g)
for i in range(N):
    cur = g[i]
    min_value = min(min_value, cost[i])
    # print(f"{i} : {min_value}")
    if cur:
        total_value += (min_value if min_value != INF else 0)
        min_value = INF
print("YES" if total_value <= K else "NO")