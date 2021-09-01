#https://www.acmicpc.net/problem/20438
#백준 20438번 출석체크(그리디, 누적합)
#import sys
#input = sys.stdin.readline

n, k, q, m = map(int, input().split())

students = [0]*(n+3)
sleep = set(map(int, input().split()))
attend = list(map(int, input().split()))
attendPossible = set()

for code in attend:
    if code in sleep:
        continue
    for ncode in range(code, n+3, code):
        if ncode not in sleep:
            attendPossible.add(ncode)
            
for i in range(3, n+3):
    students[i] += students[i-1]
    if i in attendPossible:
        students[i] += 1

for _ in range(m):
    s, e = map(int, input().split())
    print((e-s+1)-(students[e]-students[s-1]))
#python으로 시간 제한을 맞추기 위해서는 누적합을 활용해서 작성해야 한다.   