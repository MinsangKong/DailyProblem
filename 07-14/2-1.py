#https://www.acmicpc.net/problem/4811
#백준 4811번 알약(DFS)
#import sys
#input = sys.stdin.readline

while True:
    def dfs(message, w, h):
        if w == 0 and h == 0:
            global cnt
            if message not in book:
                cnt += 1
        if w > 0 :
            dfs(message+"w",w-1,h+1)
        if h > 0 :
            dfs(message+'h',w,h-1)
            
    n = int(input())
    if n == 0 :
        break
    
    cnt = 0
    book = dict()
    
    dfs("",n,0)
    print(cnt)
    
#DFS 방식으로는 시간 초과발생