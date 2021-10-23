#https://www.acmicpc.net/problem/7795
#백준 7795번 먹을 것인가 먹힐 것인가 (그리디)
#import sys
#input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    anum = sorted(list(map(int, input().split())))
    bnum = sorted(list(map(int, input().split())))
    result = 0
    cnt = 0
    
    for target in anum :
        for j in range(cnt,b) :
            if target <= bnum[j] :
                break
            cnt += 1
        result += cnt
    print(result)