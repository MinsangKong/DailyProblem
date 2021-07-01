#https://www.acmicpc.net/problem/15732
#백준 15732번 도토리 숨기기(이분탐색)
#import sys
#input = sys.stdin.readline

def check(mid):
    total = 0
    for start, end, step in rules:
        point = min(end,mid)
        if start <= point:
            dotori = (point-start) // step + 1
            total += dotori
    return total

n, k, d = map(int, input().split())

rules = [list(map(int, input().split())) for _ in range(k)]

left, right = 1, n
result = 0

while left <= right:
    mid = (left+right) // 2
    
    if check(mid) >= d:
        result = mid
        right = mid-1
    else:
        left = mid+1
        
print(result)
'''
그리디로 풀다가 아무리 봐도 시간초과가 발생할 것 같아서 포기...
이분 탐색 태그를 알면 꽤 할만한 문제지만 이분탐색이 안 떠올라서 오래걸렸다...
'''