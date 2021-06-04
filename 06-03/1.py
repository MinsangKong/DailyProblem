#https://www.acmicpc.net/problem/1159
#백준 1159번 농구경기(정렬)
#import sys
#input = sys.stdin.readline

n = int(input())

cnt = 1
result = []

teams = []

for _ in range(n):
    teams.append(input().rstrip())
    
teams.sort()

for i in range(1,n):
    if teams[i][0] == teams[i-1][0]:
        cnt+=1
    else:
        if cnt >= 5:
            result.append(teams[i-1][0])
        cnt = 1
        
if cnt >= 5:
    result.append(teams[-1][0])
    
if result:
    result.sort()
    print("".join(result))
else:
    print("PREDAJA")