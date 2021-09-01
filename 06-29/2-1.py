#https://www.acmicpc.net/problem/20438
#백준 20438번 출석체크(그리디)
#import sys
#input = sys.stdin.readline

n, k, q, m = map(int, input().split())

students = [1]*(n+3)

sleep = list(map(int, input().split()))

attend = list(map(int, input().split()))

for code in attend:
    if code in sleep:
        continue
    idx = 1
    while code * idx < n+3:
        if code * idx in sleep:
            idx+=1
            continue
        students[code*idx] = 0
        idx+=1

checkList = [list(map(int, input().split())) for _ in range(m)]

for s,e in checkList:
    print(sum(students[s:e+1])) #이 과정자체도 O(e-s+1)만큼의 시간이 든다.
#pypy3로는 정답, 그냥 파이썬에서는 시간 초과 발생