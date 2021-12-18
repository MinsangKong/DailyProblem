import sys

n, m = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

column = []
for j in range(m):
    res = 0
    for i in range(n):
        if i % (n-1) == 0: res += num[i][j]
        else:              res += 2*num[i][j]
    if j % (m-1) == 0: column.append(res)
    else:              column.append(2*res)

row = []
for i in range(n):
    res = 0
    for j in range(m):
        if j % (m-1) == 0: res += num[i][j]
        else:              res += 2*num[i][j]
    if i % (n-1) == 0: row.append(res)
    else:              row.append(2*res)

if m == 2:
    if n == 2:
        print(sum(row))
    else:
        print(sum(row) + max(0, max(row[0], row[-1]) - min(row[1:-1])//2))
else:
    if n == 2:
        print(sum(row) + max(0, max(column[0], column[-1]) - min(column[1:-1])//2))
    else:
        print(sum(row) + max(0, max(row[0], row[-1]) - min(row[1:-1])//2, max(column[0], column[-1]) - min(column[1:-1])//2))