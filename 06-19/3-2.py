import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
print = lambda x:sys.stdout.write(str(x) + '\n')

n,m = map(int,input().split())
s,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


queue = deque([(s,0)])
ans = 0

while queue:
    curr,cnt = queue.popleft()
    if curr == e:
        ans = cnt
        break

    # +-1
    for jump in [-1,1]:
        if 1 <= curr + jump <= n and visited[curr+jump] == False:
            visited[curr+jump] = True
            queue.append([curr+jump,cnt+1])

    # tele
    for _next in graph[curr]:
        if visited[_next] == False:
            visited[_next] = True
            queue.append([_next,cnt + 1])


print(ans)
'''
dict가 더 빠를거라고 생각했는데 아니었다.
'''