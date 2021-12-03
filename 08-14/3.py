#https://www.acmicpc.net/problem/14676
#백준 14676번 영우는 사기꾼 (위상정렬)
#import sys
#input = sys.stdin.readline

n,m,k = map(int, input().split())

indegree = [0]*n
info = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    info[x-1].append(y-1)
    indegree[y-1]+=1
    
plays = []
for _ in range(k):
    a,b = map(int, input().split())
    plays.append((a,b-1))
    
flag = True
building = [0]*n
for oper, target in plays:
    if not flag:
        break
    if oper == 1:
        if indegree[target] :
            flag = False
            break
        building[target] +=1
        if building[target] == 1:
            for i in info[target]:
                indegree[i]-=1
    elif oper == 2:
        if building[target] <= 0:
            flag = False
            break
        building[target]-=1
        if building[target] == 0:
            for i in info[target]:
                indegree[i]+=1
        
if flag:
    print("King-God-Emperor")
else:
    print("Lier!")