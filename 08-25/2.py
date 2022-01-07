#https://www.acmicpc.net/problem/15566
#백준 15566번 개구리 1 (백트래킹)
import sys
#input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(idx):
    if idx == n+1:
        for i in range(1,n+1):
            if not lotus[i]:
                return
            for j in range(1,i):
                if log[i][j]:
                    t = log[i][j]
                    if info[lotus[i]][t] != info[lotus[j]][t] :
                        return
        print("YES")
        for i in range(1,n+1):
            print(lotus[i], end=' ')
        sys.exit(0)
        
    for target in frog[idx]:
        if lotus[target] :
            continue
        lotus[target] = idx
        dfs(idx+1)
        lotus[target] = 0

n,m = map(int, input().split())
info = [[]]
for _ in range(n):
    data = [0]+list(map(int, input().split()))
    info.append(data)
frog = [[] for _ in range(n+1)]
log = [[0]*(n+1) for _ in range(n+1)]
lotus = [0]*(n+1)

for i in range(1,n+1):
    a,b = map(int, input().split())
    if a == b :
        frog[i].append(a)
    else:
        frog[i].append(a)
        frog[i].append(b)
        
for _ in range(m):
    a,b,t = map(int, input().split())
    log[a][b] = t
    log[b][a] = t
    
dfs(1)
print("NO")