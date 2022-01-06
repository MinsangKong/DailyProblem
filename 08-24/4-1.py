#https://www.acmicpc.net/problem/15823
#백준 15823번 카드 팩 구매하기 (이분탐색)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = 1
e = n
result = 0

while s <= e :
    mid = (s+e)//2
    card = dict()
    cnt = 0
    
    for i in range(n):
        if nums[i] in card:
            target = card[nums[i]]
            temp = dict()
            for num in card:
                if card[num] > target:
                    temp[num] = card[num]
            card = temp
        card[nums[i]] = i
        if len(card) == mid :
            cnt += 1
            card = dict()
    
    if len(card) >= mid :
        cnt += 1

    if cnt >= m :
        s = mid + 1
        result = mid
    else:
        e = mid - 1
        
print(result)