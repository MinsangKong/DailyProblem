n, m = map(int, input().split())
pre = [0 for i in range(m)]

for i in range(n):
    new = list(map(int, input().split()))
    for j in range(m):
        if pre[j] > new[j - 1] or j == 0:
            new[j] += pre[j]
        else:
            new[j] += new[j - 1]

    pre = new[:]

print(pre[m-1])