#https://www.acmicpc.net/problem/12908
#백준 12908번 텔레포트 3 (BFS)
import sys
#input = sys.stdin.readline

def dfs(total, x, y):
    global result
    
    if x == xe and y == ye :
        result = min(result, total)
        return
    
    for i in range(3):
        a,b,c,d = tele[i]
        if not visited[i][0]:
            visited[i][0] = 1
            dfs(total+abs(a-x)+abs(b-y)+10,c,d)
            visited[i][0] = 0
        if not visited[i][1]:
            visited[i][1] = 1
            dfs(total+abs(c-x)+abs(d-y)+10,a,b)
            visited[i][1] = 0
    dfs(total+abs(x-xe)+abs(y-ye),xe,ye)

xs, ys = map(int, input().split())
xe, ye = map(int, input().split())
tele = []
result = sys.maxsize
visited = [[0]*2 for _ in range(3)]
for _ in range(3):
    a,b,c,d = map(int, input().split())
    tele.append([a,b,c,d])
dfs(0,xs,ys)
print(result)