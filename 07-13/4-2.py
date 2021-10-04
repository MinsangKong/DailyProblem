#https://www.acmicpc.net/problem/17136
#백준 17136번 색종이 붙이기(DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def check(x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if board[i][j] == 0:
                return False
    return True

def change(x,y,size,value):
    for i in range(x,x+size):
        for j in range(y,y+size):
            board[i][j] = value

def dfs(x,y,cnt):
    global ans
    print(x,y)
    if y >= 10:
        ans = min(ans, cnt)
        return
    
    if x >= 10:
        dfs(0,y+1,cnt)
        return
    
    if board[x][y]:
        for k in range(5):
            if papers[k] :
                if x + k >= 10 or y + k >= 10:
                    continue
                if check(x,y,k+1):
                    change(x,y,k+1,0)
                    papers[k] -= 1
                    dfs(x+k+1,y,cnt+1)
                    papers[k] += 1
                    change(x,y,k+1,1)
    else:
        dfs(x+1,y,cnt)

board = [list(map(int, input().split())) for _ in range(10)]
ans = 26
papers = [5]*5
dfs(0,0,0)

print(ans if ans != 26 else -1)
'''
방문기록을 처리하면서 DFS를 하기가 너무 까다로웠다...
Y축부터 DFS를 처리하고 그 라인의 방문처리가 마무리되면 dfs(0,y+1,cnt)으로
다음번 X축으로 이동한 뒤 X축이 마무리되면 다시 반복
만약에 10행 10열에 도달하지 못한다는 의미는 조건을 만족할 수 없다는 의미이기 때문에
이를 반영하여 출력하면 된다.
'''