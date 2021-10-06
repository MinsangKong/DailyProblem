#https://www.acmicpc.net/problem/20922
#백준 20922번 겹치는건 싫어 (투포인터)
#import sys
#input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

nums = list(map(int, input().split()))

check = deque()
counter = dict()
result = 1
check.append(nums[0])
counter[nums[0]] = 1
for i in range(1,n):
    check.append(nums[i])
    if nums[i] in counter:
        if counter[nums[i]] < k :
            counter[nums[i]] += 1
        else:
            result = max(result, len(check)-1)
            while True:
                num = check.popleft()
                if num == nums[i]:
                    break
                else:
                    counter[num] -= 1
                    if counter[num] == 0 :
                        del counter[num]
    else:
        counter[nums[i]] = 1
result = max(result, len(check))
print(result)          
#서버 문제인지는 모르겠지만 del이 있는 코드가 더 빨랐다