#https://www.acmicpc.net/problem/17490
#백준 17490번 일감호에 다리 놓기(그리디)
import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split())
stones = list(map(int, input().split()))
pair = []

for _ in range(m):
    a,b = map(int, input().split())
    if a > b and a != n:
        a,b = b, a
    pair.append([a-1,b-1])

if m <= 1:
    print("YES")
    sys.exit()
pair.sort()

last = 0
result = 0

for i in range(m):
    point = INF
    left = pair[i][0]
    right = pair[i][1]
    for j in range(last,left+1):
        point = min(point,stones[j])
    if last == 0 and pair[-1][1] != 0:
        end = pair[-1][1]
        for j in range(n-1,end-1,-1):
            point = min(point, stones[j])
    result+= point
    last = right
    
if result <= k:
    print("YES")
else:
    print("NO")