#https://www.acmicpc.net/problem/1561
#백준 1561번 놀이 공원 (이분 탐색)
#import sys
#input = sys.stdin.readline

def count(time):
    cnt = 0
    for num in nums:
        cnt += time//num+1
    return cnt

n, m = map(int, input().split())
nums = list(map(int, input().split()))

if n < m :
    print(n)
else:
    s = 0
    e = n*30
    idx = 0

    while s <= e :
        mid = (s+e)//2

        if count(mid) < n :
            s = mid + 1
        else:
            e = mid - 1
            idx = mid
            
    result = count(idx-1)

    for i in range(m) :
        if idx % nums[i] == 0 :
            result += 1
        if result == n :
            print(i+1)
            break