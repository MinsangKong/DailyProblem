#https://www.acmicpc.net/problem/19535
#백준 19535번 ㄷㄷㄷㅈ (트리)
#import sys
#input = sys.stdin.readline

def comb(num):
    c = 1
    for i in range(num,num-3,-1):
        c *= i
    return c//6

def find_D():
    global dcount
    for i in range(1,n):
        if len(graph[i]) < 2:
            continue
        for node in graph[i]:
            if node < i :
                continue
            if len(graph[node]) < 2 :
                continue
            dcount += (len(graph[i])-1)*(len(graph[node])-1)           

n = int(input())
graph = [[] for _ in range(n+1)]
dcount = 0
gcount = 0

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1,n+1):
    if len(graph[i]) >= 3 :
        gcount += comb(len(graph[i]))

find_D()

if dcount == 3*gcount:
    print("DUDUDUNGA")
elif dcount > 3*gcount:
    print("D")
else:
    print("G")
#continue를 사용해서 경우의 수를 줄이는 경우가 훨씬 더 빨랐다