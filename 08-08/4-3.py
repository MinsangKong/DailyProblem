import sys
input = sys.stdin.readline

N = int(input())
lines = [0 for _ in range(N + 1)]
two_nodes = [0] * (N - 1)

for i in range(N - 1):
    A, B = map(int, input().split())
    two_nodes[i] = (A, B)
    lines[A] += 1
    lines[B] += 1

G = D = 0
for left, right in two_nodes:
    D += (lines[left] - 1) * (lines[right] - 1)

for line in lines:
    if line >= 3:
        G += line * (line - 1) * (line - 2) // 6 

ans = "G"
if D == G * 3:
    ans = "DUDUDUNGA"
elif D > G * 3:
    ans = "D"

print(ans)