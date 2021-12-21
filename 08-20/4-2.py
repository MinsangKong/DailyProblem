from sys import stdin

n, m, k = map(int, input().split())
money = [0] + list(map(int, input().split()))
parent = [-money[i] for i in range(n + 1)]


def collpsing_find(a):
    global parent
    root = a
    while parent[root] >= 0:
        root = parent[root]

    while parent[a] >= 0:
        s = a
        a = parent[a]
        parent[s] = root
    return root


for i in range(m):
    a, b = map(int, stdin.readline().split())
    root1 = collpsing_find(a)
    root2 = collpsing_find(b)
    if root1 != root2:
        if money[root1] > money[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1

s = 0
for i in range(1, n + 1):
    if parent[i] < 0:
        s += -parent[i]
if s > k:
    print('Oh no')
else:
    print(s)