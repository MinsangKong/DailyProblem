#https://www.acmicpc.net/problem/18114
#백준 18114번 블랙 프라이데이(투포인터)
#import sys
#input = sys.stdin.readline

n, c = map(int, input().split())
weights = sorted(list(map(int, input().split())))

if c in weights:
    print(1)
else:
    check = False
    l,r = 0,1
    total = weights[0]
    
    while l < r:
        if total == c:
            check = True
            break
        if r == n :
            break

        if total < c:
            total+=weights[r]
            r+=1
        else:
            total-=weights[l]
            l+=1
    if check:
        print(1)
    else:
        print(0)
#계속 1%에서 틀리는 걸로 봐선 투포인터로는 풀 수 없는 문제인것 같다
#dfs로 풀어도 시간 초과가 발생한다.
#최대 물건의 수는 3개로 고정되어 있었다... 문제를 잘 못 이해했다.