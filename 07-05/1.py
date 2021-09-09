#https://www.acmicpc.net/problem/1110
#백준 1110번 더하기 사이클(그리디)
#import sys
#input = sys.stdin.readline

N = input()
count = 0
cycle = N

while True:
    if int(N)==0:
        count = 1
        break
    if count >= 1 and N==cycle:
        break
    if int(cycle) < 10:
        cycle=cycle+cycle
    else:
        temp = cycle
        cycle = str(int(cycle[0])+int(cycle[1]))
        if int(cycle) >= 10:
            cycle = cycle[1]
        if int(temp[1]) == 0:
            cycle = cycle[0]
        else:
            cycle = temp[1]+cycle[0]
    count+=1
    
print(count)