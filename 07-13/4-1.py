#https://www.acmicpc.net/problem/17136
#백준 17136번 색종이 붙이기(DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(total, cnt):
    global ans
    if total == 0:
        ans = min(cnt, ans)
        return
    for i in range(10):
        for j in range(10):
            if board[i][j] :
                flag = False
                for k in range(5,0,-1):
                    if papers[k]:
                        if check(i,j,k):
                            papers[k] -= 1
                            change(i,j,k,0)
                            flag = True
                            dfs(total-k**2,cnt+1)
                            change(i,j,k,1)
                            papers[k] += 1
                if not flag:
                    return
                            
                            
def check(x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if 0 <= i < 10 and 0 <= j < 10 :
                if board[i][j] == 0:
                    return False
            else:
                return False
    return True

def change(x,y,size,value):
    for i in range(x,x+size):
        for j in range(y,y+size):
            board[i][j] = value

board = [list(map(int, input().split())) for _ in range(10)]
result = 0
ans = 26
papers = [5]*6
visited = set()

for i in range(10):
    for j in range(10):
        if board[i][j]:
            result += 1

dfs(result,0)

print(ans if ans != 26 else -1)
'''
계속 시간 초과 발생... 어떻게 방문 처리를 해야할지 감이 안잡힌다
'''