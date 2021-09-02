#https://www.acmicpc.net/problem/5904
#백준 5904번 Moo 게임(DP)
#import sys
#input = sys.stdin.readline

n = int(input())

mList = set()
cnt = 1
moo = 3

mList.add(1)

while moo < n:
    temp = set()
    check = (cnt+2)*2+1+moo
    print(check)
    for i in mList:
        temp.add(check+i)
    mList.add(moo+1)
    mList.update(temp)
    moo = (moo*2)+(cnt+2)*2+1
    cnt+=1

if n in mList :
    print("m")
else:
    print("o")
#m인 값만 넣어도 메모리 초과 발생