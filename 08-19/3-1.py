#https://www.acmicpc.net/problem/6068
#백준 6068번 시간 관리하기 (정렬, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
times = []
total = 0
limit = 0

for _ in range(n):
    time, e = map(int, input().split())
    times.append([e,time])
    total += time
    limit = max(limit,e)

if total > limit :
    print(-1)
else:
    times.sort(key = lambda x : (x[0],x[1]))

    s = times[0][0]-times[0][1]
    answer = -1

    for i in range(s,-1,-1):
        start = i
        flag = True
        for j in range(n):
            e, time = times[j]
            start += time
            if start > e:
                flag = False
                break
        if flag:
            answer = i
            break

    print(answer)
#동일한 끝점일 때를 고려해야 하기 때문에 단순히 heapq로 처리하면 틀렸다고 나온다
#완전 탐색을 하는 방식으로 구현했지만 더 효율적인 방법이 있을것 같다.
#내가 생각한 효율적인 방법은 가지 치기를 통해 1020->76ms까지 줄였다
#지금 문제의 경우에는 경우의 수가 적어서 가지치는 방식이 더 빨랐지만,
#입력이 더 컸다면 이분탐색이 최선이었을 것 같다.