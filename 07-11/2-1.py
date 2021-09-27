#https://www.acmicpc.net/problem/18513
#백준 18513번 샘터(그리디)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())
springs = list(map(int, input().split()))

houses = set()
idx = 1
total = 0
for spring in springs:
    houses.add(spring)
while k > 0:
    for spring in springs:
        l, r = spring+idx, spring-idx
        for num in [l,r]:
            if num < -100000000 or num > 100000000:
                continue
            if k == 0:
                break
            if num not in houses:
                houses.add(num)
                k -= 1
                total += idx
    idx += 1
print(total)
#그리디 알고리즘은 계속 66%에서 시간 초과 발생
#그리디라고 생각했지만 더해주는 부분에서 비효율적이었다.
#굳이 반복된 숫자들을 재사용할 필요가 없었는데 반복되는 부분이 너무 많았다.