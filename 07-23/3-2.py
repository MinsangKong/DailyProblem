#https://www.acmicpc.net/problem/5430
#백준 5430번 AC (문자열)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')

    p.replace('RR','')
    rcnt = 0
    s = 0
    e = 0
    
    for c in p :
        if c == 'R':
            rcnt = (rcnt+1)%2
        else:
            if rcnt : 
                e += 1
            else:
                s += 1
    if e+s <= n :
        arr = arr[s:n-e]
        if rcnt :
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
