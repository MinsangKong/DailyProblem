#https://www.acmicpc.net/problem/5904
#백준 5904번 Moo 게임(점화식)
#import sys
#input = sys.stdin.readline

def check(idx):
    if idx <= 3:
        if idx == 1: 
            return 'm'
        else:
            return 'o'
    
    point = 1
    
    while idx > moo[point]:
        point+=1
        
    if idx <= moo[point]-moo[point-1]: # 중간에 위치할 경우
        if idx-moo[point-1] == 1:
            return "m"
        else:
            return "o"
        
    return check(idx-moo[point-1]-(point+3)) # 중간에 위치하는 경우가 아니면 다시 재귀로 처리

n = int(input())

moo = []
moo.append(3)
cnt = 4

while n > moo[-1]:
    moo.append(moo[-1]*2+cnt)
    cnt+=1

print(check(n))
#길이를 기준으로 재귀를 통해 구하는 방식은 문제 없이 출력됨