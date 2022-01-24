#https://www.acmicpc.net/problem/18234
#백준 18234번 당근 훔쳐먹기 (그리디)
#import sys
#input = sys.stdin.readline

n, t = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
total = 0
    
info.sort(key = lambda x : -x[1])
print(info)
for i in range(n):
    total += info[i][0]+info[i][1]*(t-i-1)
print(total)