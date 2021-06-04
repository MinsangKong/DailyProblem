import sys
input = sys.stdin.readline
N, root = map(int, input().split())
g = [[] for i in range(N+1)]
v = [-1] * (N+1)
v[0] = None
for i in range(N-1):
    a, b, d = map(int, input().split())
    g[a].append((b, d))
    g[b].append((a, d))
leaves = []
giga = -1

stk = [(root, 0)]
while stk:
    cur, distance = stk.pop()
    v[cur] = distance
    # Find giga
    if (len(g[cur]) > 2 and giga == -1) or (cur == root and len(g[cur]) == 2 and giga == -1):
        giga = cur
    # Find leaf
    if len(g[cur]) == 1 and cur != root:
        leaves.append(cur)
    for nxt, nd in g[cur]:
        if v[nxt] == -1:
            stk.append((nxt, distance + nd))
d_giga = v[giga] - v[root]
d_leaves = 0 if len(leaves) < 2 else max([v[x] - v[giga] for x in leaves])
print(d_giga, d_leaves)

'''
리프 노드를 별개로 처리하는 방식이 약간 더 빨랐다.
'''