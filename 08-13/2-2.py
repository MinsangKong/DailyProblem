import sys
input = sys.stdin.readline
S = input().strip()
t = int(input())

p = [[0]*26]
for c in S:
    cnt = p[-1][:]
    cnt[ord(c)-97] += 1
    p.append(cnt)

for _ in range(t):
    a, l, r = input().split()
    l, r = map(int, (l, r))
    print(p[r+1][ord(a)-97] - p[l][ord(a)-97])