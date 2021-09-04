#https://www.acmicpc.net/problem/14712
#백준 14712번 넴모넴모(Easy) (DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(cnt):
    global result
    if cnt == n*m:
        result+=1
        return
    x = cnt // m + 1
    y = cnt % m + 1
    
    dfs(cnt+1)
    if not board[x-1][y] or not board[x][y-1] or not board[x-1][y-1]:
        board[x][y] = 1
        dfs(cnt+1)
        board[x][y] = 0

n, m = map(int, input().split())

board = [[0]*(m+1) for _ in range(n+1)]
result = 0

dfs(0)

print(result)
#백트래킹으로 풀면 답은 옳게 나오지만 시간 초과 발생 
#검색해보니까 python이 느려서 java로는 동일 알고리즘은 정답처리 됨
#결국 정답 처리를 받았지만 서버 상태에 따라서 되는 알고리즘도 계속 시간 초과가 발생