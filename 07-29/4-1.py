#https://www.acmicpc.net/problem/16434
#백준 16434번 드래곤 앤 던전 (이분탐색)
#import sys
#input = sys.stdin.readline

n, atk = map(int, input().split())
info = []
max_hp = 0
max_hp

for i in range(n):
    data = list(map(int,input().split()))
    if data[0] == 1:
        max_hp =max(max_hp,data[2])
    info.append(data)

s = 1 #다 2번방인거나 체력이 1인경우에는 1로 문제없이 해결할 수 있다 
e = n*max_hp*(max_hp//atk+1)

while s < e :
    mid = (s+e)//2
    cur_hp = mid
    cur_atk = atk
    flag = False
    for t,a,b in info:
        if t == 1 :
            cnt = b//cur_atk if b%cur_atk == 0 else b//cur_atk+1
            cur_hp -= a*(cnt-1)
            if cur_hp <= 0 :
                break
        else:
            cur_hp = min(mid,cur_hp+b)
            cur_atk += a
            
    if cur_hp < 1 :
        s = mid+1
    else:
        e = mid
        
print(e)