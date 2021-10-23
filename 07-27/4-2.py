import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 다익스트라
def dijkstra(s, e):
    time = [INF for _ in range(n + 1)]
    time[1] = 0
    q = [(0, 1)]
    while q:
        dist, now = heapq.heappop(q)
        if now == n: break
        if time[now] < dist: continue
        for next, plus in graph[now]:
            # 검문소는 지나가지 않는다. 
            if s == now and e == next or s == next and e == now: continue
            if dist + plus < time[next]:
                time[next] = dist + plus
                # 이전 노드 저장
                if not s: pre[next] = now
                heapq.heappush(q, (time[next], next))
    return time[n]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 이전 노드를 저장하는 리스트
pre = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))

result = dijkstra(0, 0)

ans = -1
e = n

while pre[e]!=0:
    s = pre[e]
    output = dijkstra(s, e)
    # 검문소가 없을 때 값과 비교하여 값 변경
    if output != INF:
        diff = output-result
        ans = max(ans, diff)
    else:
        ans = -1
        break
    e = s
print(ans)