#https://www.acmicpc.net/problem/16986
#백준 16986번 인싸들의 가위바위보 (구현, BFS)
#import sys
#input = sys.stdin.readline
from itertools import permutations

def dfs(p1,p2,idx,wins,player):
    global result
    if wins[0] == k :
        result = 1
        return
    if wins[1] == k or wins[2] == k :
        return
    if idx[0] == n :
        return
    
    p3 = 3-(p1+p2)
    pvp1 = player[p1][idx[p1]]-1
    pvp2 = player[p2][idx[p2]]-1
    idx[p1] += 1
    idx[p2] += 1
    if types[pvp1][pvp2] == 2 or (types[pvp1][pvp2] == 1 and p1 > p2):
        wins[p1] += 1
        dfs(p1,p3,idx,wins,player)
    elif types[pvp1][pvp2] == 0 or (types[pvp1][pvp2] == 1 and p2 > p1):
        wins[p2] += 1
        dfs(p2,p3,idx,wins,player)
    
n, k = map(int, input().split())

types = [list(map(int, input().split())) for _ in range(n)]
cases = [i for i in range(1,n+1)]
kyunghee = list(map(int, input().split()))
minho = list(map(int, input().split()))
result = 0

for case in permutations(cases, n):
    player = [case,kyunghee,minho]
    idx = [0,0,0]
    wins = [0,0,0]
    dfs(0,1,idx,wins,player)
    if result :
        break
        
print(1 if result else 0)