#https://www.acmicpc.net/problem/5430
#백준 5430번 AC (문자열)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    case = input().rstrip()
    
    arr = []
    temp = ""
    
    for i in range(1,len(case)):
        if case[i].isdigit():
            temp += case[i]
        else:
            if temp :
                arr.append(int(temp))
                temp = ""
    flag = True
    rcnt = 0
    s = 0
    e = 0
    length = len(arr)
    
    for c in p :
        if c == 'R':
            rcnt = (rcnt+1)%2
        else:
            if length > s + e :
                if rcnt : 
                    e += 1
                else:
                    s += 1
            else:
                flag = False
                break
                
    if flag :
        arr = arr[s:length-e]
        if rcnt % 2 == 1 :
            arr.reverse()
        if arr :
            print('[', end = '')
            for i in range(len(arr)):
                if i == len(arr)-1:
                    print(arr[i], end=']\n')
                else:
                    print(arr[i], end=',')
        else:
            print('[]')            
    else:
        print('error')